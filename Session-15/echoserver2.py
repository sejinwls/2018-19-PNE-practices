import http.server
import socketserver
import termcolor

PORT = 8081


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- printing th request line
        termcolor.cprint(self.requestline, 'green')
        inputs = self.requestline[14:].split(" ")
        msg = inputs[0]

        if not("msg" in self.requestline):
            f = open('2echoform.html', 'r')
            contents = f.read()

            self.send_response(200)

            self.send_header('Content-Type', 'text.html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()

            # --Sending he body of the response message
            self.wfile.write(str.encode(contents))
        elif "msg" in self.requestline:
            if msg != "":
                if "&" in msg:
                    msg = msg[0:msg.find("&")]
                    msg = msg.upper()
                f = open('echoform2.html', 'r')
                contents = f.read()
                contents = contents.replace('%message%',msg)
                contents = contents.replace('+', ' ')
                self.send_response(200)

                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(str.encode(contents)))
                self.end_headers()

                # --Sending he body of the response message
                self.wfile.write(str.encode(contents))
# Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}". format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
