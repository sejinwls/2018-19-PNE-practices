from seq import Seq
import socket

s1 = Seq(input("Please introduce a sequence: "))
s2 = Seq(s1.reverse())
s3 = Seq(s1.complement())

print(s2.strbases)
print(s3.strbases)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8080
IP = "212.128.253.73"

# Connect to the server
s.connect((IP, PORT))

# Send a message
s.send(str.encode("Reverse:{}".format(s2.strbases)))
s.send(str.encode("\nComplement:{}".format(s3.strbases)))


msg = s.recv(2048).decode("utf-8")
print("Mesaage from server: ")
print(msg)

s.close()
