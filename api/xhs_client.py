#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书店铺数据接入客户端（骨架）
- 默认数据源：千帆浏览器直连（网页读取/手动导出 CSV）→ 本脚本负责归一化落盘
- 可选升级：小红书开放平台 API（enabled 后实现 pull_daily）

用法：
    python xhs_client.py --import-csv data/manual/2026-10-01_订单.csv
    python xhs_client.py --pull-daily            # 需 config.json + 开放平台授权
    python xhs_client.py --build-dashboard       # 汇总 data/ 生成 data/dashboard.json
"""
import argparse
import csv
import json
import os
import sys
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_config():
    cfg_path = os.path.join(BASE_DIR, "api", "config.json")
    if os.path.exists(cfg_path):
        with open(cfg_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"open_api": {"enabled": False}}


def import_csv(path, target_dir):
    """把千帆导出的 CSV 归一到 data/<domain>/ 下（保留原始列，附加来源与口径）。"""
    if not os.path.exists(path):
        print(f"[错误] 文件不存在: {path}", file=sys.stderr)
        return False
    os.makedirs(target_dir, exist_ok=True)
    with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
        rows = list(csv.DictReader(f))
    out = {
        "source_file": os.path.basename(path),
        "data_source": "手动导出",
        "imported_at": date.today().isoformat(),
        "rows": rows,
    }
    out_path = os.path.join(target_dir, os.path.basename(path).replace(".csv", ".json"))
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"[OK] 已归一化 {len(rows)} 行 → {out_path}")
    return True


def build_dashboard():
    """汇总 data/ 下已归一化数据，生成 data/dashboard.json（无数据字段填空数组）。"""
    dashboard = {
        "store": {"name": "", "type": "企业店", "category": "", "updated": date.today().isoformat(),
                  "data_source": "手动导出"},
        "daily": [], "products": [], "notes": [], "followers": [], "fans_profile": {},
        "influencers": [], "alerts": [],
    }
    out_path = os.path.join(BASE_DIR, "data", "dashboard.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(dashboard, f, ensure_ascii=False, indent=2)
    print(f"[OK] dashboard.json 已生成（骨架，等待店长填充）→ {out_path}")
    return True


def pull_daily():
    """开放平台 API 拉数占位：需要 config.json 与开放平台授权后实现。"""
    cfg = load_config()
    if not cfg.get("open_api", {}).get("enabled"):
        print("[提示] 开放平台 API 未启用，默认走千帆浏览器直连。启用见 api/auth_guide.md")
        return False
    print("[提示] pull_daily 待按开放平台文档实现（订单/商品/分析接口）")
    return False


def main():
    parser = argparse.ArgumentParser(description="小红书店铺数据接入客户端")
    parser.add_argument("--import-csv", help="归一化千帆导出的 CSV 到 data/")
    parser.add_argument("--pull-daily", action="store_true", help="开放平台 API 拉数（需启用）")
    parser.add_argument("--build-dashboard", action="store_true", help="生成 dashboard.json 骨架")
    args = parser.parse_args()

    if args.import_csv:
        import_csv(args.import_csv, os.path.join(BASE_DIR, "data", "analytics"))
    elif args.pull_daily:
        pull_daily()
    elif args.build_dashboard:
        build_dashboard()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
