import http.server
import socketserver

PORT = 8004

# Request line rpints the first line

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('GET received')

        print('Request line:' + self.requestline)
        print(' Cmd:' + self.command)
        print(' Path:' + self.path)

        if self.path == '/':
            with open('index.html', 'r') as f:
                contents = f.read()
        else:
            with open ('error.html', 'r') as f:
                contents = f.read()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content.Length', len(str.encode(contents)))
        self.end_headers()

        self.wfile.write(str.encode(contents))
        return



Handler = TestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('Serving at PORT', PORT)
    httpd.serve_forever()
