import http.server
import socketserver

PORT = 8080


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("   cmd: " + self.command)
        print("   Path: " + self.path)

        content = "I am the happy server"

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-lenght', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("212.128.253.68", PORT), Handler) as httpd:
    print("Serving at port", PORT)

    httpd.serve_forever()
