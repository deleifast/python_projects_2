import socket, pickle, os, configparser, shutil, re, glob, time
import datetime as dt

from subprocess import call

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
info1 = {'name': printer, 'file': f_imp}


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


path = "c:\pdv"

files = glob.glob(os.path.join(path,'pdvsal.exe'))
files.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files1 = glob.glob(os.path.join(path,'satsal.dll'))
files1.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files2 = glob.glob(os.path.join(path,'nfce.dll'))
files2.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])


with open('versao_pdv.txt',"w") as stream:
	for file in (files, files1, files2):
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(caixa,file=stream)
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)

path = 'c:\\pdv\\plugin'

files4 = glob.glob(os.path.join(path, 'clitef.dll'))
files4.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

with open('versao_pdv.txt',"a") as stream:
	for file in files4:
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)
		
		
files5 = glob.glob(os.path.join(path,'apromos.dll'))
files5.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

with open('versao_pdv.txt',"a") as stream:
	for file in files5:
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
info2 = {'name': ('lj') + loja + ('.') + ('verpdv_') + caixa + ('.txt'), 'file': f_bin1} 

f_bin1 = open(('lj') + loja + ('.') + ('key_') + caixa + ('.txt'), 'rb').read()
info1 = {'name': ('lj') + loja + ('.') + ('key_') + caixa + ('.txt'), 'file': f_bin1} 

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
	
except socket.error as err:
	print ("Sem conexão com o Servidor") 
	
