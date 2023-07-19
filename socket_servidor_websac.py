import socket
import traceback
import os
import time

s = socket.socket()
s.bind(("",9005))
s.listen(1)

while True:
    client,address = s.accept()
    print(f"{address} connected")

    # client socket and makefile wrapper will be closed when with exits.
    with client,client.makefile("rb") as clientfile:
        while True:
            folder = clientfile.readline()
            if not folder: # When client closes connection folder == b""
                break
            folder = folder.strip().decode()
            no_files = int(clientfile.readline())
            localtime = time.asctime( time.localtime(time.time()) )
            print(f"Receiving folder: {folder} ({no_files} files)", localtime)
            folderpath = os.path.join("REMARCA",folder)  # put in different directory in case server/client on same system
            os.makedirs(folderpath,exist_ok=True)
            for i in range(no_files):
                filename = clientfile.readline().strip().decode()
                filesize = int(clientfile.readline())
                data = clientfile.read(filesize)
                print(f"Receiving file: {filename} ({filesize} bytes)")
                with open(os.path.join(folderpath,filename),"wb") as f:
                    f.write(data)
