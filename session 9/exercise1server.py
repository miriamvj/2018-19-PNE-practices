import socket
import termcolor

PORT = 8082
IP = '212.128.253.75'
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # reading the message from the client
    msg = cs.recv(2048).decode('utf-8')

    termcolor.cprint('Message from the client:{}'.format(msg), 'green')
    # sending the message to the client (because we are an echo server)
    cs.send(str.encode(msg))
    cs.close()


# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print('Socket ready: {}'.format(serversocket))


while True:

    print('Waiting for connections at:{}, {}'.format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # ---- Process the client request
    print('Attending client: {}'.format(address))
    process_client(clientsocket)

    # ----Close the socket
    clientsocket.close()
