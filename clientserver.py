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

    message = input("Input message:")

    while message.lower().strip() != "message":
        client_socket.send(message.encode())
        data = client_socket.recv(2700).decode()

        print("Received message from socketserver: " + data)

        message = input("Do put message:")

    client_socket.close()


if __name__ == "__main__":
    client_connect()
