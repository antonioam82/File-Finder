#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from colorama import init, Fore, Back, Style
import re

def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))
			
def change_dir(d):
    if os.path.isdir(d):
        os.chdir(d)
        print("Directorio actual: {} ".format(os.getcwd())+"\n")
    else:
        print(Fore.RED+"ERROR, DIRECTORIO NO VÁLIDO"+Fore.RESET+"\n")

def show_dir(direc):
    global showed_dir
    if showed_dir == False:
        print(Fore.BLUE+Back.WHITE+direc+Fore.RESET+Back.RESET)
        showed_dir = True

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def commands():
    print(Fore.WHITE+Back.BLUE+"---------------------------------COMANDOS---------------------------------")
    print("cbd <dir>                                           CAMBIA DIRECTORIO BASE")
    print("sch <string>                                            BÚSQUEDA CON REGEX")
    print("cl                                                       LIMPIEZA PANTALLA")
    print("q                                                       FINALIZAR PROGRAMA")
    print("help                                                MUESTRA LISTA COMANDOS")
    print("--------------------------------------------------------------------------\n"+Fore.RESET+Back.RESET)

def start():
    print(Back.BLUE+"\n--------------------------FILE FINDER WITH REGEX--------------------------")
    print(Back.RESET+"")
    print("Directorio actual: {} ".format(os.getcwd())+"\n")
    
init()

command_list = ['cl','cbd','sch','q','help']#lista comandos
start()

while True:
    count = 0
    showed_dir = False
    command = input("Command: ").split(" ")
    
    if command[0] in command_list:
        if command[0] == "cbd":
            change_dir(command[1])
        elif command[0] == "q":
            break
        elif command[0] == "cl":
            clear()
            start()
        elif command[0] == "help":
            commands()
        elif command[0] == "sch":
            command.pop(0)
            string = (" ").join(command)
            print(string)
            texto_entrada = BMP(string)
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

                if count == 0:
                    print(Fore.BLACK+Back.RED+"No se encontraron coincidencias con \'{}\'.".format(texto_entrada)+Fore.RESET+Back.RESET+"\n")
                else:
                    if count == 1:
                        print(Fore.BLACK+Back.GREEN+"\n1 ARCHIVO ENCONTRADO."+Fore.RESET+Back.RESET+"\n")
                    else:
                        print(Fore.BLACK+Back.GREEN+"\n{} ARCHIVOS ENCONTRADOS.".format(count)+Fore.RESET+Back.RESET+"\n")
                
            except Exception as e:
                print(Fore.BLACK+Back.RED+'ERROR: {} '.format(str(e))+Fore.RESET+Back.RESET+"\n")
        
    else:
        print(Fore.RED+"ERROR, COMANDO NO VÁLIDO"+Fore.RESET+"\n")
   
