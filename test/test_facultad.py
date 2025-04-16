from dataclasses import dataclass 

class Facultad():
    def __init(self):
        self.nombre = None
        self.abreviatura = None
        self.directorio = None
        self.sigla = None
        self.codigoPostal = None
        self.ciudad = None
        self.domicilio = None
        self.telefono = None
        self.contacto = None
        self.email = None


@dataclass(init=False, repr=False, eq=False)
class Facultad1(): 
    nombre: str 
    abreviatura : str
    directorio: str 
    sigla: str 
    codigoPostal : str
    ciudad : str
    domicilio : str
    telefono : str
    contacto : str
    email : str