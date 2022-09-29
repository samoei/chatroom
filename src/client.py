import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


while True:
    message = ''
    while True:
        b = s.recv(8)
        if len(b) <= 0:
            break
        message += b.decode("utf-8")
    if len(message) > 0:
        print(message)
