#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pynput import keyboard
from colorama import init, Fore, Back, Style
from rich.console import Console
from rich.table import Table
import re

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
    try:
        if os.name == "posix":
            os.system("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system("cls")
    except Exception as e:
        error = str(e)
        text = "\n" + f"ERROR: {error}" + "\n"
        console.print(text,style="black on red")

def commands():
    print("\n")
    table = Table(title="COMANDOS")
    table.add_column("Comando")
    table.add_column("Acción")

    table.add_row("cbd <dir>", "Cambia directorio base")
    table.add_row("sch <string>", "Busqueda con regex")
    table.add_row("cl", "Limpieza de pantalla")
    table.add_row("q", "Finalizar programa")
    table.add_row("help", "Mostrar tabla de comandos")
    table.add_row("<SPACE BAR>","Detener proceso de busqueda")

    console.print(table)
    print("\n")

def start():
    init()
    text = '\n'+'FILE SEARCH WITH REGEX'.center(74, '-')+'\n'
    console.print(text,style="white on blue")
    print("Directorio actual: {} ".format(os.getcwd())+"\n")
    commands()

def validate_entries(l):
    if len(l) > 1:
        if l[0] == 'sch' or l[0] == 'cbd':
            return l
    elif len(l) == 1:
        if l[0] == 'cl' or l[0] == 'help' or l[0] == 'q':
            return l
    else:
        return None

def on_press(key):##
    global stop
    if key == keyboard.Key.space:
        stop = True
        return False


command_list = ['cl','cbd','sch','q','help']#lista comandos
console = Console()
start()
#commands()

while True:
    count = 0
    showed_dir = False
    stop = False
    command = validate_entries(input(str(os.getcwd())+"\\FM:\\> ").split(" "))

    if command is not None and command[0] in command_list:
        if command[0] == "cbd":
            command.pop(0)
            dire = (" ").join(command)
            change_dir(dire)
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
            
            listener = keyboard.Listener(on_press=on_press)
            listener.start()
            
            print("BUSCANDO...\n")
            try:
                for root, folders, files in os.walk(os.getcwd()):
                    if stop:
                        print("stopped")
                        listener.stop()
                        break
                    for file in files:
                        if stop:
                            break
                        match_ = re.search(texto_entrada, file)
                        if match_:
                            show_dir(root)
                            count+=1
                            print(Fore.GREEN+'{}-'.format(count)+os.path.join(root,BMP(Fore.YELLOW+Style.DIM+file+Fore.RESET+Style.NORMAL)))
                    showed_dir = False

                listener.stop()
                if count == 0:
                    text = "\n" + f"No se encontraron coincidencias con_'{texto_entrada}'." + "\n"
                    console.print(text,style="black on red")
                else:
                    if count == 1:
                        text = "\n"+"1 ARCHIVO ENCONTRADO."+"\n"
                        console.print(text,style="black on green")
                    else:
                        text = "\n"+str(count)+"_ARCHIVOS ENCONTRADOS."+"\n"
                        console.print(text,style="black on green")

            except Exception as e:
                error = str(e)
                text = "\n" + f"ERROR: {error}" + "\n"
                console.print(text,style="black on red")

    else:
        print(Fore.RED+"ERROR, COMANDO NO VÁLIDO"+Fore.RESET+"\n")

