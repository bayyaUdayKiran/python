# A Simple UDP Client...
import socket

target_host = "127.0.0.1"
target_port = 9997

# create a socket object...
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data to the host..
# UDP is a connectionless protocol, there is no call to 'connect()' beforehand.
client.sendto(b"UdayKiranBayya", (target_host, target_port))

# receive some data..
data, addr = client.recvfrom(4096)
print(data.decode())

client.close()