class Usuario:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, rut, clave):
        self.__nombre = nombre
        self.__apellidoPaterno = apellidoPaterno
        self.__apellidoMaterno = apellidoMaterno
        self.__rut = rut
        self.__clave = clave
    
    def getNombre(self):
        return self.__nombre
    def getApellidoPaterno(self):
        return self.__apellidoPaterno
    def getApellidoMaterno(self):
        return self.__apellidoMaterno
    def getRut(self):
        return self.__rut
    def getClave(self):
        return self.__clave
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setApellidoPaterno(self, apellidoPaterno):
        self.__apellidoPaterno = apellidoPaterno
    def setApellidoMaterno(self, apellidoMaterno):
        self.__apellidoMaterno = apellidoMaterno
    def setRut(self, rut):
        self.__rut = rut
    def setClave(self, clave):
        self.__clave = clave

    def to_dict(self):
        return {
            "Nombre": self.__nombre,
            "ApellidoPaterno": self.__apellidoPaterno,
            "ApellidoMaterno": self.__apellidoMaterno,
            "Rut": self.__rut,
            "Clave": self.__clave
        }

    def cargarDict(self, data):
        self.__nombre = data.get("Nombre", "")
        self.__apellidoPaterno = data.get("ApellidoPaterno", "")
        self.__apellidoMaterno = data.get("ApellidoMaterno", "")
        self.__rut = data.get("Rut", "")
        self.__clave = data.get("Clave", "")
        return self
    def __str__(self):
        txt = f"Nombre: {self.__nombre}\n"
        txt += f"Apellido Paterno: {self.__apellidoPaterno}\n"
        txt += f"Apellido Materno: {self.__apellidoMaterno}\n"
        txt += f"Rut: {self.__rut}\n"
        txt += f"Clave: {self.__clave}"
        return txt