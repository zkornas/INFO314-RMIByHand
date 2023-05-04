import socket
import logging
import pickle

host = ""
port = 10314

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host, port))
#logging.info("Connecting to service: {} on port (${})".format(host, port))

class my_request:
    ID = ""
    lhs = ""
    rhs = ""
    ans = ""
    msg = ""
    response = ""

def add(lhs, rhs):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    add_object = my_request()
    add_object.ID = "add"
    add_object.lhs = lhs
    add_object.rhs = rhs

    add_pickle = pickle.dumps(add_object)

    s.send(add_pickle)
    logging.info("Sending pickle to server")

    data = s.recv(1024)
    logging.info("Receiving data from server")

    data_unpickled = pickle.loads(data)
    return data_unpickled.ans

def divide(lhs, rhs):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    divide_object = my_request()
    divide_object.ID = "divide"
    divide_object.lhs = lhs
    divide_object.rhs = rhs

    divide_pickle = pickle.dumps(divide_object)

    s.send(divide_pickle)
    logging.info("Sending pickle to server")

    data = s.recv(1024)
    logging.info("Receiving data from server")

    data_unpickle = pickle.loads(data)
    return data_unpickle.ans

def echo(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    echo_object = my_request()
    echo_object.ID = "echo"
    echo_object.msg = msg

    echo_pickle = pickle.dumps(echo_object)

    s.send(echo_pickle)
    #print("Sending echo pickle to server")

    data = s.recv(1024)
    #print("Receiving echo pickle from server")

    data_unpickled = pickle.loads(data)
    print(data_unpickled.response)
    return data_unpickled.response


# --------------------------------------------
# The following exercises the remote calls
# and should not need modification

print("Starting Client...")
if (add(2, 4) == 6):
    print(".")
else:
    print("X")

try:
    divide(1, 0)
    print("X")
except Exception:
    print(".")

if echo("Hello") == "You said Hello!":
    print(".")
else:
    print("X")

print(" Finished")
