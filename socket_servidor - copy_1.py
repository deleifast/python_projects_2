import socket, threading, pickle, time

def run(conn):
    info_bin = b''
    st = time.time()
    while True:
        c = conn.recv(2048)
        if not c:
            break
        info_bin += c
        if time.time() - st >= 2: # opcional, informacao sobre o total ja carregado
            print('bytes downloaded:', len(info_bin))
            st = time.time()
    info = pickle.loads(info_bin)
    if info['file']:
        dest = 'c:/remarca/lojas/{}'.format(info['name'])
        with open(dest, 'wb') as f:
            f.write(info['file'])
        print('Arquivo copiado {} : {}'.format(info['name'], conn.getpeername()))
        conn.close()

host, port = ('', 9005)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        print('Conectado', addr)
        threading.Thread(target=run, args=(conn,)).start()
