import sqlite3

class log:
    def __init__(self, empresa, correo_electronico, password):
        self.empresa=str(empresa)
        self.correo_electrónico=str(correo_electronico)
        self.password=str(password)
        try:
            miConexion = sqlite3.connect("LOGGIN")
            miCursor = miConexion.cursor()
            miCursor.execute("""
                                CREATE TABLE LOGGIN (
                                    correo_electronico VARCHAR(50) PRIMARY KEY,
                                    nombre_empresa VARCHAR(50),
                                    password VARCHAR(50)
                            );""")
            miConexion.commit()
            miConexion.close()
        except:
            print("Ya esta creada la base de datos LOGGIN")
        print("Creada conexion")
    def register(self):
            try:
                miConexion = sqlite3.connect("LOGGIN")
                miCursor = miConexion.cursor()
                
                miCursor.executemany("INSERT INTO LOGGIN VALUES (?, ?, ?)", [(str(self.empresa), str(self.correo_electrónico), str(self.password))])

                miConexion.commit()
                miConexion.close()
            except:
                print("error")

    def loggin ():
        pass

    def isNewLoggin(self):
        try:
            miConexion = sqlite3.connect("LOGGIN")
            miCursor = miConexion.cursor()

            miCursor.execute("SELECT * FROM LOGGIN WHERE correo_electronico=?", [(self.correo_electronico)])
            lista = miCursor.fetchall()
            print(lista)
        except:
            self.register()

    def __str__(self):
        return "Empresa: "+self.empresa+" Correo: "+self.correo_electrónico+" passwd: "+self.password