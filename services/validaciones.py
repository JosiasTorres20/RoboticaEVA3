from utils.utils import entradas, limpiar
from services.rut import buscarRut
from services.clave import validarClave
from services.rut import validarFormatoRut

def soloTexto(texto):
    while True:
        dato = entradas(f"Ingrese {texto}")
        if not dato.strip().isalpha():
            limpiar()
            print(f"{texto} invalido. Solo letras y no debe estar vacio")
        else:
            limpiar()
            return dato
        
def rutUnico():
    while True:
        rut = entradas("Ingrese RUT")
        if not validarFormatoRut(rut):
            limpiar()
            print("Formato de RUT incorrecto. \033[03;30m12345678-9\033[0m")
        elif buscarRut(rut):
            limpiar()
            print("RUT ya registrado")
        else:
            limpiar()
            return rut

def claveSegura():
    while True:
        clave = entradas("Ingrese Clave")
        if not validarClave(clave):
            limpiar()
            print("Clave invalida. Debe tener entre 8 y 16 caracteres, una mayuscula, una minuscula y un numero")
        else:
            limpiar()
            return clave