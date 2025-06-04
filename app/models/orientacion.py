from dataclasses import dataclass
from app.models.especialidad import Especialidad
from app.models.plan import Plan
from app.models.materia import Materia

@dataclass(init=False, repr=False, eq=False)
class Orientacion():
    nombre: str
    especialidad: Especialidad
    plan: Plan
    materia: Materia

