import socket

def server_connect():
    host = socket.gethostname()
    port = 2700

    server_socket = socket.socket()
    server_socket.bind((host,port))

    # Configuring the server to hold a maximum number of clients
    server_socket.listen(100)
    conn,address = server_socket.accept()
    print("Connection from:" + str(address))

    while True:
        data = conn.recv(2700).decode()
        if not data:
            break
        print("Received from client: " + str(data))
        data = input('Input message:')
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    server_connect()    