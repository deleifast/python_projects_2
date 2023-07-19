#encoding: iso-8859-1
import os, os.path, configparser

import tkinter as tk
from tkinter import *

from satcfe import BibliotecaSAT
from satcfe import ClienteSATLocal
from satcfe.excecoes import ErroRespostaSATInvalida
from satcfe.excecoes import ExcecaoRespostaSAT

config = configparser.ConfigParser(defaults=None, strict=False, allow_no_value=True)
config.optionxform = str

source = os.listdir('c:\\pdv')

config.read('PDVSAL.INI')

caixa = config.get('IMPRESSORA','CAIXA')
loja = config.get('LOJA', 'NUMERO')

gui = tk.Tk()

gui.geometry('400x50')
gui.title('Pdvcoral - Remarca')
gui.resizable(0,0)

msg = Label(gui, text='Consultando SAT_SWEDA, aguarde....', fg="red", font='Arial 18')
msg.place(x=1, y=10)

cliente = ClienteSATLocal(BibliotecaSAT('c:\pdv\satdll.dll'),
            codigo_ativacao='123123123')

 

try:
    resp = cliente.consultar_status_operacional()

    if resp.LISTA_INICIAL != resp.LISTA_FINAL:
      
      r = "      Pendentes      "

#      ipAddress   = socket.gethostbyname_ex(socket.gethostname())

      f =  open ('sat.txt', "w") 
      print(loja,',',caixa,',','SWEDA',',',resp.DH_CFE,',',resp.DH_ULTIMA,',',resp.NSERIE,',',resp.VER_SB,',',resp.LISTA_INICIAL,',',resp.LISTA_FINAL,',',resp.CERT_EMISSAO,',',resp.CERT_VENCIMENTO,',',resp.LAN_IP,',',resp.LAN_DNS_1,',',resp.LAN_DNS_2,',',resp.LAN_GW,',',resp.LAN_MASK, file= f)
      f.close()    

    else:
        r = "      Sem Cupons  "
        f =  open ('sat.txt', "w")
        print(loja,',',caixa,',','SWEDA',',',resp.DH_CFE,',',resp.DH_ULTIMA,',',resp.NSERIE,',',resp.VER_SB,',',resp.LISTA_INICIAL,',',resp.LISTA_FINAL,',',resp.CERT_EMISSAO,',',resp.CERT_VENCIMENTO,',',resp.LAN_IP,',',resp.LAN_DNS_1,',',resp.LAN_DNS_2,',',resp.LAN_GW,',',resp.LAN_MASK,',',r, file= f)
        f.close()

except ErroRespostaSATInvalida as ex_resp_invalida:
  f =  open ('sat.txt', "w") 
  print(loja, caixa, 'SWEDA','|', 'Status SAT - Resposta inválida', file = f)
  f.close()
    
except ExcecaoRespostaSAT as ex_resposta:
  resp = ex_resposta.resposta
  if resp.EEEEE != '10000':
    f =  open ('sat.txt', "w")
    print(loja, caixa, 'SWEDA','|', resp.msg, resp.EEEEE, file = f)
    f.close()
    pass
    
def sair():
  gui.destroy()
  return

gui.after(3000, sair)


gui.mainloop()
