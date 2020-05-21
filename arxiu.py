import os, sys
import shutil
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
    document = open(path+"/"+resposta,"r")
    contingut = document.read()
    print(contingut)
    if(contingut[0] ==" moure"):
      if os.path.exists("demofile.txt"):
        os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
        shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
        os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
      else:
        print("The file does not exist")
    elif(contingut[0] == "borra"):
      if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
      else:
        print("The file does not exist")
    elif(contingut == "copia"):
      if os.path.exists("demofile.txt"):
        from shutil import copyfile
        copyfile(src, dst)
      else:
        print("The file does not exist")
    document.close()
