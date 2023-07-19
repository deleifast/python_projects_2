import socket, pickle, os

#f = input('escreva o nome do ficheiro')
source = os.listdir("C:\\PDV")
for f in source:
    if f.startswith("000501586.txt"):
        f_bin = open(f, 'rb').read()
        info = {'name': f, 'file': f_bin, 'opcao': 1} 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.0.16', 9005))
    s.sendall(pickle.dumps(info))
