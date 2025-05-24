from database.db import obtenerUsuarios
import re
def buscarRut(rut):
    usuarios = obtenerUsuarios()
    return any(u.getRut() == rut for u in usuarios)


def validarFormatoRut(rut):
    return re.match(r"^\d{1,8}\-(\d|k|K)$", rut) is not None