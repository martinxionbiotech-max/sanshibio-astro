const MARKDOWN_ACCEPT = /(?:^|,)\s*text\/markdown(?:\s*;\s*q=([0-9.]+))?/i;

function wantsMarkdown(request) {
  const accept = request.headers.get('Accept') || '';
  const match = accept.match(MARKDOWN_ACCEPT);
  if (!match) return false;
  const q = match[1] === undefined ? 1 : Number(match[1]);
  return Number.isFinite(q) && q > 0;
}

function markdownPath(pathname) {
  if (pathname === '/') return '/markdown/home.md';
  if (pathname === '/en/' || pathname === '/en') return '/markdown/en.md';
  const rel = pathname.replace(/^\/+|\/+$/g, '');
  return `/markdown/${rel}.md`;
}

export async function onRequest(context) {
  const { request, next, env } = context;
  const url = new URL(request.url);

  // Only negotiate for page URLs, never for the mirror files themselves.
  if (wantsMarkdown(request) && !url.pathname.startsWith('/markdown/')) {
    if (env.ASSETS) {
      const mdUrl = new URL(markdownPath(url.pathname), url);
      const asset = await env.ASSETS.fetch(new Request(mdUrl, request));
      if (asset.status === 200) {
        const headers = new Headers(asset.headers);
        headers.set('Content-Type', 'text/markdown; charset=utf-8');
        headers.set('Vary', 'Accept');
        headers.set('Link', '</llms.txt>; rel="describedby", </sitemap-index.xml>; rel="sitemap"');
        return new Response(asset.body, { status: 200, headers });
      }
    }
  }

  const response = await next();
  const headers = new Headers(response.headers);
  headers.set('Vary', 'Accept');
  return new Response(response.body, { status: response.status, headers });
}
