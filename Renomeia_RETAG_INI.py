#encoding: iso-8859-1
import subprocess, os, sys


ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.1.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag1.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag1")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.2.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag2.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag2")


ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.3.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag3.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag3")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.4.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag4.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag4")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.6.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag6.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag6")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.7.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag7.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag7")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.8.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag8.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag8")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.9.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag9.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag9")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.10.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag10.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag10")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.11.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag11.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag11")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.12.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag12.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag12")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.13.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag13.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag13")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.141.150 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag14.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag14")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.15.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag15.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag15")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.16.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag16.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag16")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.17.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag17.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag17")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.18.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag18.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag18")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.19.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag19.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag19")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.20.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag20.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag20")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.21.100 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag21.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag21")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.22.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag22.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag22")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.23.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag23.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag23")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.24.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag24.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag24")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.25.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag25.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag25")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.26.150 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag26.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag26")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.27.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag27.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag27")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.28.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag28.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag28")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.29.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag29.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag29")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.30.102 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag30.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag30")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.31.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag31.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag31")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.32.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag32.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag32")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.33.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag33.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag33")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.34.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag34.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag34")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.35.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag35.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag35")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.36.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag36.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag36")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.37.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag37.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag37")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.38.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag38.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag38")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.39.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag39.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag39")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.40.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag40.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag40")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.41.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag41.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag41")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.42.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag42.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag42")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.43.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag43.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag43")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.44.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag44.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag44")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.45.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag45.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag45")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.46.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag46.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag46")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.47.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag47.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag47")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.48.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag48.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag48")

ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\10.132.49.101 ""c:\\retag\\ini.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Retag49.txt', 'a') as caixa:
		caixa.write('Arquivo não atualizado\n')
		caixa.close()
else:
	print("Retag atualizado Retag49")


input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")


