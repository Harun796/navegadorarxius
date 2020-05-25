import os, sys
import shutil
from shutil import copyfile

menu = "0"
while(menu!="2"):
  menu= input("1 Escull fitxers/ 2 Tancar")
  if(menu == "1" ):
    #Open a file
    path = "fitxers"
    dirs = os.listdir( path )
    # This would print all the files and directories
    for file in dirs:
      print(file)
    resposta= input("Quin document vols")
    if os.path.exists(path+"/"+resposta):
      document = open(path+"/"+resposta,"r")
      contingut = document.read()
      print(contingut)
      continguts=contingut.split()
      confirmacio= input("Vols executar")
      if(continguts[0]=="moure" and confirmacio == "si"):
        if os.path.exists(path+"/"+continguts[1]):
          shutil.move(path+"/"+continguts[1] , path+"/"+ continguts[2])
        else:
          print("El document que vols moure no existeix")
      elif(continguts[0] == "borra"and confirmacio == "si"):
        if os.path.exists(path+"/"+continguts[1]):
          os.remove(path+"/"+continguts[1])
        else:
          print("L'arxiu que vols borrar no existeix")
      elif(continguts[0] == "copia"and confirmacio == "si"):
        if os.path.exists(path+"/"+continguts[1]):
          copyfile(path+"/"+continguts[1], path+"/"+continguts[2])
        else:
          print("El document que vols copiar no existeix")
      document.close()
    else:
      print("No existeix")
      resposta= input("Quin document vols")
