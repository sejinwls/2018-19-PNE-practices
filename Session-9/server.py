import socket
import termcolor

PORT = 8080
IP = "212.128.253.68"
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    if msg == "EXIT":
        exit()

    termcolor.cprint("Message from the client: {}".format(msg), 'magenta')

    # Sending the message back to the client
    cs.send(str.encode(msg))


# Create a socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:
    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, adress) = serversocket.accept()

    # -- Processing the clients request
    print("Attending client: {}".format(adress))

    process_client(clientsocket)

    # Close the socket
    clientsocket.close()
