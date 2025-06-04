from dataclasses import dataclass

@dataclass(init=False, repr=False, eq=False)
class Materia():
    nombre: str
    codigo: str
    observacion: str