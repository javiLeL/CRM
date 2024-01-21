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
                                    CREATE TABLE CLIENTE (
                                        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nombre VARCHAR(50) NOT NULL,
                                        calle VARCHAR(50) NOT NULL,
                                        codigo_postal VARCHAR(50) NOT NULL,
                                        ciudad VARCHAR(50) NOT NULL,
                                        pais VARCHAR(50) NOT NULL,
                                        telefono VARCHAR(50) NOT NULL,
                                        persona_de_contacto VARCHAR(50) NOT NULL,
                                        correo_electronico VARCHAR(50) NOT NULL,
                                        iva VARCHAR(50) NOT NULL
                                    );""")
                miCursor.execute("""
                                    CREATE TABLE PRESUPUESTO (
                                        id_presupuesto INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nombre VARCHAR(50) NOT NULL,
                                        fecha_creacion VARCHAR(50) NOT NULL,
                                        fecha_expiracion VARCHAR(50)
                                    );""")
                miCursor.execute("""
                                    CREATE TABLE OPORTUNIDAD (
                                        id_oportunidad INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nombre VARCHAR(50) NOT NULL,
                                        ingreso INTEGER NOT NULL,
                                        estado VARCHAR(50) NOT NULL,
                                        id_cliente INTEGER NOT NULL,
                                        id_presupuesto INTEGER NOT NULL,
                                        FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente) ON DELETE CASCADE,
                                        FOREIGN KEY (id_presupuesto) REFERENCES PRESUPUESTO(id_presupuesto) ON DELETE CASCADE
                                    );""")
                miCursor.execute("""
                                    CREATE TABLE PRODUCTO (
                                        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nombre VARCHAR(50) NOT NULL,
                                        descripcion VARCHAR(50) NOT NULL,
                                        stock INTEGER NOT NULL,
                                        precio_unitario INTEGER NOT NULL
                                    );""")
                miCursor.execute("""
                                    CREATE TABLE PEDIDO (
                                        id_presupuesto INTEGER NOT NULL,
                                        id_producto INTEGER NOT NULL,
                                        cantidad INTEGER NOT NULL,
                                        PRIMARY KEY(id_presupuesto, id_producto),
                                        FOREIGN KEY (id_presupuesto) REFERENCES PRESUPUESTO(id_presupuesto) ON DELETE CASCADE,
                                        FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto) ON DELETE CASCADE
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