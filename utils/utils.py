import os

def entradas(mensaje):
    print(mensaje)
    return input("\033[03;30m>>> \033[0m")

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')