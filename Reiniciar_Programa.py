import os
import subprocess
import shutil
import glob

os.remove('C://Retag/retag.old')

os.system("taskkill /im retag.exe")

os.rename('C://Retag/retag.exe','C://Retag/retag.6.0.32')


dest_dir = "C:\\RETAG"
for file in glob.glob(r'C:/PDV/PRINI/loja14/RETAG/retag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir1 = "C:\\RETAG\PLUGIN"
for file in glob.glob(r'C:/PDV/PRINI/loja14/RETAG/PLUGIN/*.dll'):
	print(file)
	shutil.copy(file, dest_dir1)

subprocess.call(["C://Retag/retag.exe"])
0
subprocess.call("exit 1", shell=True)
1

