from dataclasses import dataclass 


@dataclass(init=False, repr=False, eq=False)
class CategoriaCargo():
    nombre: str 