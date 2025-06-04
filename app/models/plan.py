from dataclasses import dataclass

@dataclass(init=False, repr=False, eq=False)
class Plan():
    nombre: str
    fecha_inicio: str
    fecha_fin: str
    observacion: str