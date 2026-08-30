# 三狮生物 (Sanshi Bio) — Astro 静态站

河北三狮生物科技有限公司官网（重建版），基于 Astro 5 + Tailwind CSS 3，部署于 Cloudflare Pages。

## 技术栈

- Astro `^5.5.0`
- `@astrojs/tailwind` `^6.0.2` + Tailwind CSS `^3.4.19`
- 纯静态输出，无 SSR 适配器

## 页面结构

| 路由 | 内容 |
|------|------|
| `/` | 首页（三大业务 + 公司简介 + 服务流程 + 检测项目） |
| `/about` | 关于三狮（公司简介、三位一体、荣誉资质） |
| `/flight-ability` | 赛鸽飞行能力基因检测（8 项基因） |
| `/virus-detection` | 赛鸽病毒检测（10 种病原体） |
| `/products` | 产品中心（Q162D / ES08 + 试剂产品线） |
| `/services` | 检测服务（基因身份证 / AB 鸽 / 亲缘 / 性别 / 培训） |
| `/contact` | 联系我们 |

## 本地开发

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # 输出到 dist/
npm run preview  # 预览构建产物
```

## 部署（Cloudflare Pages）

- 框架预设：Astro
- 构建命令：`npm run build`
- 输出目录：`dist`
- 域名：`sanshibio.com`（可自行调整，同时更新 `astro.config.mjs` 的 `site`、`public/sitemap.xml`、`public/llms.txt`、`public/robots.txt` 中的域名）

## 图片

`public/images/` 下的图片来自原官网（cdn.myxypt.com）与公开资料，版权归原作者所有。
