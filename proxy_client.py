import socket

BYTES_TO_READ = 4096
proxy_host = "localhost"
proxy_port = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((proxy_host, proxy_port))

request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
client_socket.sendall(request.encode())

response = b""
while True:
    data = client_socket.recv(BYTES_TO_READ)
    if not data:
        break
    response += data

print(response.decode())

client_socket.close()
