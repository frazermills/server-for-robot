import socket

IP = "sender's ip"

port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(IP, port)

while True:
    data, address = sock.recvfrom(2048) # sets buffer to 2048 bytes
    print(data, address)
