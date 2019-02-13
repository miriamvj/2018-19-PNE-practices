#My exercise from practice 2 where this is the server
import socket

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    PORT = 8083
    IP = "212.128.253.80"
    s.connect((IP, PORT))

    s1 = input('Please, enter a sequence:')
    from Seq import Seq
    s1 = Seq(s1)
    s2 = Seq(s1.reverse())
    s3 = Seq(s2.complement())
    s.send(str.encode(s3.strbases))

    msg = s.recv(2048).decode('utf-8')
    print('Message from the server')
    print(msg)
    print(s1.strbases)
    print(s2.strbases)
    print(s3.strbases)

    s.close()