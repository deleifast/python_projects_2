#encoding: iso-8859-1
import subprocess, os, sys


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.1 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa1lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa1lj31")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.2 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa2lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa2lj31")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.3 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa3lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa3lj31")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.4 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa4lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa4lj31")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.5 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa5lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa5lj31")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.6 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa6lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa6lj31")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.7 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa7lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa7lj31")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.8 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa8lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa8lj31")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.9 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa9lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa9lj31")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.10 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa10lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa10lj31")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.11 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa11lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa11lj31")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.31.12 ""c:\\pdv\\renomeia_salcomm.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa12lj31.txt', 'a') as caixa:
		caixa.write('Salcomm não atualizado\n')
		caixa.close()
else:
	print("Salcomm atualizado Caixa12lj31")


input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")


