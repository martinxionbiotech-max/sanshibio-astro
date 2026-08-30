你是资深前端设计工程师，任务：优化一个 Astro 5 + Tailwind CSS 3 的赛鸽基因检测企业官网（河北三狮生物科技有限公司）的**视觉设计与图文搭配**。只做设计/视觉层，不改内容。

## 项目背景
- 项目目录：`~/sanshibio-astro`（已是 git 仓库，main 分支，请勿 push）
- 技术栈：Astro 5.5 + @astrojs/tailwind 6 + Tailwind CSS 3.4，纯静态输出
- 行业风格：生物科技 / 医疗健康，专业、干净、可信（参考 MediSite 模板的 clean/professional 风格）
- 主题色：tailwind.config.mjs 已定义 `brand`（emerald 绿 50-900）与 `deep`（teal）色系，请沿用，不要换配色方案
- 现有图片素材（public/images/）：logo.png、banner-home.png(260x95)、banner-home2.jpg(1920x900)、banner-home3.jpg(1920x893)、banner-about.jpg(1920x301)、company-intro.png(864x462)、honor.jpg、q162d.jpg(500x400)、es08.jpg(500x400)

## 你的任务（仅设计/视觉层）

1. **先运行 `npm install`**（node_modules 缺失，npm 版本 10.9.8）
2. **Hero 图文化**：首页 hero 目前是 CSS 纯渐变，改为用 `banner-home2.jpg`（或 banner-home3.jpg）作背景图，叠加半透明渐变遮罩保证文字可读，可用 `<img>` 或 CSS background
3. **页面顶部 banner**：关于三狮页 / 其他子页顶部可用 `banner-about.jpg`（1920x301 宽幅）或渐变，自选
4. **图文搭配优化**：
   - 首页「三大核心业务」卡片可加图标或配图，提升视觉层次
   - 产品中心 Q162D / ES08 图片展示优化（当前图片偏小）
   - 关于页 company-intro.png、荣誉 honor.jpg 展示优化
5. **组件化（推荐）**：把 Header / Footer / Hero 抽取到 `src/components/` 复用，减少重复
6. **响应式**：确保 375px–1440px 宽度下布局良好，移动端导航可用
7. **视觉细节**：卡片阴影、hover 过渡、间距统一、表格样式美化、字体层级

## 硬性约束（严格遵守，违反即失败）

1. **禁止修改任何中文文案**（正文、标题、描述、按钮文字一个字都不能改）
2. **禁止删除或修改 JSON-LD 结构化数据**（所有 `<script type="application/ld+json">` 块）
3. **禁止修改 `src/content/blog/*.md` 文章的正文与 frontmatter**
4. **禁止新增或删除页面路由**（保持现有 8 个页面 + blog 结构不变）
5. 图片可优化压缩但不要删除；无压缩工具就保持原样

## 验收标准

1. `npm run build` 构建通过，无报错
2. 18 个 HTML 页面正常生成
3. 所有中文文案与 JSON-LD 与修改前一致（用 `git diff` 自查，确保 diff 只涉及 class 名、结构、图片引用等设计层改动）

## 交付

1. 完成后运行 `git add -A && git commit -m "设计优化:hero图文化+组件化+视觉细节"`（**不要 push**）
2. 最后用简短中文回复：你修改了哪些文件、做了哪些设计改进、构建是否通过
