from tkinter import *
import sqlite3

def exit_btn(ventana):
    ventana.destroy()
    ventana.update()

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
    fecha_expiracion2 = Label(miFrame, text = "Fecha de Creacion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    
    row += 1

    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_añadir_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Enviar")
    botonEnvio.grid(row = row, column = 1)