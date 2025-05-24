import re

def validarClave(clave):
    regex = r"^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$"
    return re.match(regex, clave) is not None
