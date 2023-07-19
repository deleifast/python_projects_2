#encoding: iso-8859-1
import os, os.path, socket

import tkinter as tk
from tkinter import *

from satcfe import BibliotecaSAT
from satcfe import ClienteSATLocal
from satcfe.excecoes import ErroRespostaSATInvalida
from satcfe.excecoes import ExcecaoRespostaSAT

gui = tk.Tk()

gui.geometry('400x50')
gui.title('Pdvcoral - Remarca')
gui.resizable(0,0)

msg = Label(gui, text='Consultando SAT_TANCA, aguarde....', fg="red", font='Arial 18')
msg.place(x=1, y=10)

cliente = ClienteSATLocal(BibliotecaSAT('c:\pdv\sat.dll'),
            codigo_ativacao='123123123')

 

try:
    resp = cliente.consultar_status_operacional()

    if resp.LISTA_INICIAL != resp.LISTA_FINAL:
      
      r = "      Pendentes      "

#      ipAddress   = socket.gethostbyname_ex(socket.gethostname())

      f =  open ('sat.txt', "w") 
      print('TANCA','  ',resp.DH_CFE,'  ',resp.DH_ULTIMA,'    ',resp.NSERIE,'   ',resp.VER_SB,r,'       ',resp.LISTA_INICIAL,'     ',resp.LISTA_FINAL,'     ',resp.CERT_EMISSAO,'     ',resp.CERT_VENCIMENTO, file= f)
      f.close()    

    else:
        r = "      Sem Cupons  "
 #       ipAddress   = socket.gethostbyname_ex(socket.gethostname())        
        f =  open ('sat.txt', "w")
        print('TANCA','  ',resp.DH_CFE,'   ',resp.DH_ULTIMA,'    ',resp.NSERIE,'   ',resp.VER_SB,r,'       ',resp.LISTA_INICIAL,'     ',resp.LISTA_FINAL,'     ',resp.CERT_EMISSAO,'     ',resp.CERT_VENCIMENTO, file= f)
        f.close()

except ErroRespostaSATInvalida as ex_resp_invalida:
  f =  open ('sat.txt', "w") 
  print('TANCA','|', 'Status SAT - Resposta inválida', file = f)
  f.close()
    
except ExcecaoRespostaSAT as ex_resposta:
  resp = ex_resposta.resposta
  if resp.EEEEE != '10000':
    f =  open ('sat.txt', "w")
    print('TANCA','|', resp.msg, resp.EEEEE, file = f)
    f.close()
    pass
    
def sair():
  gui.destroy()
  return

gui.after(3000, sair)


gui.mainloop()
