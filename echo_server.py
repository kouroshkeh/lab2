import socket
import threading

BYTES_TO_READ = 4096
HOST = "127.0.0.1" 
PORT = 8080
def handle_client(client_socket):
    while True:
        data = client_socket.recv(BYTES_TO_READ)
        if not data:
            break
        print(f"Received: {data.decode()}")
        client_socket.sendall(data)
        
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.listen(5)

    print(f"Listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()