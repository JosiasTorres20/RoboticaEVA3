from services.rut import buscarRut
from services.clave import validarClave
from services.rut import validarFormatoRut
from utils.utils import entradas, limpiar
from database.db import guardarUsuario
from models.usuario import Usuario
from services.validaciones import soloTexto, rutUnico, claveSegura



def crearCuenta():
    limpiar()
    print("Creando Cuenta")
    nombre = soloTexto("Ingrese Nombre")

    apellidoPaterno = soloTexto("Ingrese Apellido Paterno")

    apellidoMaterno = soloTexto("Ingrese Apellido Materno")

    rut = rutUnico("Ingrese Rut")

    clave = claveSegura("Ingrese Clave")

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