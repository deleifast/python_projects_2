import socket
import threading
import tkinter as tk
import pickle
import time
from tkinter.scrolledtext import ScrolledText

import  gerarel

def run(conn):
    info_bin = b''
    st = time.time()

    while True:
        c = conn.recv(2048)
        if not c:
            break
        info_bin += c
        if time.time() - st >= 2: 
            logbox.insert('bytes downloaded:', len(info_bin))
            st = time.time()
    info = pickle.loads(info_bin)
    if info['file']:
        dest = 'c:/remarca/lojas/{}'.format(info['name'])
        with open(dest, 'wb') as f:
            f.write(info['file'])
            localtime = time.strftime("%d/%m/%Y - %H:%M:%S")
            #localtime = time.asctime( time.localtime(time.time())
        logbox.insert("end", 'Arquivo copiado - {} : {}'.format(dest, conn.getpeername()) + ' - ' + localtime + "\n")
        logbox.see(tk.END)
        conn.close()
        gerarel.consolidar()

def server():
    host = ''
    port = 9005
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    while True:
        try:
            conn, addr = server.accept()
            #logbox.insert("end", f"connected with {addr}\n")
            thread = threading.Thread(target=run, args=(conn,), daemon=True)
            thread.start()
        except Exception as ex:
            logbox.insert("end", "Server exception:", ex)
            break

    server.close()

root = tk.Tk()
root.title("Servidor_Socket")
root.geometry("680x300")
root.resizable(0,0)

logbox = ScrolledText(root, width=800, height=18, border=6, font=("Helvetica", 10), background = "gray", foreground = "white")
logbox.see(tk.END)
logbox.pack()

threading.Thread(target=server, daemon=True).start()

root.mainloop()    
