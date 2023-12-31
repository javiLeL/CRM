import sqlite3

class log:
    def __init__(self, empresa, correo_electronico, password):
        self.empresa=str(empresa)
        self.correo_electronico=str(correo_electronico)
        self.password=str(password)
        try:
            miConexion = sqlite3.connect("LOGGIN")
            miCursor = miConexion.cursor()
            miCursor.execute("""
                                CREATE TABLE LOGGIN (
                                    nombre_empresa VARCHAR(50),
                                    correo_electronico VARCHAR(50) PRIMARY KEY,
                                    password VARCHAR(50)
                            );""")
            miConexion.commit()
            miConexion.close()
        except:
            pass
            # print("Ya esta creada la base de datos LOGGIN")
        # print("Creada conexion")
    def register(self):
            try:
                miConexion = sqlite3.connect("LOGGIN")
                miCursor = miConexion.cursor()
                miCursor.executemany("INSERT INTO LOGGIN VALUES (?, ?, ?)", [(str(self.empresa), str(self.correo_electronico), str(self.password))])
                miConexion.commit()
                miConexion.close()
            except:
                print("Error al crear el registro")
            
            try:
                miConexion = sqlite3.connect(str(self.empresa).upper())
                miCursor = miConexion.cursor()
                miCursor.execute("""
                                    CREATE TABLE USUARIOS (
                                        nombre VARCHAR(50) PRIMARY KEY,
                                        password VARCHAR(50)
                                    );""")
                miCursor.execute("""
                                    CREATE TABLE CONTACTOS (
                                        ID VARCHAR(50) PRIMARY KEY,
                                        nombre VARCHAR(50),
                                        calle VARCHAR(50),
                                        codigopostal VARCHAR(50),
                                        telefono VARCHAR(50),
                                        personaContacto VARCHAR(50),
                                        correo_electronico VARCHAR(50),
                                        porcentaje_iva VARCHAR(50)
                                    );""")
                miCursor.execute("""
                                    CREATE TABLE OPORTUNIDADES (
                                        ID VARCHAR(50) PRIMARY KEY,
                                        contacto VARCHAR(50),
                                        nombre VARCHAR(50),
                                        correo_electronico VARCHAR(50),
                                        telefono VARCHAR(50),
                                        ingreso VARCHAR(50),
                                        estado VARCHAR(50)
                                    );""")
                miCursor.execute("""
                                    CREATE TABLE PRODUCTOS (
                                        ID VARCHAR(50) PRIMARY KEY,
                                        nombre VARCHAR(50),
                                        descripcion VARCHAR(50),
                                        stok VARCHAR(50),
                                        precio VARCHAR(50)
                                    );""")
                miConexion.commit()
                miConexion.close()
            except:
                print("Ya esta creada la base de datos "+str(self.empresa).upper())
            
            try:
                miConexion = sqlite3.connect(str(self.empresa).upper())
                miCursor = miConexion.cursor()
                miCursor.executemany("INSERT INTO USUARIOS VALUES (?, ?)", [("root", "toor")])
                miConexion.commit()
                miConexion.close()
            except:
                print("Error al crear el registro")
    def loggin ():
        pass

    def isLoggin(self):
        lista=[]
        try:
            miConexion = sqlite3.connect("LOGGIN")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM LOGGIN WHERE correo_electronico=?", [(str(self.correo_electronico))])
            lista = miCursor.fetchall()
        except:
            print("Error al buscar los datos")
        print()
        if(lista==[]):
            print("No se encontro el correo registrando...")
            self.register()
        else:
            if(str(lista[0][2])==self.password and str(lista[0][0])==self.empresa): 
                return True
            else:
                return False
    def __str__(self):
        return "Empresa: "+self.empresa+" Correo: "+self.correo_electronico+" passwd: "+self.password