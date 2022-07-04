import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT = '@DISCONNECT'
SERVER = 'enter with server ip'
ADDR = (SERVER, PORT)

print(ADDR)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(200).decode(FORMAT))

while True:
    d = input()
    send(d)
    if d == '@out':
        break
    
send(DISCONNECT)
