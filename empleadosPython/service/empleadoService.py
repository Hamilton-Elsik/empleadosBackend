from typing import Annotated, Any
from fastapi import Depends
from repositories.EmpleadoRepository import query_crear_empleado, query_get_empleados, query_delete_empleados, query_extractor
from DTO.EmpleadoDTO import empleadoDTO

def query_or_cookie_extractor(
    q: Annotated[Any, Depends(query_extractor)],
    skip: int = 0, limit: int = 100,
):
    # last_query: { "skip": skip, "limit": limit}
    if not q:
        return "last_query"
    return q

# def crear_empleado(
#     q: Annotated[empleadoDTO, Depends(query_empleado)],
#     empleadoDTO,
# ):
#     # last_query: { "skip": skip, "limit": limit}
#     if not q:
#         return "last_query"
#     return q

def crear_empleado( q: Annotated[Any, Depends(query_crear_empleado)]):
    # print('servcice', empleadoDTO.email)
    return q

def get_empleados( q: Annotated[list[empleadoDTO], Depends(query_get_empleados)]):
    # print('servcice', empleadoDTO.email)
    return q

def delete_empleados( q: Annotated[Any, Depends(query_delete_empleados)]):
    # print('servcice', empleadoDTO.email)
    return q
