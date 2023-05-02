import sqlite3

DB_PATH = "database/empleados.db"


def createDB():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("""CREATE TABLE empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        primer_apellido VARCHAR(20),
        primer_nombre VARCHAR(20),
        otros_nombres VARCHAR(50), 
        tipo_identificacion VARCHAR(30),
        numero_identificacion VARCHAR(20),
        pais_empleo VARCHAR(20),
        email VARCHAR(100), 
        fecha_ingreso date, 
        registro date
        )""")
    con.commit()
    con.close()

# if __name__ == "__main__":
#     print("hola")
#     createDB()