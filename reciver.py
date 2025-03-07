import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_add = "192.168.221.141"
port = 1234
complete = (ip_add, port)
s.bind(complete)
while True:
    mgs=s.recvfrom(1024)
    mgs=(mgs[0].decode('ascii'))
    print(mgs)