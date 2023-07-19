#encoding: iso-8859-1
import os, shutil, subprocess, time, glob, copy, os.path, sys, socket
from zipfile import ZipFile

import tkinter as tk
from tkinter import *

gui = tk.Tk()

gui.geometry('400x50')
gui.title('Pdvcoral - Remarca')
gui.resizable(0,0)

msg = Label(gui, text='Manutenção no arquivos, aguarde...', fg="red", font='Arial 18')
msg.place(x=1, y=10)

time.sleep(30)
driveLetter = 'X:' 
networkPath = '\\\\10.0.20.42\Atual' 
user = 'compartilhar' 
password = 'ruaf305'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 0:
	print(winCMD)

else:
	exitcode == 2

	os.chdir('C:\\PDV')
	path = 'C:\\PDV'
	dir = os.listdir(path)
	for file in dir:
		if file == "pdv.txt":
			os.remove(file)

	hostName    = ""

	ipAddress   = socket.gethostbyname_ex(socket.gethostname())
	time.sleep(5)
	msg = Label(gui, text="Sem conexão com o Servidor, enviando e-mail....", fg="blue", font= 'Arial 18')
	msg.place(x=1, y=10)

	with open('pdv.txt', 'a') as caixa:
		caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
		caixa.close()

				
	os.startfile(r"c:\\pdv\pdvsal.exe")

	time.sleep(10)

	msg = Label(gui, text='Processos inicializados sem atualização!' + '\n' + 'Remarca verificar!', bg = "yellow", fg="red", font= 'Arial 18')
	msg.place(x=1, y=10)

	sys.exit()

		
	
msg = Label(gui, text='Copiando arquivos para o PDV, aguarde....', fg="blue", font= 'Arial 18')
msg.place(x=1, y=10)


PATHPDV='X://loja99_pdv.zip'
PATHPLUGIN='X://loja99_plugin.zip'

if os.path.isfile(PATHPDV):
	dest_dir = "C:\\PDV"
	for file in glob.glob(r'X:/loja99_pdv.zip'):
		print(file)
	shutil.copy(file, dest_dir)

else:
	time.sleep(5)
	msg = Label(gui, text="Sem arquivos(PDV) para atualizar no Servidor", fg="blue", font= 'Arial 18')
	msg.place(x=1, y=10)


if os.path.isfile(PATHPLUGIN):
	dest_dir = "C:\\PDV\PLUGIN"
	for file in glob.glob(r'X:/loja99_plugin.zip'):
		print(file)
	shutil.copy(file, dest_dir)

else:
	time.sleep(5)
	msg = Label(gui, text="Sem arquivos(PLUGIN) para atualizar no Servidor", fg="blue", font= 'Arial 18')
	msg.place(x=1, y=10)


winCMD = 'NET USE ' + driveLetter + ' /delete /y'
print(winCMD)
subprocess.call(winCMD, shell=True)

PATHPDV='C://PDV/loja99_pdv.zip'
PATHPLUGIN='C://PDV/PLUGIN/loja99_plugin.zip'

if os.path.isfile(PATHPDV):
	file_pdv = "c:\\pdv\loja99_pdv.zip"
	with ZipFile(file_pdv, 'r') as zip:
		zip.printdir()
		 
		time.sleep(5)
		msg = Label(gui, text="Extraindo todos os arquivos do pdv agora...", fg="blue", font= 'Arial 18')
		msg.place(x=1, y=10)

		zip.extractall('c:\\pdv')
		time.sleep(5)
		msg = Label(gui, text="Pdv OK!", fg="blue", font= 'Arial 18')
		msg.place(x=1, y=10)

else:
	time.sleep(5)
	msg = Label(gui, text="Sem arquivos(PDV) para descompactar", fg="blue", font= 'Arial 18')
	msg.place(x=1, y=10)

if os.path.isfile(PATHPLUGIN):
	file_plugin = "c:\\pdv\plugin\loja99_plugin.zip"
	with ZipFile(file_plugin, 'r') as zip:
		zip.printdir()
	
		time.sleep(5)
		msg = Label(gui, text="Extraindo todos os arquivos do plugin agora...", fg="blue", font= 'Arial 18')
		msg.place(x=1, y=10)

		zip.extractall('c:\\pdv\plugin')
		time.sleep(5)
		msg = Label(gui, text="Plugin OK!", fg="blue", font= 'Arial 18')
		msg.place(x=1, y=10)

else:
	time.sleep(5)
	msg = Label(gui, text="Sem arquivos(PLUGIN) para descompactar", fg="blue", font= 'Arial 18')
	msg.place(x=1, y=10)

os.chdir('C:\\PDV')

os.startfile(r"pdvsal.exe")
		
time.sleep(10)

msg = Label(gui, text='Processos inicializados com sucesso!', fg="blue", font= 'Arial 18')
msg.place(x=1, y=10)


def sair():
	gui.destroy()
	return

gui.after(10000, sair)


gui.mainloop()
