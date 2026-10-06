# data/ 数据目录说明

本目录存放店铺运营数据。所有数据标注口径（网页读取 / 手动导出 / API / 估算）。

## 目录结构

| 路径 | 内容 |
|---|---|
| data/manual/ | 千帆后台手动导出的 CSV（`YYYY-MM-DD_<模块>.csv`） |
| data/orders/ | 订单数据（API 拉取或归一化后） |
| data/analytics/ | 流量/转化/商品表现数据 |
| data/notes/ | 笔记文案存档（`YYYY-MM-DD-标题.md`）与笔记数据 |
| data/influencers/ | 达人跟进表 |
| data/products/ | 商品资料（`<SKU>/product-info.md`、listing-copy.md、图片） |
| data/dashboard.json | **数据分析平台数据源**（店长每日更新） |

## dashboard.json Schema（数据分析平台读取）

```json
{
  "store": { "name": "店铺名", "type": "企业店", "category": "主营类目", "updated": "2026-10-02", "data_source": "千帆网页读取" },
  "daily": [
    { "date": "2026-10-01", "gmv": 0, "orders": 0, "aov": 0, "refund_rate": 0, "visitors": 0, "conversion": 0, "followers_gained": 0 }
  ],
  "products": [
    { "sku": "", "name": "", "impressions": 0, "clicks": 0, "ctr": 0, "orders": 0, "gmv": 0, "stock": 0, "status": "在售" }
  ],
  "notes": [
    { "note_id": "", "title": "", "type": "图文", "impressions": 0, "reads": 0, "likes": 0, "comments": 0, "collects": 0, "shares": 0, "fans_gained": 0, "has_product_card": true, "date": "2026-10-01" }
  ],
  "followers": [
    { "date": "2026-10-01", "followers": 0, "new_fans": 0 }
  ],
  "traffic": [
    { "source": "搜索", "value": 0 }, { "source": "推荐", "value": 0 }, { "source": "关注", "value": 0 }, { "source": "其他", "value": 0 }
  ],
  "fans_profile": { "gender": [], "age": [], "city": [] },
  "influencers": [
    { "name": "", "platform": "蒲公英", "stage": "邀约", "note_type": "报备", "gmv": 0, "date": "2026-10-01" }
  ],
  "alerts": [
    { "level": "高", "category": "CTR", "message": "", "sku": "", "date": "2026-10-01" }
  ]
}
```

- 无数据的数组写 `[]`，不要省略字段名；数字为 0 时保留 0。
- `data_source` 只允许：`千帆网页读取` / `手动导出` / `官方 API` / `估算`。
- 更新方式：店长每日晚报前用 `xhs-store-dashboard` 技能更新本文件；`docs/数据分析平台.html` 自动读取（需 `python serve.py` 提供本地服务，或手动导入）。

## 命名规范

- 手动导出：`data/manual/YYYY-MM-DD_<模块>.csv`
- 笔记文案：`data/notes/YYYY-MM-DD-标题.md`
- 商品资料：`data/products/<SKU>/product-info.md`
