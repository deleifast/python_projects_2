#encoding: iso-8859-1
import subprocess, os, sys


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.6.1 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa1lj06.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa1lj06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.6.2 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa2lj06.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa2lj06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.6.3 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa3lj06.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa3lj06")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.6.4 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa4lj06.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa4lj06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.6.5 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa5lj06.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa5lj06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.6.6 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa6lj06.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa6lj06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.6.7 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa7lj06.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa7lj06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.6.8 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa8lj06.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa8lj06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.6.9 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa9lj06.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa9lj06")


input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")


