import sys
import socket

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
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_socket.bind((host, port))
    tcp_socket.listen()

    while True:
        client_connection, client_address = tcp_socket.accept()
        
        request = client_connection.recv(1024)
    pass

if __name__ == '__main__':
    sys.exit(main())
