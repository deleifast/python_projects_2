import socket, pickle, os, configparser, shutil, re, glob, time, wmi, subprocess
import datetime as dt


c = wmi.WMI ()

total, used, free = shutil.disk_usage("/")

cpuArr = c.Win32_Processor()

config = configparser.ConfigParser(defaults=None, strict=False, allow_no_value=True)
config.optionxform = str

source = os.listdir('c:\\pdv')

ip = socket.gethostbyname_ex(socket.gethostname())[0]


config.read('PDVSAL.INI')

caixa = config.get('IMPRESSORA','CAIXA')
modelo = config.get('IMPRESSORA','MODELO')
sat = config.get('SAT','NSERIE')
loja = config.get('LOJA', 'NUMERO')

printer = ('lj') + str(loja) + ('.') + str(ip.lower()) + ('.txt')
with open(printer, "w") as stream:
	print("Sat:",caixa,"Impressora:",modelo, file=stream)
f_imp = open(printer, 'rb').read()
info6 = {'name': printer, 'file': f_imp}


with open('cpu.txt','w') as arquivo:
	
	for cpu in cpuArr :
		print(caixa, file=arquivo)	
		print('Cpu:', cpu.loadPercentage, cpu.numberOfCores, cpu.name, cpu.maxClockSpeed/1000, file=arquivo)
		print('Total Memória: {0}'.format(c.Win32_ComputerSystem()[0].TotalPhysicalMemory), file=arquivo)
		print("Total do disco: %d GB" % (total // (2**30)), "Usado: %d GB" % (used // (2**30)), "Livre: %d GB" % (free // (2**30)), file=arquivo)

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	dns_google = socket.gethostbyname('dns.google')
except socket.gaierror:
	print("Sem internet....")

	
with open("ip.txt", "w") as f:
	print(s.getsockname()[0], file=f)

with open('ip.txt') as f, open('dns.txt', 'w') as out:
    for line in map(str.rstrip, f):
        if line:  # skips empty lines
            try:
                subprocess.check_call(["nslookup", line],
                                         stdout=out)
            except subprocess.CalledProcessError:
                pass

if os.path.exists ('sat.txt'):
	shutil.copy2('sat.txt',('lj') + loja + ('.') + ('sat_') + caixa + ('.txt'))
else:
	with open(('lj') + loja + ('.') + ('sat_') + caixa + ('.txt'), "w") as stream:
		print('SEM ARQUIVO - SAT.TXT NA PASTA PDV, VERIFICAR!', file=stream)

if os.path.exists('key.txt'):
	shutil.copy2('key.txt',('lj') + loja + ('.') + ('key_') + caixa + ('.txt'))
else:
	with open(('lj') + loja + ('.') + ('key_') + caixa + ('.txt'), "w") as stream:
		print('KEY.TXT NÃO EXISTE, VERIFICAR!', file=stream)

if os.path.exists ('cpu.txt'):
	shutil.copy2('cpu.txt',('lj') + loja + ('.') + ('cpu_') + caixa + ('.txt'))
else:
	with open(('lj') + loja + ('.') + ('cpu_') + caixa + ('.txt'), "w") as stream:
		print('ERRO AO CRIAR O ARQUIVO, VERIFICAR!', file=stream)

if os.path.exists ('ip.txt'):
	shutil.copy2('ip.txt',('lj') + loja + ('.') + ('ip_') + caixa + ('.txt'))
else:
	with open(('lj') + loja + ('.') + ('ip_') + caixa + ('.txt'), "w") as stream:
		print('IP.TXT NÃO EXISTE, VERIFICAR!', file=stream)

if os.path.exists ('dns.txt'):
	shutil.copy2('dns.txt',('lj') + loja + ('.') + ('dns_') + caixa + ('.txt'))
else:
	with open(('lj') + loja + ('.') + ('cpu_') + caixa + ('.txt'), "w") as stream:
		print('DNS.TXT NÃO EXISTE, VERIFICAR!', file=stream)

path = "c:\\pdv"

files = glob.glob(os.path.join(path,'clisitef32i.dll'))
files.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files1 = glob.glob(os.path.join(path,'logsat.exe'))
files1.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files2 = glob.glob(os.path.join(path,'nfce.dll'))
files2.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files3 = glob.glob(os.path.join(path,'nfe2ws4.exe'))
files3.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files4 = glob.glob(os.path.join(path,'pdvsal.exe'))
files4.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files5 = glob.glob(os.path.join(path,'qrencode32.dll'))
files5.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files6 = glob.glob(os.path.join(path,'satsal.dll'))
files6.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])


with open('versao_pdv.txt',"w") as stream:
	for file in files:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(caixa,file=stream)
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)

with open('versao_pdv.txt',"a") as stream:
	for file in files1:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)

with open('versao_pdv.txt',"a") as stream:
	for file in files2:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)

with open('versao_pdv.txt',"a") as stream:
	for file in files3:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)

with open('versao_pdv.txt',"a") as stream:
	for file in files4:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)

with open('versao_pdv.txt',"a") as stream:
	for file in files5:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)

with open('versao_pdv.txt',"a") as stream:
	for file in files6:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)


path = 'c:\\pdv\\plugin'

files8 = glob.glob(os.path.join(path, 'clitef.dll'))
files8.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

with open('versao_pdv.txt',"a") as stream:
	for file in files8:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)
		
		
files9 = glob.glob(os.path.join(path,'apromos.dll'))
files9.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

with open('versao_pdv.txt',"a") as stream:
	for file in files9:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)


if os.path.exists ('versao_pdv.txt'):
	shutil.copy2('versao_pdv.txt',('lj') + loja + ('.') + ('verpdv_') + caixa + ('.txt'))
else:
	with open(('lj') + loja + ('.') + caixa + ('.txt'), "w") as stream:
		print('ERRO AO CRIAR O ARQUIVO, VERIFICAR!', file=stream)

f_bin = open(('lj') + (loja) + ('.') + ('sat_') + caixa + ('.txt'), 'rb').read()
info = {'name': ('lj') + (loja) + ('.') + ('sat_') + caixa + ('.txt'), 'file': f_bin} 

f_bin1 = open(('lj') + loja + ('.') + ('verpdv_') + caixa + ('.txt'), 'rb').read()
info1 = {'name': ('lj') + loja + ('.') + ('verpdv_') + caixa + ('.txt'), 'file': f_bin1} 

f_bin1 = open(('lj') + loja + ('.') + ('key_') + caixa + ('.txt'), 'rb').read()
info2 = {'name': ('lj') + loja + ('.') + ('key_') + caixa + ('.txt'), 'file': f_bin1} 

f_bin1 = open(('lj') + loja + ('.') + ('cpu_') + caixa + ('.txt'), 'rb').read()
info3 = {'name': ('lj') + loja + ('.') + ('cpu_') + caixa + ('.txt'), 'file': f_bin1} 

f_bin = open(('lj') + loja + ('.') + ('ip_') + caixa + ('.txt'), 'rb').read()
info4 = {'name': ('lj') + loja + ('.') + ('ip_') + caixa + ('.txt'), 'file': f_bin} 

f_bin = open(('lj') + loja + ('.') + ('dns_') + caixa + ('.txt'), 'rb').read()
info5 = {'name': ('lj') + loja + ('.') + ('dns_') + caixa + ('.txt'), 'file': f_bin} 


try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.20.15', 9005))
	s.sendall(pickle.dumps(info))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.20.15', 9005))
	s.sendall(pickle.dumps(info1))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.20.15', 9005))
	s.sendall(pickle.dumps(info2))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.20.15', 9005))
	s.sendall(pickle.dumps(info3))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.20.15', 9005))
	s.sendall(pickle.dumps(info4))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.20.15', 9005))
	s.sendall(pickle.dumps(info5))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.20.15', 9005))
	s.sendall(pickle.dumps(info6))

except socket.error as err:
	print ("Sem conexão com o Servidor") 
	
