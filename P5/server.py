import http.server
import socketserver

PORT = 8080


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("   cmd: " + self.command)
        print("   Path: " + self.path)
        if self.requestline.startswith("GET / ") or self.requestline.startswith("GET /index"):
            f = open('index.html', 'r')
            content = f.read()
            f.close()
        elif self.requestline.startswith("GET /blue"):
            f = open('blue.html', 'r')
            content = f.read()
            f.close()
        elif self.requestline.startswith("GET /pink"):
            f = open('pink.html', 'r')
            content = f.read()
            f.close()
        else:
            f = open('error.html', 'r')
            content = f.read()
            f.close()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-lenght', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("192.168.1.48", PORT), Handler) as httpd:
    print("Serving at port", PORT)

    httpd.serve_forever()