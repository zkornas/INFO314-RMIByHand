import sys
import socket
import pickle

class addition:
    ID = "add"
    lhs = 0
    rhs = 0
    ans = 0

class division:
    ID = "divide"
    lhs = 0
    rhs = 0
    ans = 0

class repeater:
    ID = "echo"
    msg = ""
    response = ""

# Do not modify the add() function
def add(lhs, rhs):
    return lhs + rhs

# Do not modify the divide() function
def divide(lhs, rhs):
    if rhs == 0:
        raise Exception()
    return lhs / rhs

# Do not modify the echo() function
def echo(msg):
    return "You said '" + str(msg) + "'!'"

# Begin your server implementation here
def main():
    # Put your code here
    host = ""
    port = 10314

    # Open Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen()

    print("listening")

    while True:
        client_connection, client_address = s.accept()

        data = client_connection.recv(1024)
        data_unpickled = pickle.loads(data)
        print("Getting pickle!")

        if data_unpickled.ID == "add":
            print("We have addition!")
            data_unpickled.ans = add(data_unpickled.lhs, data_unpickled.rhs)
            data_pickle = pickle.dumps(data_unpickled)
            client_connection.send(data_pickle)
        #elif data_unpickled.ID == "divide":
        #    data_unpickled.ans = divide(data_unpickled.lhs, data_unpickled.rhs)
        #    data_pickle = pickle.dumps(data_unpickled)
        #    client_connection.send(data_pickle)
        elif data_unpickled.ID == "echo":
            print("We have an echo!")
            data_unpickled.response == echo(data_unpickled.msg)
            data_pickle = pickle.dumps(data_unpickled)
            client_connection.send(data_pickle)
            print("sending back pickled echo")

        client_connection.close()
    pass

if __name__ == '__main__':
    sys.exit(main())
