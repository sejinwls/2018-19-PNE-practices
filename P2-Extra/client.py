import socket
# Server that sends a sequence to the server
# Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 8080
IP = "212.128.253.73"

# Connect to the server
s.connect((IP, PORT))

# Send a message
message = input("Please introduce a sequence: ")
s.send(str.encode(message))

msg = s.recv(2048).decode("utf-8")
print("Mesaage from server: ")
print(msg)

s.close()
