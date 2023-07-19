import socket, pickle, os, glob, time,threading

from threading import Timer

def executar():
		
	os.chdir('c:\\envio')

	for file in glob.glob('RV*.???'):
		localtime = time.asctime( time.localtime(time.time()) )
		print(file, " - ", localtime)
		
		arquivo = open(file, 'rb').read()
		envio = {'name': file, 'file': arquivo} 


		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(('144.22.237.112', 9005))
			s.sendall(pickle.dumps(envio))
		
		except socket.error as err:
			print ("Sem conexão com o Servidor") 

while True:	
	t = Timer(60.0, executar)
	t.start()
