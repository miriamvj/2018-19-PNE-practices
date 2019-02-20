import socket
import sys
# SERVER IP, PORT
PORT = 8082
IP = '212.128.253.75'

while True:

    # Before connecting to the server, ask the user for the string
    msg = input("> ")

    if msg != 'EXIT':
        # Now we can create the socket and connect to the servewr
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((IP, PORT))

        # Send the request message to the server
        s.send(str.encode(msg))

        # Receive the servers response
        response = s.recv(2048).decode()

        # Print the server's response
        print("Response: {}".format(response))

        s.close()
    else:
        sys.exit()
