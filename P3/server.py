import socket
from seq import Seq

IP = "192.168.1.48"
PORT = 8081
MAX_OPEN_REQUEST = 5


# First function detects if the first line is empty and if the sequence is correct
def first_process_seq(client_list):
    if client_list[0] == "":
        return_message = "ALIVE"
    else:
        valid_letters = ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']
        valid = True
        for letter in client_list[0]:
            if letter not in valid_letters:
                valid = False
        if valid:
            return_message = "OK"
        else:
            return_message = "ERROR"
    return return_message


def function_process_seq(client_list):
    return_msg = ""
    # list with possible operations requested
    possible_op = ['len', 'complement', 'reverse', 'countA', 'countC',
                   'countG', 'countT', 'percA', 'percC', 'percG', 'percT']
    # Check if the sequence is on the first or second place
    if client_list[0] == "":
        sequence = Seq(client_list[1])
        # List with all the operations required
        operations = client_list[2:]
    else:
        sequence = Seq(client_list[0])
        operations = client_list[1:]
    for op in operations:
        if op not in possible_op:
            return_msg = return_msg + "ERROR" + "\n"
        elif op == 'len':
            return_msg = return_msg + sequence.len() + "\n"
        elif op == 'complement':
            return_msg = return_msg + sequence.complement() + "\n"
        elif op == 'reverse':
            return_msg = return_msg + sequence.reverse() + "\n"
        elif 'count' in op:
            return_msg = return_msg + str(sequence.count(op[-1])) + "\n"
        elif 'perc' in op:
            return_msg = return_msg + str(sequence.perc(op[-1])) + "\n"
    return return_msg


# Creating socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, PORT))

while True:
    serversocket.listen(MAX_OPEN_REQUEST)
    print("Waiting for connections at {}, {}".format(IP, PORT))
    (clientsocket, adress) = serversocket.accept()
    print("Message received from {}".format(adress))

    # Receiving the message and creating a list
    msg = clientsocket.recv(2048).decode("utf-8")
    info = msg.split("\n")

    # Generating the response
    message = first_process_seq(info)
    # If the sequence is not valid we don't carry out the functions. I t would raise an error
    if message == "ERROR":
        final_message = "ERROR"
    else:
        secondmessage = function_process_seq(info)
        final_message = message + "\n" + secondmessage

    # Sending the response
    send_bytes = str.encode(final_message)
    clientsocket.send(send_bytes)
