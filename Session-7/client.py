# Programming our first client

import socket

# Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 8080
IP = "212.128.253.108"

# Connect to the server
s.connect((IP, PORT))

# Send a message
s.send(str.encode("HELLO FROM MY CLIENT"))

msg = s.recv(2048).decode("utf-8")
print("Mesaage from server: ")
print(msg)

s.close()

print("The end")
