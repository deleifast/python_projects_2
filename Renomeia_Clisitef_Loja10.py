#encoding: iso-8859-1
import subprocess, os, sys


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.10.2 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa2lj10.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa2lj10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.10.3 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa3lj10.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa3lj10")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.10.4 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa4lj10.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa4lj10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.10.5 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa5lj10.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa5lj10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.10.6 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa6lj10.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa6lj10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.10.7 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa7lj10.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa7lj10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.10.8 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa8lj10.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa8lj10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.10.9 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa9lj10.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa9lj10")


input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")


