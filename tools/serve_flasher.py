#!/usr/bin/env python3
"""
serve_flasher.py, Sirve el repo local en localhost:8080
para que flasher.html pueda acceder a los binarios compilados.

Uso:  python tools/serve_flasher.py
Luego abrir: http://localhost:8080/tools/flasher.html
"""
import http.server
import socketserver
import os
import webbrowser

PORT = 8080
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = f"http://localhost:{PORT}/tools/flasher.html"


class CORSHandler(http.server.SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler con CORS y sin logs verbosos."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=REPO_ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        # Solo muestra GETs de binarios y la página principal
        path = args[0] if args else ""
        if ".bin" in str(path) or "flasher.html" in str(path):
            super().log_message(fmt, *args)


if __name__ == "__main__":
    os.chdir(REPO_ROOT)
    with socketserver.TCPServer(("", PORT), CORSHandler) as httpd:
        httpd.allow_reuse_address = True
        print("=" * 55)
        print("  SomloK Flasher, servidor local")
        print("=" * 55)
        print(f"\n  Abre en Chrome/Edge:\n  {URL}\n")
        print("  Ctrl+C para detener\n")
        webbrowser.open(URL)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Servidor detenido.")
