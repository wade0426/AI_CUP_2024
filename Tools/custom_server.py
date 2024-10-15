import http.server
import socketserver
import os

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        ctype = super().guess_type(path)
        if ctype == 'text/plain':
            return 'text/plain; charset=utf-8'
        return ctype

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                content = f.read()
                try:
                    content.decode('utf-8')
                    self.send_header("Content-Type", "text/plain; charset=utf-8")
                except UnicodeDecodeError:
                    pass  # 如果不是 UTF-8，使用默认处理
        return super().send_head()

handler = MyHTTPRequestHandler

with socketserver.TCPServer(("", 8000), handler) as httpd:
    print("Server started at localhost:8000")
    httpd.serve_forever()