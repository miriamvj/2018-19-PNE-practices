#My exercise 3 done with esther computer
import socket

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    PORT = 8081
    IP = "212.128.253.81"
    s.connect((IP, PORT))

    message = input('Please, enter a message:')
    s.send(str.encode(message))

    msg = s.recv(2048).decode('utf-8')
    print('Message from the server')
    print(msg)

    s.close()