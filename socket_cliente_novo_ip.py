#encoding: iso-8859-1

import socket, pickle, os, configparser, shutil, re, glob, wmi, logging, subprocess
import datetime as dt

data = dt.datetime.now()

logging.basicConfig(filename="socket.log", format="[v.1.0]:%(asctime)s %(message)s", datefmt='%d-%m-%y %H:%M:%S',
                    level=logging.INFO)

c = wmi.WMI ()

total, used, free = shutil.disk_usage("/")

try:
    cpuArr = c.Win32_Processor()
except AttributeError:
    cpuArr = 0
    
config = configparser.ConfigParser(defaults=None, strict=False, allow_no_value=True)
config.optionxform = str

source = os.listdir('c:\\pdv')

try:
    ip = socket.gethostbyname_ex(socket.gethostname())[0]
except socket.gaierror:
	ip = 'Sem Nome'

config.read('PDVSAL.INI')

caixa = config.get('IMPRESSORA','CAIXA')
modelo = config.get('IMPRESSORA','MODELO')
sat = config.get('SAT','NSERIE')
loja = config.get('LOJA', 'NUMERO')

printer = ('lj') + str(loja) + ('.') + ('imp_') + caixa + ('.txt')
with open(printer, "w") as stream:
	print(loja,caixa,modelo,data.strftime("%Y-%m-%d"), file=stream)
f_imp = open(printer, 'rb').read()
info6 = {'name': printer, 'file': f_imp}

with open('cpu.txt','w') as arquivo:
    
    try:
	    for cpu in cpuArr :
             print(loja,",",caixa,",",cpu.name,",",'{0}'.format(c.Win32_ComputerSystem()[0].TotalPhysicalMemory),",","%dGB" % (total // (2**30)),",","%dGB" % (used // (2**30)),",","%dGB" % (free // (2**30)), ",", data.strftime("%Y-%m-%d"), file=arquivo)	
    except:
        print('erro', file=arquivo)
try:    
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	dns_google = socket.gethostbyname('dns.google')
except socket.gaierror:
	print("Sem internet....")

	
with open("ip.txt", "w") as f:
	print(loja,caixa,ip, s.getsockname()[0], data.strftime("%Y-%m-%d"), file=f)

with open('ip.txt') as f, open('dns.txt', 'w') as out:
    for line in map(str.rstrip, f):
        if line:  # skips empty lines
            try:
                subprocess.check_call(["nslookup", line],
                                         stdout=out)
            except subprocess.CalledProcessError:
                pass 
try:
    with open('dns.txt', 'r') as fr:
        lines = fr.readlines()
  
        with open('dns.txt', 'w') as fw:
            for line in lines:
                
                if line.find('Servidor') == -1:
                    fw.write(line)
except:
    pass

with open("dns.txt", "r+") as f:
    print(loja,caixa,f.read(),file=f)     		

try:
    with open('dns.txt', 'r') as fr:
        lines = fr.readlines()
          
        ptr = 1
      
        with open('dns.txt', 'w') as fw:
            for line in lines:
                
                if ptr != 1:
                    fw.write(line)
                ptr += 1
except:
    pass

try:
    with open('dns.txt', 'r') as fr:
        lines = fr.readlines()
  
        min_len = 7
  
        with open('dns.txt', 'w') as fw:
            for line in lines:
                if len(line.strip('\n')) >= min_len:
                    fw.write(line)
except:
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

files1 = glob.glob(os.path.join(path,'nfce.dll'))
files1.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files2 = glob.glob(os.path.join(path,'nfe2ws4.exe'))
files2.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files3 = glob.glob(os.path.join(path,'pdvsal.exe'))
files3.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files4 = glob.glob(os.path.join(path,'satsal.dll'))
files4.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])


with open('versao_pdv.txt',"w") as stream:
	for file in files:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		#print(loja,caixa,file=stream)
		print(loja,(','),caixa,(','),file,(','), file_time.strftime("%Y-%m-%d"), file=stream)

with open('versao_pdv.txt',"a") as stream:
	for file in files1:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(loja,(','),caixa,(','),file,(','), file_time.strftime("%Y-%m-%d"), file=stream)

with open('versao_pdv.txt',"a") as stream:
	for file in files2:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(loja,(','),caixa,(','),file,(','), file_time.strftime("%Y-%m-%d"), file=stream)

with open('versao_pdv.txt',"a") as stream:
	for file in files3:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(loja,(','),caixa,(','),file,(','), file_time.strftime("%Y-%m-%d"), file=stream)

with open('versao_pdv.txt',"a") as stream:
	for file in files4:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(loja,(','),caixa,(','),file,(','), file_time.strftime("%Y-%m-%d"), file=stream)

path = 'c:\\pdv\\plugin'

files8 = glob.glob(os.path.join(path, '*.dll'))
#files8.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d)', x)])

with open('versao_pdv.txt',"a") as stream:
	for file in files8:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		#print(loja, file,(' '), file_time.strftime("%Y-%M-%D"))
		print(loja,(','),caixa,(','),file,(','), file_time.strftime("%Y-%m-%d"), file=stream)
	
		
		
		
#files9 = glob.glob(os.path.join(path,'apromos.dll'))
#files9.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

#with open('versao_pdv.txt',"a") as stream:
#	for file in files9:
#		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
#		print(file,(' '), file_time.strftime("%d/%m/%Y"), file=stream)


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
       
    config.read('socket.ini')
    ip = config.get('servidor', 'ip')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9005))
    s.sendall(pickle.dumps(info))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9005))
    s.sendall(pickle.dumps(info1))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9005))
    s.sendall(pickle.dumps(info2))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9005))
    s.sendall(pickle.dumps(info3))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9005))
    s.sendall(pickle.dumps(info4))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9005))
    s.sendall(pickle.dumps(info5))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9005))
    s.sendall(pickle.dumps(info6))

except socket.error as err:
	print ("Sem conexão com o servidor") 
	logging.info("Sem conexão com o servidor!!!")
except configparser.NoSectionError as err:
    print("Sem arquivo socket.ini")
    logging.info("Sem arquivo socket.ini!!!")
    
	
