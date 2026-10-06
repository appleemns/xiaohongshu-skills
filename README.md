# 小红书小店 AI 员工团队

小红书（企业店）AI 员工团队技能包：4 名 AI 员工（店长 / 运营 / 美工 / 客服）+ 13 个可复用技能，覆盖选品上架、内容笔记、图片素材、活动策划、客户售后、达人合作、数据看板的完整运营闭环。

## 员工与技能清单

| 员工 | 职责 | 技能 |
|---|---|---|
| 1 号 店长 | 整体运营、活动策划、任务分配、数据输出、账号运营决策 | `xhs-team-manager`（入口）· `xhs-task-dispatcher` · `xhs-store-dashboard` · `xhs-campaign-planner` · `xhs-qianfan-web` |
| 2 号 运营 | 选品、上架、笔记发布、粉丝互动 | `xhs-product-picker` · `xhs-product-listing` · `xhs-note-publishing` · `xhs-fan-operations` |
| 3 号 美工 | 商品图 / 笔记封面 / 活动海报制作、主图 CTR 分析与优化 | `xhs-image-production` · `xhs-main-image-ctr` |
| 4 号 客服 | 客户接待与售后回复、达人邀约与跟进 | `xhs-customer-reply` · `xhs-influencer-outreach` |

## 目录结构

```
xiaohongshu-skills/
├── 00-团队手册.md          # 团队 SOP、角色权限、红线
├── AGENTS.md               # 店长（员工 1 号）工作规范
├── 使用说明.md              # 部署与使用说明
├── serve.py                # 数据分析平台本地服务
├── 01-店长/                # 店长技能
├── 02-运营/                # 运营技能
├── 03-美工/                # 美工技能
├── 04-客服/                # 客服技能
├── api/                    # 小红书开放平台 API 客户端（可选，默认千帆浏览器直连）
│   ├── auth_guide.md       # 登录与授权说明
│   ├── config.example.json # 配置示例（真实配置不入库）
│   └── xhs_client.py       # 数据导入/归一化客户端
├── data/                   # 数据目录（示例文件入库，运行时数据不入库）
├── docs/                   # 工作流总览、数据分析平台（HTML）
├── reports/                # 日报/周报模板
└── tasks/                  # 任务卡模板
```

## 部署说明

1. 将各员工目录下的 `skills/` 技能安装到豆包（Doubao）用户技能目录。
2. 数据默认通过豆包浏览器登录千帆商家后台（seller.xiaohongshu.com）直连读取，首次需老板扫码，登录态长期保留。
3. 每日第 0 步：店长检查登录态；失效则提醒老板重新扫码。
4. 可选升级：开通小红书开放平台 API 后，填写 `api/config.json`（复制自 `config.example.json`）并启用。

## 安全约定

- 凭证不落盘（扫码优先），API 密钥等真实配置不入库。
- 只操作本店账号；触发验证码/风控立即停止并人工介入。
- 数据来源标注「千帆后台 / 蒲公英后台 / 估算」，寄样审批必须留痕。

## 使用协议

仅供个人/团队内部使用，请遵守小红书平台规则与相关法律法规。
