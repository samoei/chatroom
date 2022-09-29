import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established")
    client_socket.send(bytes(f"Hey there visitor from {address}, Are you human, or a robot like me?", "utf-8"))
    client_socket.close()