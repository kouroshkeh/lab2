import socket
import threading

BYTES_TO_READ = 4096
PROXY_SERVER_HOST = "127.0.0.1"
PROXY_SERVER_PORT = 8080

def send_request_to_destination(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as destination_socket:
        destination_socket.connect((host, port))
        destination_socket.sendall(request)
        destination_socket.shutdown(socket.SHUT_WR)

        response_data = b""
        while True:
            chunk = destination_socket.recv(BYTES_TO_READ)
            if not chunk:
                break
            response_data += chunk

        return response_data

def handle_client(client_socket):
    request_data = b""
    while True:
        data_chunk = client_socket.recv(BYTES_TO_READ)
        if not data_chunk:
            break
        request_data += data_chunk

    response_data = send_request_to_destination("www.google.com", 80, request_data)
    client_socket.sendall(response_data)
    client_socket.close()

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(5)
        print(f"Proxy server listening on {PROXY_SERVER_HOST}:{PROXY_SERVER_PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

if __name__ == "__main__":
    start_threaded_server()