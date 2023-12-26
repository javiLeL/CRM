import sqlite3

class log:
    def __init__(self, empresa, nombre, password):
        self.empresa=empresa
        self.nombre=nombre
        self.password=password
        try:
            miConexion = sqlite3.connect("LOGIN")
            miCursor = miConexion.cursor()
            miCursor.execute("""
                                CREATE TABLE LOGIN (
                                    nombre_empresa VARCHAR(50) NOT NULL,
                                    correo_electrónico VARCHAR(50) NOT NULL PRIMARY KEY,
                                    contrasena VARCHAR(50) NOT NULL
                            );""")
            miConexion.commit()
            miConexion.close()
        except:
            print("Ya esta creada la base de datos LOGGIN")
    def register():
        pass

    def loggin ():
        pass

    def isNewLoggin():
        pass