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
      if(contingut[0] ==" moure"):
        shutil.move(path+"/"+contingut[1] , path+"/"+ contingut[2])
      elif(contingut[0] == "borra"):
        os.remove(path+"/"+document[1])
      elif(contingut == "copia"):
        copyfile(path+"/"+contingut[1], path+"/"+contingut[2])
      document.close()
    else:
      print("The file does not exist")
      resposta= input("Quin document vols")
