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

# start server


def server_connect(self):
    # self.host = socket.gethostname()
    # self.port = 2700

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

# new client connection and assigning of rank in the server


def new_client(self, client_socket):
    rank = self.get_new_rank()
    client = (rank, client_socket)
    self.clients.appends(client)
    print("New client commected with rank {rank}")
    threading.Thread(target=self.handle_commands, args=(client,)).start()

# handling commands from a client


def handle_commands(self, client):
    rank, client_socket = client
    while True:
        data = client_socket.recv(2700).decode()
        if not data:
            self.client_disconnect(client)
            break
        command = (rank, data)
        self.queue.put(command)
        self.notify_clients()


def execute_command(self):
    command = self.queue.get()
    rank, data = command
    client = next((c for c in self.clients if c[0] == rank), None)
    if client:
        client_socket = client[1]
        client_socket.send("Command executed successfully".encode())
        self.notify_client()
    else:
        self.execute_command()


def client_disconnect(self, client):
    rank, client_socket = client
    client_socket.close()
    self.clients.remove(client)
    print("Client number {rank} disconnected")
    self.adjust_ranks()


def adjust_ranks(self):
    for i, client in enumerate(self.clients):
        rank = client[0]
        if rank != i:
            self.clients[i] = (i, client[1])


def new_rank_client(self):
    self.highest_rank = +1
    return self.highest_rank


def notify_clients(self):
    for n in self.clients:
        rank, client_socket = n
        client_socket.send("New command is available".encode())


server = Server(max_clients=100, host=socket.gethostname, port=2700)
server.start()

if __name__ == '__main__':
    server_connect()
