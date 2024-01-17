import tkinter as tk
from tkinter import *

def ventana_añadir():
    global ventana_añadir_var
    ventana_añadir_var = tk.Toplevel()
    miFrame = Frame(ventana_añadir_var, width=700, height=500)
    miFrame.pack()
    ventana_añadir_var.title("Nuevo Cliente")

    row = 0

    nombre = StringVar()
    nombre2 = Entry(miFrame, textvariable = nombre)
    nombre2.grid(row = row, column = 1, padx=10, pady=10)
    nombre2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    calle = StringVar()
    calle2 = Entry(miFrame, textvariable = calle)
    calle2.grid(row = row, column = 1, padx=10, pady=10)
    calle2 = Label(miFrame, text = "Calle: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    codigo_postal = StringVar()
    codigo_postal2 = Entry(miFrame, textvariable = codigo_postal)
    codigo_postal2.grid(row = row, column = 1, padx=10, pady=10)
    codigo_postal2 = Label(miFrame, text = "Codigo Postal: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    ciudad = StringVar()
    ciudad2 = Entry(miFrame, textvariable = ciudad)
    ciudad2.grid(row = row, column = 1, padx=10, pady=10)
    ciudad2 = Label(miFrame, text = "Ciudad: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    pais = StringVar()
    pais2 = Entry(miFrame, textvariable = pais)
    pais2.grid(row = row, column = 1, padx=10, pady=10)
    pais2 = Label(miFrame, text = "Pais: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    telefono = StringVar()
    telefono2 = Entry(miFrame, textvariable = telefono)
    telefono2.grid(row = row, column = 1, padx=10, pady=10)
    telefono2 = Label(miFrame, text = "Telefono: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    persona_contacto = StringVar()
    persona_contacto2 = Entry(miFrame, textvariable = persona_contacto)
    persona_contacto2.grid(row = row, column = 1, padx=10, pady=10)
    persona_contacto2 = Label(miFrame, text = "Persona de Contacto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    correo_electronico = StringVar()
    correo_electronico2 = Entry(miFrame, textvariable = correo_electronico)
    correo_electronico2.grid(row = row, column = 1, padx=10, pady=10)
    correo_electronico2 = Label(miFrame, text = "Correo Electronico: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    iva = StringVar()
    iva.set("21")
    iva2 = Entry(miFrame, textvariable = iva)
    iva2.grid(row = row, column = 1, padx=10, pady=10)
    iva2 = Label(miFrame, text = "Correo Electronico: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    botonEnvio = Button (miFrame, text="Cancelar")
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Enviar")
    botonEnvio.grid(row = row, column = 1)