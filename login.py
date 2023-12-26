from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

miFrame = Frame(root, width=700, height=500)
miFrame.pack()

try:
    miConexion = sqlite3.connect("LOGIN")
    miCursor = miConexion.cursor()
    miCursor.execute("""
                        CREATE TABLE LOGIN (
                            id VARCHAR(50) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                            nombre_empresa VARCHAR(50) NOT NULL,
                            correo_electrónico VARCHAR(50) NOT NULL,
                            contrasena VARCHAR(50) NOT NULL
                    );""")
    miConexion.commit()
    miConexion.close()
except:
    pass

root.title("Loggin CRM")

row = 0

empresa = StringVar()
empresa2 = Entry(miFrame, textvariable = empresa)
empresa2.grid(row = row, column = 1, padx=10, pady=10)
empresa2 = Label(miFrame, text = "Empresa: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

row+=1

nombre = StringVar()
nombre2 = Entry(miFrame, textvariable = nombre)
nombre2.grid(row = row, column = 1, padx=10, pady=10)
nombre2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

row+=1

password = StringVar()
password2 = Entry(miFrame, textvariable = password)
password2.grid(row = row, column = 1, padx=10, pady=10)
password2 = Label(miFrame, text = "Password: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

row+=1

confirmar_password = StringVar()
confirmar_password2 = Entry(miFrame, textvariable = password)
confirmar_password2.grid(row = row, column = 1, padx=10, pady=10)
confirmar_password2 = Label(miFrame, text = "Confirmar Password: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

root.mainloop()