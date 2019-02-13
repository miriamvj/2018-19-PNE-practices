# A socket is an object to communicate
# Programming our first client
import socket

# Create a socket for communicating with the server
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    PORT = 8083
    IP = "212.128.253.64"
    s.connect((IP, PORT))

    message = input('Please, enter a message:')
    s.send(str.encode(message))

    msg = s.recv(2048).decode('utf-8')
    print('Message from the server')
    print(msg)

    s.close()