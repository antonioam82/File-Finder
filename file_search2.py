#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from colorama import init, Fore, Back, Style
from rich.console import Console
from rich.table import Table
import re

#print('[' + 'gamma'.center(20, '*') + ']')


def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

def change_dir(d):
    if os.path.isdir(d):
        os.chdir(d)
        print(Fore.GREEN+"Directorio actual: {} ".format(os.getcwd())+Fore.RESET+"\n")
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
    table = Table(title="COMANDOS")
    table.add_column("Comando")
    table.add_column("Acción")

    table.add_row("cbd <dir>", "Cambia directorio base")
    table.add_row("sch <string>", "Busqueda con regex")
    table.add_row("cl", "Limpieza de pantalla")
    table.add_row("q", "Finalizar programa")
    table.add_row("help", "Mostrar linea de comandos")

    #console = Console()
    console.print(table)

def start():
    init()
    print(Back.BLUE+"\n--------------------------FILE FINDER WITH REGEX--------------------------"+Back.RESET+"\n")
    print("Directorio actual: {} ".format(os.getcwd())+"\n")

def validate_entries(l):
    if len(l) > 1:
        if l[0] == 'sch' or l[0] == 'cbd':
            return l
    elif len(l) == 1:
        if l[0] == 'cl' or l[0] == 'help' or l[0] == 'q':
            return l
    else:
        return None


command_list = ['cl','cbd','sch','q','help']#lista comandos
console = Console()
start()
commands()

while True:
    count = 0
    showed_dir = False
    command = validate_entries(input(str(os.getcwd())+"\\FM:\\> ").split(" "))

    if command is not None and command[0] in command_list:
        if command[0] == "cbd":
            command.pop(0)
            dire = (" ").join(command)
            change_dir(dire)
        elif command[0] == "q":
            #clear()
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
