#encoding: iso-8859-1
from datetime import datetime
import socket
import threading
import pickle

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


root = tk.Tk()
root.title("Servidor")

text = tk.Text(master=root)
text.pack(expand=True, fill="both")

entry = tk.Entry(master=root)
entry.pack(expand=True, fill="x")

frame = tk.Frame(master=root)
frame.pack()


def buttons():
    for i in "Connect", "Send", "Clear", "Exit":
        b = tk.Button(master=frame, text=i)
        b.pack(side="left")
        yield b


b1, b2, b3, b4, = buttons()


class Server:
    clients = []

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.s.bind(("", 9005))
        self.s.listen(10)
        now = str(datetime.now())[:-7]
        text.insert("insert", "({}) : Connected.\n".format(now))
        self.condition()

    def accept(self):
        c, addr = self.s.accept()
        self.clients.append(c)
        data = c.recv(2048)
        text.insert("insert", "({}) : {} connected.\n".format(str(datetime.now())[:-7], str(data)[1:]))

    def receive(self):
        for i in self.clients:

            def f():
                data = str(i.recv(1024))[2:-1]
                now = str(datetime.now())[:-7]
                if len(data) == 0:
                    pass
                else:
                    text.insert("insert", "({}) : {}\n".format(now, data))

            t1_2_1 = threading.Thread(target=f)
            t1_2_1.start()

    def condition(self):
        while True:
            t1_1 = threading.Thread(target=self.accept)
            t1_1.daemon = True
            t1_1.start()
            t1_1.join(1)
            t1_2 = threading.Thread(target=self.receive)
            t1_2.daemon = True
            t1_2.start()
            t1_2.join(1)

    def send(self):
        respond = "Server: {}".format(str(entry.get()))
        now = str(datetime.now())[:-7]
        entry.delete("0", "end")
        try:
            for i in self.clients:
                i.sendall(bytes(respond.encode("utf-8")))
            text.insert("insert", "({}) : {}\n".format(now, respond))
        except BrokenPipeError:
            text.insert("insert", "({}) : Client has been disconnected.\n".format(now))


s1 = Server()


def connect():
    t1 = threading.Thread(target=s1.connect)
    t1.start()


def send():
    t2 = threading.Thread(target=s1.send)
    t2.start()


def run():
    info_bin = b''
    info = pickle.loads(info_bin)
    if info['file']:
        dest = 'c:/remarca/lojas/{}'.format(info['name'])
        with open(dest, 'wb') as f:
            f.write(info['file'])
        print('Arquivo copiado {} : {}'.format(info['name'], conn.getpeername()))
        
        

def destroy():
    root.destroy()
    exit()


if __name__ == "__main__":
    b1.configure(command=connect)
    b2.configure(command=send)
    b3.configure(command=run)
    b4.configure(command=destroy)
    t0 = threading.Thread(target=root.mainloop)
    t0.run()
