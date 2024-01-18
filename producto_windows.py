from tkinter import *
import sqlite3

def exit_btn():
    ventana_añadir_var.destroy()
    ventana_añadir_var.update()

def new_cliente(nombre, descripcion, stock, precio_unitario):
    print([(str(nombre), str(descripcion), int(stock), str(precio_unitario))])
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.executemany("INSERT INTO PRODUCTO (nombre, descripcion, stock, precio_unitario) VALUES (?, ?, ?, ?)", [(str(nombre), str(descripcion), int(stock), str(precio_unitario))])
        miConexion.commit()
        miConexion.close()
        print("Introducido")
        exit_btn()
    except:
        print("Error al crear el registro")

def ventana_añadir(bbdd):
    global ventana_añadir_var
    global empresa
    empresa = bbdd
    ventana_añadir_var = Toplevel()
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
    precio_unitario2 = Label(miFrame, text = "Precio Unitario: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1
    
    botonEnvio = Button (miFrame, text="Cancelar", command=exit_btn)
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Enviar", command=lambda:new_cliente(nombre=nombre.get(), descripcion=descripcion.get(), stock=stock.get(), precio_unitario=precio_unitario.get()))
    botonEnvio.grid(row = row, column = 1)