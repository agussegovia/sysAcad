from dataclasses import dataclass

@dataclass(init=False, repr=False, eq=False)
class Departamento():
    nombre: str