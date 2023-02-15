import socket
# import threading
import queue


class server:
    def __init__(self, max_clients, host,port):
        self.max_clients = max_clients
        self.host = host
        self.port = port
        self.command_queue = queue.Queue(max_clients)
        self.clients = {}
        self.current_rank = 0


def server_connect(self):
    self.host = socket.gethostname()
    self.port = 2700

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((self.host, self.port))

    # Configuring the server to hold a maximum number of clients
    server_socket.listen()
    conn, address = server_socket.accept()
    print("Connection from:" + str(address))

    while True:
        data = conn.recv(2700).decode()
        if not data:
            break
        print("Received from clientserver: " + str(data))
        data = input('Input message:')
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    server_connect()
