import tkinter as tk
from tkinter import *
import sqlite3


def ventana_añadir(bbdd):
    global ventana_añadir_var
    global empresa
    empresa = bbdd
    ventana_añadir_var = tk.Toplevel()
    miFrame = Frame(ventana_añadir_var, width=700, height=500)
    miFrame.pack()
    ventana_añadir_var.title("Nuevo Producto")

    row = 0

    nombre = StringVar()
    nombre2 = Entry(miFrame, textvariable = nombre)
    nombre2.grid(row = row, column = 1, padx=10, pady=10)
    nombre2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    descripcion = StringVar()
    descripcion2 = Entry(miFrame, textvariable = descripcion)
    descripcion2.grid(row = row, column = 1, padx=10, pady=10)
    descripcion2 = Label(miFrame, text = "Descripcion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    stock = StringVar()
    stock2 = Entry(miFrame, textvariable = stock)
    stock2.grid(row = row, column = 1, padx=10, pady=10)
    stock2 = Label(miFrame, text = "Stock: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    
    row += 1

    precio_unitario = StringVar()
    precio_unitario2 = Entry(miFrame, textvariable = precio_unitario)
    precio_unitario2.grid(row = row, column = 1, padx=10, pady=10)
    precio_unitario2 = Label(miFrame, text = "Stock: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1
    
    botonEnvio = Button (miFrame, text="Cancelar")
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Enviar")
    botonEnvio.grid(row = row, column = 1)