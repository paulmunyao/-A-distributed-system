import socket

def client_connect():
    host = socket.gethostname()
    port = 2700

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("Input message:")

    while message.lower().strip() != "message":
        client_socket.send(message.encode())
        data = client_connect.recv(2700).decode()

        print("Received message from socketserver: " + data)

        message = input("Do put message:")

    client_socket.close()

if __name__ == "__main__":
    client_connect()  

    

        
                                                                      

