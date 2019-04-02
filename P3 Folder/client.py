import socket

# SERVER IP, PORT
IP = "212.128.253.84"
PORT = 8003

msg = """aaccttggg\nlen\ncountA\ncountG\npercC"""
#msg = """hola\nlen\ncountA\ncountG\npercC"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(str.encode(msg))

# Receive the servers response and print it
response = s.recv(2048).decode()
print("Response: {}".format(response))
s.close()