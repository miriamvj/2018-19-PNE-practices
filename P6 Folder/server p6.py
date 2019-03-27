import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8009


def correct(seq):
    ok = 'ACTG'
    for letter in seq:
        if letter not in ok:
            return False
    return True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print(' Cmd: ' + self.command)
        print(' Path: ' + self.path)

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            f = open("form Server p6.html")
            content = f.read()
            f.close()
        elif "msg" in self.path:
            msg_sent = self.path.split("&")
            print(msg_sent)
            seq = msg_sent[0][msg_sent[0].find("=") + 1:]
            seq = seq.upper()
            print(seq)
            if correct(seq):
                content = ("""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>SEQUENCE RESPONSE:</title>
                            </head>
                            <body style="background-color: light-green;">
                                <h1>Sequence information:</h1>
                                <p>{}</p>
                                <br>
                                <p>{}</p>
                                <br>
                                <p>{}</p>
                                <br>
                                <a href="/">Main page</a>
                            </body>
                            </html.>""")

                s = ""
                l = ""
                mode = ""

                s += 'Sequence:' + seq

                seq = Seq(seq)
                print(seq)

                print(s)

                for i in range(len(msg_sent)):
                    if "chk=on" in msg_sent[i]:
                        total = seq.len()
                        l += "Len:" + str(total)
                        print(l)
                    elif "base" in msg_sent[i]:
                        base = msg_sent[i].split("=")
                        b = base[1]
                    elif "operation" in msg_sent[i]:
                        oper = msg_sent[i].split("=")
                        if oper[1] == "count":
                            base = msg_sent[i].split("=")
                            b = base[1]
                            counter = seq.count()
                            mode += "Base {} appears {} times in the sequence".format(b, str(counter))
                            print(mode)
                        elif oper[1] == "perc":
                            base = msg_sent[i].split("=")
                            b = base[1]
                            perc = seq.percentage()
                            mode += "The percentage for base {} is: {}".format(b, str(perc))
                            print(mode)

                content = content.format(s, l, mode)

            else:
                f = open("error.html")
                content = f.read()
                f.close()
        else:
            f = open("error.html")
            content = f.read()
            f.close()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(content))


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()