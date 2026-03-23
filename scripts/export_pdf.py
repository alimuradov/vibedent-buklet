#!/usr/bin/env python3

from __future__ import annotations

import contextlib
import socket
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "ВайбДент — Буклет.pdf"
CHROME = "/usr/bin/google-chrome"


class SilentHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:
        return


@contextlib.contextmanager
def local_server(root: Path):
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        host, port = sock.getsockname()

    handler = lambda *args, **kwargs: SilentHandler(*args, directory=str(root), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{port}/index.html?export=1"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def build_pdf(output_path: Path) -> None:
    with local_server(ROOT) as url, sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            executable_path=CHROME,
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-gpu",
                "--disable-dev-shm-usage",
            ],
        )
        page = browser.new_page(viewport={"width": 1123, "height": 794}, device_scale_factor=1)
        page.goto(url, wait_until="networkidle", timeout=60000)
        page.emulate_media(media="print")
        page.pdf(
            path=str(output_path),
            format="A4",
            landscape=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            print_background=True,
            prefer_css_page_size=True,
        )
        browser.close()


def main() -> None:
    build_pdf(OUTPUT)
    print(f"Saved PDF to: {OUTPUT}")


if __name__ == "__main__":
    main()
