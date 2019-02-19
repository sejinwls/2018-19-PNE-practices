from seq import Seq
import socket

try:
    while True:
        s1 = Seq(input("Please introduce a sequence: "))
        s2 = Seq(s1.reverse())
        s3 = Seq(s2.complement())

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        PORT = 8080
        IP = "212.128.253.68"

        # Connect to the server
        s.connect((IP, PORT))

        # Send a message
        s.send(str.encode("Reverse/complement:{}".format(s3.strbases)))


        msg = s.recv(2048).decode("utf-8")
        print("Mesaage from server: ")
        print(msg)

        s.close()
except KeyboardInterrupt:
    print("Execution interrupted by user")