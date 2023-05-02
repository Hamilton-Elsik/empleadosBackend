from fastapi import Depends, APIRouter, status
from DTO.EmpleadoDTO import empleadoDTO
from typing import Annotated, Any
from service.empleadoService import crear_empleado, get_empleados, delete_empleados, query_or_cookie_extractor
from fastapi.encoders import jsonable_encoder

empleado = APIRouter()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @empleado.get("/empleados", response_model=list[empleadoDTO], status_code=status.HTTP_200_OK)
@empleado.get("/empleados", status_code=status.HTTP_200_OK)
# async def read_item(skip: int = 0, limit: int = 10):
async def read_items(commons: Annotated[list[empleadoDTO], Depends(get_empleados)]):
    # json_compatible_item_data = jsonable_encoder(commons)
    print(commons)
    return commons

@empleado.get("/empleados/{id}", response_model=empleadoDTO, status_code=status.HTTP_200_OK)
async def read_item(id: int):
    return{"id": id}

@empleado.post("/empleados", response_model=empleadoDTO, status_code=status.HTTP_201_CREATED)
async def create_item(commons: Annotated[empleadoDTO, Depends(crear_empleado)]):
    return commons

@empleado.put("/empleados/{id}", response_model=empleadoDTO, status_code=status.HTTP_200_OK)
async def update_item(id: int, empleadoDTO: empleadoDTO):
    return {"id": id, **empleadoDTO.dict()}

@empleado.delete("/empleados/{id}", status_code=status.HTTP_200_OK)
async def read_item(commons: Annotated[Any, Depends(delete_empleados)]):
    return commons