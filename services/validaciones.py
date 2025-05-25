from utils.utils import entradas, limpiar
from services.rut import buscarRut, validarFormatoRut
from services.clave import validarClave
from services.rut import validarFormatoRut

def soloTexto(texto):
    while True:
        try: 
            dato = entradas(texto)
            if not dato.strip().isalpha():
                raise ValueError(f"El campo no debe estar vacio y solo debe contener letras. \033[03;30m{dato}\033[0m") 
            limpiar()
            return dato
        except ValueError as ve:
            limpiar()
            print(ve)
            raise

        
def rutUnico():
    while True:
        try:
            rut = entradas("Ingrese RUT")
            
            if not validarFormatoRut(rut):
                raise ValueError("Formato de RUT incorrecto. \033[03;30m12345678-9\033[0m")
            if len(rut) != 10:
                raise ValueError("El RUT debe tener 10 digitos. incluyendo guion")
            if buscarRut(rut):
                raise ValueError("RUT ya registrado")
            limpiar()
            return rut
        except ValueError as ve:
            limpiar()
            print(ve)



def claveSegura():
    while True:
        try:

            clave = entradas("Ingrese Clave")
            if not validarClave(clave):
                raise ValueError("Clave invalida. Debe tener entre 8 y 16 caracteres, una mayuscula, una minuscula y un numero")
            limpiar()
            return clave
        except ValueError as ve:
            limpiar()
            print(ve)
        except KeyboardInterrupt:
            print("Ejecucion interrumpida")
