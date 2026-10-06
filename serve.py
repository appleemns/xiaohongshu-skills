#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书小店团队 · 本地数据服务
在 D:\\xiaohongshu-team 目录下运行：
    python serve.py
然后浏览器打开 http://localhost:8000/docs/数据分析平台.html
数据分析平台会自动读取 data/dashboard.json；也可直接在页面「数据导入」手动上传。
"""
import http.server
import socketserver
import os
import sys
import webbrowser

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        # 允许本地读取 JSON，避免跨域限制
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("[server] %s\n" % (fmt % args))


if __name__ == "__main__":
    os.chdir(ROOT)
    url = f"http://localhost:{PORT}/docs/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B9%B3%E5%8F%B0.html"
    print("=" * 60)
    print("小红书小店数据分析平台 · 本地服务已启动")
    print(f"  打开: {url}")
    print("  按 Ctrl+C 停止服务")
    print("=" * 60)
    try:
        if not os.environ.get("XHS_SKIP_OPEN"):
            webbrowser.open(url)
    except Exception:
        pass
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务已停止")
