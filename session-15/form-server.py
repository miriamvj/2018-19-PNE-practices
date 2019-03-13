import http.server
import socketserver
import termcolor

PORT = 8001


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # ----PRINTING THE REQUEST LINE
        termcolor.cprint(self.requestline, 'green')

        f = open('form2.html', 'r')
        contents = f.read()

        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.send_header('Content-length', len(str.encode(contents)))
        self.end_headers()

        # ----SENDING THE BODY OF THE RESPONSE MESSAGE
        self.wfile.write(str.encode(contents))


# -----MAIN PROGRAM

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print('Serving at PORT:{}'.format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print('The server is stopped')
