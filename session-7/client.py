# A socket is an object to communicate
# Programming our first client
import socket
# Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
PORT = 8080
IP = "212.128.253.64"
s.connect((IP, PORT))
s.send(str.encode('Hello'))
msg = s.recv(2048).decode('utf-8')
print('Message from the server')
print(msg)
s.close()
print('The end')

