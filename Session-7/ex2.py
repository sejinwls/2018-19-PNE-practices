# Programming a first client

import socket

# Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8080
IP = "212.128.253.64"
# Connect to the server
s.connect((IP, PORT))
a = True
while a:
    message = input("Enter a message for the server")
    # Send a message
    s.send(str.encode(message))

    msg = s.recv(2048).decode("utf-8")
    print("Mesaage from server: ")
    print(msg)

    s.close()
    if message == "close":
        break

print("The end")
