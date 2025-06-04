from dataclasses import dataclass

@dataclass(init=False, repr=False, eq=False)
class Grado():
    nombre: str
    sigla: str
    duracion: int