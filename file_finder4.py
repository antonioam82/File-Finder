#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from colorama import init, Fore, Back, Style
import re

def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

def ns(c):
    while c.lower()!=("s") and c.lower()!=("n"):
        c=input("Escribe solo \'n/N\' o \'s/S\' según su opción: ")
    return(c)
			
def change_dir():
    while True:
        dire = input("Introduzca directorio base: ").strip()
        if os.path.isdir(dire):
            os.chdir(dire)
            print("Directorio actual: {} ".format(os.getcwd()))
            break
        else:
            print(Fore.RED+"ERROR, DIRECTORIO NO VÁLIDO"+Fore.RESET)

def show_dir(direc):
    global showed_dir
    if showed_dir == False:
        print(Fore.BLUE+Back.WHITE+direc+Fore.RESET+Back.RESET)
        showed_dir = True

def start():
    print(Back.BLUE+"\n--------------------------FILE FINDER WITH REGEX--------------------------")
    print(Back.RESET+"")
    print("Directorio actual: {} ".format(os.getcwd()))
    
init()

command_list = ['cl','cbd','sch','q']#lista comandos
start()
while True:
    
    count = 0
    showed_dir = False
    command = input("Command: ")
    
    if command in command_list:
        if command == "cbd":
            change_dir()
        elif command == "q":
            break
        elif command == "cl":
            if os.name == "posix":
                os.system("clear")
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
            start()
        elif command == "sch":
            texto_entrada = BMP(input("Introduce patrón de búsqueda: "))
            print("BUSCANDO...\n")
            try:
                for root, folders, files in os.walk(os.getcwd()):
                    for file in files:
                        match_ = re.search(texto_entrada, file)
                        if match_:
                            show_dir(root)
                            count+=1
                            print(Fore.GREEN+'{}-'.format(count)+os.path.join(root,BMP(Fore.YELLOW+Style.DIM+file+Fore.RESET+Style.NORMAL)))
                    showed_dir = False
                    
                #time.sleep(1)
                if count == 0:
                    print(Fore.BLACK+Back.RED+"No se encontraron coincidencias con \'{}\'.".format(texto_entrada))
                else:
                    if count == 1:
                        print(Fore.BLACK+Back.GREEN+"\n1 ARCHIVO ENCONTRADO.")
                    else:
                        print(Fore.BLACK+Back.GREEN+"\n{} ARCHIVOS ENCONTRADOS.".format(count))
                
            except Exception as e:
                print(Fore.BLACK+Back.RED+'ERROR: {} '.format(str(e)))
                
        print(Fore.RESET+Back.RESET+"")
        
    else:
        print(Fore.RED+"ERROR, COMANDO NO VÁLIDO"+Fore.RESET)
   
