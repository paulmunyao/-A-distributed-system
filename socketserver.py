import socket
import threading
import queue


class Server:
    def __init__(self, max_clients, host, port):
        self.max_clients = max_clients
        self.host = host
        self.port = port
        self.queue = queue.Queue()
        self.clients = []
        self.highest_rank = -1

#start server
def server_connect(self):
    self.host = socket.gethostname()
    self.port = 2700

    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.bind((self.host, self.port))

    # Configuring the server to hold a maximum number of clients
    self.server_socket.listen(100)
    conn, address = self.server_socket.accept()
    print("Connection from:" + str(address))

    while True:
        client_socket, address = self.socket.accept()
        data = conn.recv(2700).decode()
        threading.Thread(target=server_connect, args=(client_socket,)).start()
        if not data:
            break
        print("Received from clientserver: " + str(data))
        data = input('Input message:')
        conn.send(data.encode())

    conn.close()

#new client connection and assigning of rank in the server
def new_client(self, client_socket):
    rank = self.get_new_rank()
    client = (rank, client_socket)
    self.clients.appends(client)
    print("New client commected with rank {rank}")
    threading.Thread(target=self.handle_commands, args=(client,)).start()

#handling commands from a client
def handle_commands(self, client):
    rank,client_socket = client
    while True:
        data = client_socket.recv(2700).decode()
        if not data:
            self.handle_disconnect(client)
            break
        command = (rank,data)
        self.queue.put(command)
        self.notify_clients()


if __name__ == '__main__':
    server_connect()
