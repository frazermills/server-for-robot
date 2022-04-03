import socket

IP = "whatever the reciever's ip is"
port = 5005

data = "this is a test"

print("target ip", IP)

print("target port:", port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(data, (IP, port))

