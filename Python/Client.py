import socket
import logging
import pickle

host = ""
port = 10314

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
logging.info("Connecting to service: {} on port (${})".format(host, port))

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


def add(lhs, rhs):
    add_object = addition()
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
    return -1

def echo(msg):
    echo_object = repeater()
    echo_object.msg = msg

    echo_pickle = pickle.dumps(echo_object)

    s.send(echo_pickle)
    print("Sending echo pickle to server")

    data = s.recv(1024)
    print("Receiving echo pickle from server")

    data_unpickled = pickle.loads(data)
    return data_unpickled.response


# --------------------------------------------
# The following exercises the remote calls
# and should not need modification

print("Starting Client...")
if (add(2, 4) == 6):
    print(".")
else:
    print("X")

#try:
#    divide(1, 0)
#    print("X")
#except Exception:
#    print(".")

if echo("Hello") == "You said Hello!":
    print(".")
else:
    print("X")

print(" Finished")
