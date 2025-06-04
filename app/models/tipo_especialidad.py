from dataclasses import dataclass 


@dataclass(init=False, repr=False, eq=False)
class TipoEspecialidad():
    nombre: str
    nivel: str