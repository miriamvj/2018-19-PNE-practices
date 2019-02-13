#My exercise from practice 2 where this is the server
import socket

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    PORT = 8085
    IP = "212.128.253.80"
    s.connect((IP, PORT))
    s1 = input('Please, enter a sequence:')

    s.send(str.encode(s1))

    msg = s.recv(2048).decode('utf-8')
    print('Message from the server')
    print(msg)


    s.close()