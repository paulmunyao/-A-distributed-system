import socket


class Client:
    def __init__(self, host, port, rank):
        self.host = host
        self.port = port
        self.rank = rank
        self.socket = None


def client_connect(self):
    # host = socket.gethostname()
    # port = 2700

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((self.host, self.port))
    print("Client connected {self.host}:{self.port}")


def send_command(self, command):
    if command["rank"] < self.rank:
        self.socket.sendall(str.encode(command["Message"]))


def receive_command(self, command):
    while True:
        data = self.socket.recv(2700)
        if not data:
            break
        message = data.decode()
        print("Received command from socketserver: " + message)


def disconnect(self):
    self.socket.close()
    print("Disconnected from socketserver")


if __name__ == "__main__":
    client = Client("gethostname", 2700, 1)
    client_connect()
    client.send_command({'rank': 0, 'message': 'Hello'})
    client.receive_commands()
    client.disconnect()
