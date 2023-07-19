#encoding: iso-8859-1
import subprocess, os, sys

'''
ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.1 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa1lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa1lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.2 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa2lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa2lj50")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.3 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa3lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa3lj50")


ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.4 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa4lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa4lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.5 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa5lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa5lj50")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.6 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa6lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa6lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.7 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa7lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa7lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.8 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa8lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa8lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.9 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa9lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa9lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.10 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa10lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa10lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.11 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa11lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa11lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.12 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa12lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa12lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.13 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa13lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa13lj50")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.14 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa14lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa14lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.15 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa15lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa15lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.16 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa16lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa16lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.17 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa17lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa17lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.18 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa18lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa18lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.19 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa19lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa19lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.20 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa20lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa20lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.21 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa21lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa21lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.22 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa22lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa22lj50")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.23 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa23lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa23lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.24 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa24lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa24lj50")
'''
ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.25 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa25lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa25lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.26 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa26lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa26lj50")

ret = subprocess.call("psexec.exe -d -i -u Caixa01Lj50 -p pdv \\\\192.168.50.27 ""c:\\pdv\\renomeia.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa27lj50.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Clisitef atualizado Caixa27lj50")


input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")


