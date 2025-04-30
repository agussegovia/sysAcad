from dataclasses import dataclass 

@dataclass(init=False, repr=False, eq=False)
class Facultad(): 
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