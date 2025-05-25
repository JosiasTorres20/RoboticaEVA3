from services.rut import buscarRut
from services.clave import validarClave
from services.rut import validarFormatoRut
from utils.utils import entradas, limpiar
from database.db import guardarUsuario
from models.usuario import Usuario
from services.validaciones import soloTexto, rutUnico, claveSegura
import sys


def crearCuenta():
    limpiar()
    print("Creando Cuenta")
    try:
        while True:
            try:
                nombre = soloTexto("Nombre")
                break
            except ValueError:
                continue

        while True:
            try:
                apellidoPaterno = soloTexto("Apellido Paterno")
                break
            except ValueError:
                continue

        while True:
            try:
                apellidoMaterno = soloTexto("Apellido Materno")
                break
            except ValueError:
                continue

        while True:
            try:
                rut = rutUnico()
                break
            except ValueError:
                continue

        while True:
            try:
                clave = claveSegura()
                break
            except ValueError:
                continue

        usuario = Usuario(nombre, apellidoPaterno, apellidoMaterno, rut, clave)
        guardarUsuario(usuario)
    except KeyboardInterrupt :
        print("Ejecucion interrumpida")
        sys.exit(0)


def ejecucionCuenta():
    while True:
        crearCuenta()
        limpiar()
        opcion = entradas("Crear otra cuenta? (s/n)").lower()
        if opcion == "s":
            continue
        elif opcion == "n":
            break
        else:
            print("Opcion no valida")
            continue