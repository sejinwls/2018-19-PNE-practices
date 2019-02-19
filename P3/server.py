import socket
from seq import Seq

IP = "212.128.253.68"
PORT = 8081
MAX_OPEN_REQUEST = 5


def first_process_seq(client_list):
    return_message = ""
    if client_list[0] == "":
        return_message = return_message + "ALIVE"
    else:
        valid_letters = ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']
        valid = True
        for letter in client_list[0]:
            if letter not in valid_letters:
                valid = False
        if valid:
            return_message = return_message + "OK"
        else:
            return_message = return_message + "ERROR"
    return return_message


def function_process_seq(client_list):
    #Check if the sequence is on the first or second place
    if client_list[0] == "":
        sequence =


# Creating socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

(clientsocket, adress) = serversocket.accept()

msg = clientsocket.recv(2048).decode("utf-8")
info = msg.split("\n")
message = first_process_seq(info)
print(message)
