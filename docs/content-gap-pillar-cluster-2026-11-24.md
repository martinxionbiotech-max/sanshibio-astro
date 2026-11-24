# SanshiBio — 内容 Pillar / Cluster 缺口清单

日期：2026-11-24  
范围：`src/content/blog`（43 篇中文）+ `src/content/blog-en`（42 篇英文）  
数据：`data/content-inventory.csv`、`data/content-gap.csv`

## 1. 结论

当前不是“没有内容”，而是：

- 有 4 个博客分类，但没有真正的 **pillar hub**。
- 现有 85 篇中，**43 篇中文全部低于 600 词**；英文平均约 1,358 词。
- 有 1 篇中文文章没有英文对应：`test-report-interpretation`。
- 文章集中在“病毒防控 / 检测指南 / 飞行基因”，但缺少：
  - 育种选配
  - 实验室/设备/试剂
  - 样本与报告质量
  - 营养/换羽/训练
  - 引种/检疫/赛事公平
  - 服务政策/价格/售后
  - 国际 B2B/出口样本寄送

## 2. 现有内容分布

| Pillar | 中文 | 英文 | 判断 |
|---|---:|---:|---|
| Pathogen & Health | 14 | 14 | 数量最多，缺生物安全/免疫程序/混合感染 |
| Flight Genetics | 6 | 7 | 有单基因文章，缺基因互作与遗传限制 |
| Testing Workflow & Reports | 7 | 5 | 缺样本质量、假阴假阳、实验室选择 |
| Lab, Equipment & Reagents | 4 | 4 | 无 pillar，缺实验室搭建与质控 |
| Breeding & Selection | 3 | 3 | 无 pillar，缺配对/近交/选择指数 |
| Bloodline & Identity | 3 | 3 | 有亲子/身份文章，缺 SNP 限制与样本链 |
| Nutrition, Molting & Training | 2 | 2 | 无 pillar，缺比赛期营养与恢复 |
| Trade, Quarantine & Race Integrity | 2 | 2 | 无 pillar，缺引种/检疫/拍卖防伪 |
| Service & Pricing | 2 | 2 | 无 pillar，缺服务条款/复检/样本寄送 |
| International / English B2B | 0 | 0 | 完全缺失 |

## 3. 缺失的 Pillar

### P1

1. **Testing Workflow & Reports**
   - 现有：检测指南 12 篇
   - 缺：样本拒收/质量、假阴假阳、复检、实验室选择、报告解读英文版
   - 目标 hub：`/blog/testing-workflow/` 或 `/testing/`

2. **Breeding & Selection**
   - 现有：3 篇
   - 缺：基因型配对、近交/遗传多样性、选择指数、多代选育
   - 目标 hub：`/blog/breeding-selection/`

3. **Lab, Equipment & Reagents**
   - 现有：4 篇
   - 缺：实验室分级、qPCR 验证/污染控制、试剂储存、设备 ROI
   - 目标 hub：`/blog/lab-equipment/`

4. **Service & Pricing**
   - 现有：2 篇价格文章
   - 缺：样本寄送/链式 custody、复检/退款、同意与样本保留、B2B 合作
   - 目标 hub：`/service-policy/` + `/sample-consent-retention/`

5. **International / English B2B**
   - 现有：0
   - 缺：出口样本寄送、目的国规则、英文 partner 页、监管范围页
   - 目标：`/en/partners/`、`/en/regulatory-scope/`

### P2

6. **Nutrition, Molting & Training**
   - 现有 2 篇
   - 缺：比赛期营养、恢复、训练负荷、饮水/补剂

7. **Trade, Quarantine & Race Integrity**
   - 现有 2 篇
   - 缺：进口检疫、拍卖防伪/AB 验证、运输保险、身份文件

8. **Pathogen & Health**
   - 现有 28 篇，数量足
   - 缺：免疫程序、生物安全、混合感染检测算法、抗菌药管理

9. **Flight Genetics**
   - 现有 13 篇
   - 缺：基因互作、多基因限制、遗传 vs 训练、幼鸽选择矩阵

## 4. 缺失的 Cluster（优先批次）

详细表：`data/content-gap.csv`

### 第一批 10 篇

1. 基因互作与多基因限制  
2. 遗传潜力 vs 训练/环境  
3. SNP 面板限制与亲权概率  
4. 亲子鉴定样本类型与链式 custody  
5. 鸽用疫苗程序与时间  
6. 鸽舍生物安全与隔离  
7. 样本拒收与质量控  
8. 假阴性/假阳性如何解读  
9. 基因型配对策略  
10. 近交与遗传多样性  

### 第二批 10 篇

11. 实验室分级搭建  
12. qPCR 验证与污染控制  
13. 比赛期营养  
14. 恢复与训练负荷  
15. 进口检疫流程  
16. 拍卖防伪与 AB 验证  
17. 样本寄送与链式 custody  
18. 复检/退款/服务政策（页面，不是博客）  
19. 样本同意与保留（页面）  
20. 英文 B2B partner 页  

## 5. 内容标准

- 不设定固定字数上限；按问题复杂度完整回答。
- 中文与英文应有相同证据标准，不做“中文摘要版 + 英文完整版”。
- 关键数字（99.99%、99.9%、Ct、SNP 数、基因数）必须有来源或标注为方法学说明。
- 医学/兽医声明必须标明不是诊疗建议。
- 不把“基因优良”写成“保证成绩”。
- 每篇至少连接：一个产品/服务页、一个相关基因/病原页、一个检测流程页。

## 6. 立即执行的修复

1. ✅ 已补 `test-report-interpretation` 英文版（2026-11-24）。
2. 为现有 4 个分类建立 pillar hub（检测、病原、飞行、血统）。
3. 按第一批 10 篇建立内容 brief。
4. 中文文章按“证据完整”而非“字数”扩写；先做商业价值最高的 10 篇。
5. 法律/AIO 修复与内容并行，不互相阻塞。


## 7. 本轮已修复

- 新增英文文章 `test-report-interpretation`，中文/英文博客文件数变为 43 / 43。
- 建立 `data/content-inventory.csv` 与 `data/content-gap.csv`。
- 建立 Pillar / Cluster 缺口清单。

## 8. 尚未修复

- 43 篇中文 blog 仍普遍偏薄（低于 600 词）。
- 4 个现有分类仍缺 pillar hub。
- 育种、实验室、服务政策、营养训练、贸易检疫、国际 B2B 仍缺内容。
