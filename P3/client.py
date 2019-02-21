import socket

IP = "192.168.1.48"
PORT = 8081

msg = "\ncomplement\npercG"

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode(msg))

# Receive the servers respoinse
msg = s.recv(2048).decode("utf-8")
print("Message from server: ")
# Print the server's response
print(msg)

s.close()
