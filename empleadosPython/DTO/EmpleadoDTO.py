from pydantic import BaseModel
from datetime import datetime, date

class empleadoDTO(BaseModel):
    id: int | None
    primer_apellido: str
    primer_nombre: str
    otros_nombres: str
    tipo_identificacion: str
    numero_identificacion: str
    pais_empleo: str
    email: str | None
    fecha_ingreso: datetime | str
    registro: datetime | str