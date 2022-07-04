import socket
import threading

HEADER = 64
PORT = 3000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT = '@DISCONNECT'

print(ADDR)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'NEW CONNECTION: {addr} connected.')

    connecting = True
    while connecting:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT:
                connecting = False

            print(f'[{addr}] {msg}')
            conn.send('Msg received'.encode(FORMAT))

    conn.close()
    t = threading.active_count()
    print(f'Active Connections: {t-2}')


def start():
    server.listen()
    print(f'LISTENING: Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'Active Connections: {threading.active_count()-1}')

print('Server is starting...')
start()
 
