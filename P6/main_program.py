import http.server
import socketserver
import termcolor
from seq import Seq

PORT = 8081


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- printing th request line
        termcolor.cprint(self.requestline, 'green')

        if not("seq" in self.requestline):
            f = open('main_page.html', 'r')
            contents = f.read()

            self.send_response(200)

            self.send_header('Content-Type', 'text.html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()

            # --Sending he body of the response message
            self.wfile.write(str.encode(contents))
        elif "seq" in self.requestline:
            inputs = self.requestline[14:].split("&")
            seq = Seq(inputs[0])
            if seq != "":
                okay = True
                for a in seq.strbases:
                    valid = ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']
                    if a not in valid:
                        okay = False
                if not okay:
                    contents = 'The sequence introduced is not valid. Please try again'
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/plain')
                    self.send_header('Content-Length', len(str.encode(contents)))
                    self.end_headers()

                    # --Sending he body of the response message
                    self.wfile.write(str.encode(contents))

                elif okay:
                    f = open('response.html', 'r')
                    contents = f.read()
                    contents = contents.replace('+', ' ')
                    contents = contents.replace('@', seq.strbases)
                    if len(inputs) == 4:
                        operation = inputs[2][10:]
                        base = inputs[3].split(" ")[0][-1]
                        contents = contents.replace('%', str(seq.len()))
                    elif len(inputs) == 3:
                        contents = contents.replace('The lenght of your sequence is: %', '')
                        operation = inputs[1][10:]
                        base = inputs[2].split(" ")[0][-1]
                    if operation == "count":
                        contents = contents.replace('#', 'count')
                        contents = contents.replace('?', base)
                        contents = contents.replace('*', str(seq.count(base)))
                    elif operation == "perc":
                        contents = contents.replace('#', 'percentage')
                        contents = contents.replace('?', base)
                        contents = contents.replace("*", str(seq.perc(base)))

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
