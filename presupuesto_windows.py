from tkinter import *
from tkinter import ttk
import sqlite3

def exit_btn(ventana):
    ventana.destroy()
    ventana.update()

def getSelection(combo):
    id = str(combo.get()).split(" ")[0]
    print(id)
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT nombre, fecha_creacion, fecha_expiracion FROM PRESUPUESTO WHERE id_presupuesto=?", [(id)])
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    print(lista)
    nombrever.set(lista[0][0])
    fecha_creacionver.set(lista[0][1])
    fecha_expiracionver.set(lista[0][2])

def select_presupuesto():
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT id_presupuesto, nombre FROM PRESUPUESTO")
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    print(lista)
    return(lista)

def new_presupuesto(nombre, fecha_creacion, fecha_expiracion):
    print([(str(nombre), str(fecha_creacion), str(fecha_expiracion))])
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.executemany("INSERT INTO PRESUPUESTO (nombre, fecha_creacion, fecha_expiracion) VALUES (?, ?, ?)", [(str(nombre), str(fecha_creacion), str(fecha_expiracion))])
        miConexion.commit()
        miConexion.close()
        # print("Introducido")
        exit_btn(ventana_añadir_var)
    except:
        print("Error al crear el registro")

def ventana_añadir(bbdd):
    global ventana_añadir_var
    global empresa
    empresa = bbdd
    ventana_añadir_var = Toplevel()
    miFrame = Frame(ventana_añadir_var, width=700, height=500)
    miFrame.pack()
    ventana_añadir_var.title("Nuevo Presupuesto")

    row = 0

    nombre = StringVar()
    nombre2 = Entry(miFrame, textvariable = nombre)
    nombre2.grid(row = row, column = 1, padx=10, pady=10)
    nombre2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    fecha_creacion = StringVar()
    fecha_creacion2 = Entry(miFrame, textvariable = fecha_creacion)
    fecha_creacion2.grid(row = row, column = 1, padx=10, pady=10)
    fecha_creacion2 = Label(miFrame, text = "Fecha de Creacion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    fecha_expiracion = StringVar()
    fecha_expiracion2 = Entry(miFrame, textvariable = fecha_expiracion)
    fecha_expiracion2.grid(row = row, column = 1, padx=10, pady=10)
    fecha_expiracion2 = Label(miFrame, text = "Fecha de Expiracion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    
    row += 1

    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_añadir_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Enviar", command=lambda:new_presupuesto(nombre=nombre.get(), fecha_creacion=fecha_creacion.get(), fecha_expiracion=fecha_expiracion.get()))
    botonEnvio.grid(row = row, column = 1)

def ventana_ver(bbdd):
    global ventana_ver_var
    global empresa
    empresa = bbdd
    ventana_ver_var = Toplevel()
    miFrame = Frame(ventana_ver_var, width=700, height=500)
    miFrame.pack()
    ventana_ver_var.title("Ver Presupuestos")

    row = 0

    combo = Label(miFrame, text = "ID: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    combo = ttk.Combobox(miFrame, values = select_presupuesto(), state = "readonly")
    combo.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    global nombrever, fecha_creacionver, fecha_expiracionver

    nombrever = StringVar()
    nombrever2 = Entry(miFrame, textvariable = nombrever)
    nombrever2.grid(row = row, column = 1, padx=10, pady=10)
    nombrever2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    fecha_creacionver = StringVar()
    fecha_creacionver2 = Entry(miFrame, textvariable = fecha_creacionver)
    fecha_creacionver2.grid(row = row, column = 1, padx=10, pady=10)
    fecha_creacionver2 = Label(miFrame, text = "Fecha de Creacion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    fecha_expiracionver = StringVar()
    fecha_expiracionver2 = Entry(miFrame, textvariable = fecha_expiracionver)
    fecha_expiracionver2.grid(row = row, column = 1, padx=10, pady=10)
    fecha_expiracionver2 = Label(miFrame, text = "Fecha de Expiracion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    
    row += 1

    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_ver_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Buscar", command=lambda:getSelection(combo))
    botonEnvio.grid(row = row, column = 1)