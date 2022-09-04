# A Simple Multi-Threaded TCP Server...

import socket
import threading



IP = '0.0.0.0'
PORT = 9998


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5) #server to start listening , with a maximum backlog of connections set to 5
    print(f'[*] Listening on {IP}:{PORT}')
    while True:
        client, addr = server.accept()
        print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        flag = client_handler.start()
        

    
def handle_client(client_sock):
    with client_sock as sock:
        req = sock.recv(1024)
        print(f'[*] Received: {req.decode("utf-8")}')
        sock.send(b"ACK")
        


if __name__ == "__main__":
    main()
