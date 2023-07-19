#coding: utf-8
import os, datetime
from zipfile import ZipFile
from os import walk


for nome in os.listdir('c://xml'):
    dados = str(nome).split(".")
    numero = dados[0].split("F"+ "e")[1]
    subnumero = dados[1]
    novo_nome = "AD" + numero + "." + subnumero 
    
    os.rename("c://xml/"+nome, "c://xml/"+novo_nome)
    print("arquivo " + nome + " alterado para " + novo_nome)

'''zipxml = zipfile.ZipFile('C://PDV/XML/XML.ZIP', 'w')
for folder, subfolders, files in os.walk('C:/PDV/XML'):
    for file in files:
        if file.startswith('AD'):
            zipxml.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C://PDV/XML'), compress_type = zipfile.ZIP_DEFLATED)
 
zipxml.close()

z = zipfile.ZipFile("c://pdv/xml/xml.zip", 'r')


z.printdir()'''

os.chdir('c://xml')

current_directory = 'c://xml'
total = 0
cnt = 0
zip_list = []
name_count = 0 

file_names = os.listdir(current_directory)
file_count = len(os.listdir(current_directory))

while cnt<file_count:
    zip_list = []
    if file_count-cnt>9:
        zip_list = file_names[cnt:cnt+10]
        cnt = cnt+10
    else:
        zip_list = file_names[cnt:]
        cnt = file_count
    name_count +=1
    with ZipFile(str(name_count)+'.zip', 'w') as myzip:
        for f in zip_list:
            myzip.write(f)


