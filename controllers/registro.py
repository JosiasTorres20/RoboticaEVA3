from services.rut import buscarRut
from services.clave import validarClave
from services.rut import validarFormatoRut
from utils.utils import entradas, limpiar
from database.db import guardarUsuario
from models.usuario import Usuario



def crearCuenta():
    limpiar()
    print("Creando Cuenta")

    nombre = entradas("Ingrese Nombre")
    limpiar()

    apellidoPaterno = entradas("Ingrese Apellido Paterno")
    limpiar()

    apellidoMaterno = entradas("Ingrese Apellido Materno")
    limpiar()

    while True:
        rut = entradas("Ingrese Rut")

        if not validarFormatoRut(rut):
            limpiar()
            print("Formato de Rut incorrecto. \033[03;30m[12345678-9]\033[0m")
        elif buscarRut(rut):
            limpiar()
            print("Rut ya registrado")
        else:
            limpiar()
            break


    while True:

        clave = entradas("Ingrese Clave")

        if not validarClave(clave):
            limpiar()
            print("Clave invalida. Debe contener al menos 8 caracteres, una letra mayuscula, una letra minuscula y un numero.")
        else:
            limpiar()
            break

    usuario = Usuario(nombre, apellidoPaterno, apellidoMaterno, rut, clave)
    guardarUsuario(usuario)

    limpiar()
    print("\033[03;30mCuenta creada\033[0m")


def ejecucionCuenta():
    while True:
        crearCuenta()
        limpiar()
        opcion = entradas("Crear otra cuenta? (s/n)")
        if opcion == "s":
            continue
        elif opcion == "n":
            break
        else:
            print("Opcion no valida")
            continue