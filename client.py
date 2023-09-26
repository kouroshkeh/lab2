import socket

BYTES_TO_READ = 4096
host = "www.google.com"
port = 80 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
client_socket.sendall(request.encode())

response = client_socket.recv(BYTES_TO_READ)
while response:
    print(response.decode('ISO-8859-1'), end="")
    response = client_socket.recv(BYTES_TO_READ)

client_socket.close()