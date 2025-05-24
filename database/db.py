import json, os 
from models.usuario import Usuario

DB = "usuarios.json"

def guardarUsuario(usuario):
    usuarios = obtenerUsuarios()
    usuarios.append(usuario)
    guardarUsuarios(usuarios)


def obtenerUsuarios():
    if not os.path.exists(DB):
        return []
    with open(DB, "r", encoding="utf-8") as file:
        data = json.load(file)
        usuarios = []
        for u in data:
            usuario = Usuario("", "", "", "", "").cargarDict(u)
            usuarios.append(usuario)
        return usuarios

def guardarUsuarios(usuarios):
    with open(DB, "w", encoding="utf-8") as archivo:
        json.dump([usuario.to_dict() for usuario in usuarios], archivo, indent=4, ensure_ascii=False)