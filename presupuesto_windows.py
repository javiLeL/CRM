from tkinter import *
from tkinter import ttk
import sqlite3

def exit_btn(ventana):
    ventana.destroy()
    ventana.update()

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