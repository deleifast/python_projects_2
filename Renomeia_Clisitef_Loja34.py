#encoding: iso-8859-1
import subprocess, os, sys


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.34.1 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa1lj34.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa1lj34")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.34.2 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa2lj34.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa2lj34")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.34.3 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa3lj34.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa3lj34")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.34.4 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa4lj34.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa4lj34")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.34.5 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa5lj34.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa5lj34")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.34.6 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa6lj34.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa6lj34")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.34.7 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa7lj34.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa7lj34")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.34.8 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa8lj34.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa8lj34")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.34.9 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa9lj34.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa9lj34")


input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")


