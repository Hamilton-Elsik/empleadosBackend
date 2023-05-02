from DTO.EmpleadoDTO import empleadoDTO
from configDb.configDb import DB_PATH
import sqlite3

async def query_extractor(skip: int = 0, limit: int = 100):
    return { "skipRepo": skip, "limitRepo": limit}

async def query_get_empleados():
    auxmodel= []
    con = sqlite3.connect(DB_PATH, detect_types=sqlite3.PARSE_COLNAMES)
    cur = con.cursor()
    cur.execute('select * from empleados')
    auxData = cur.fetchall()
    for x in auxData:
        auxmodel.append( {'id': x[0], 'primer_apellido': x[1], 'primer_nombre': x[2],
                   'otros_nombres': x[3], 'tipo_identificacion': x[4], 
                   "numero_identificacion": x[5], "pais_empleo": x[6],
                   "email": x[7], "fecha_ingreso": x[8], "registro": x[9]})
    # print(auxmodel)

    return auxmodel

async def query_crear_empleado(empleadoDTO: empleadoDTO):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("INSERT INTO empleados VALUES (NULL,?,?,?,?,?,?,?,?,?)"
                ,(
        empleadoDTO.primer_apellido,
        empleadoDTO.primer_nombre,
        empleadoDTO.otros_nombres,
        empleadoDTO.tipo_identificacion,
        empleadoDTO.numero_identificacion,
        empleadoDTO.pais_empleo,
        empleadoDTO.email,
        empleadoDTO.fecha_ingreso,
        empleadoDTO.registro
        ))
    con.commit()
    con.close()
    # print('repository')
    return empleadoDTO

async def query_delete_empleados(id: int):
    try:
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("DELETE FROM empleados WHERE id=?", (id,))
        con.commit()
        con.close()
        print(id)
        return id
    except:
        return id