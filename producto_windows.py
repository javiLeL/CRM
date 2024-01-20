from tkinter import *
from tkinter import ttk
import sqlite3

def exit_btn(ventana):
    ventana.destroy()
    ventana.update()

def new_cliente(nombre, descripcion, stock, precio_unitario):
    print([(str(nombre), str(descripcion), int(stock), str(precio_unitario))])
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.executemany("INSERT INTO PRODUCTO (nombre, descripcion, stock, precio_unitario) VALUES (?, ?, ?, ?)", [(str(nombre), str(descripcion), int(stock), str(precio_unitario))])
        miConexion.commit()
        miConexion.close()
        # print("Introducido")
        exit_btn(ventana_añadir_var)
    except:
        print("Error al crear el registro")

def getSelection(combo):
    id = str(combo.get()).split(" ")[0]
    print(id)
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT nombre, descripcion, stock, precio_unitario FROM PRODUCTO WHERE id_producto=?", [(id)])
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    print(lista)
    nombrever.set(lista[0][0])
    descripcionver.set(lista[0][1])
    stockver.set(lista[0][2])
    precio_unitariover.set(lista[0][3])

def getSelectionUpdate(combo):
    id = str(combo.get()).split(" ")[0]
    print(id)
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT nombre, descripcion, stock, precio_unitario FROM PRODUCTO WHERE id_producto=?", [(id)])
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    print(lista)
    nombreact.set(lista[0][0])
    descripcionact.set(lista[0][1])
    stockact.set(lista[0][2])
    precio_unitarioact.set(lista[0][3])

def update(combo, nombre, descripcion, stock, precio_unitario):
    id = str(combo.get()).split(" ")[0]
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.executemany("UPDATE PRODUCTO SET nombre=?, descripcion=?, stock=?, precio_unitario=? WHERE id_producto=?", [(str(nombre), str(descripcion), str(stock), str(precio_unitario), str(id))])
        miConexion.commit()
        miConexion.close()
        print("Actualizado")
        exit_btn(ventana_actualizar_var)
    except:
        print("Error al modificar el registro")

def select_producto():
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT id_producto, nombre nombre FROM PRODUCTO")
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    print(lista)
    return(lista)

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
    
    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_añadir_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Enviar", command=lambda:new_cliente(nombre=nombre.get(), descripcion=descripcion.get(), stock=stock.get(), precio_unitario=precio_unitario.get()))
    botonEnvio.grid(row = row, column = 1)

def ventana_ver(bbdd):
    global ventana_ver_var
    global empresa
    empresa = bbdd
    ventana_ver_var = Toplevel()
    miFrame = Frame(ventana_ver_var, width=700, height=500)
    miFrame.pack()
    ventana_ver_var.title("Ver Producto")

    row = 0

    listaContactos = select_producto()
    combo = Label(miFrame, text = "ID: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    combo = ttk.Combobox(miFrame, values = listaContactos, state = "readonly")
    combo.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    global nombrever, descripcionver, stockver, precio_unitariover
    nombrever = StringVar()
    nombrever2 = Entry(miFrame, textvariable = nombrever)
    nombrever2.grid(row = row, column = 1, padx=10, pady=10)
    nombrever2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    descripcionver = StringVar()
    descripcionver2 = Entry(miFrame, textvariable = descripcionver)
    descripcionver2.grid(row = row, column = 1, padx=10, pady=10)
    descripcionver2 = Label(miFrame, text = "Descripcion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    stockver = StringVar()
    stockver2 = Entry(miFrame, textvariable = stockver)
    stockver2.grid(row = row, column = 1, padx=10, pady=10)
    stockver2 = Label(miFrame, text = "Stock: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    
    row += 1

    precio_unitariover = StringVar()
    precio_unitariover2 = Entry(miFrame, textvariable = precio_unitariover)
    precio_unitariover2.grid(row = row, column = 1, padx=10, pady=10)
    precio_unitariover2 = Label(miFrame, text = "Precio Unitario: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1
    
    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_ver_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Buscar", command=lambda:getSelection(combo=combo))
    botonEnvio.grid(row = row, column = 1)

def ventana_actualizar(bbdd):
    global ventana_actualizar_var
    global empresa
    empresa = bbdd
    ventana_actualizar_var = Toplevel()
    miFrame = Frame(ventana_actualizar_var, width=700, height=500)
    miFrame.pack()
    ventana_actualizar_var.title("Actualizar Producto")

    row = 0

    listaContactos = select_producto()
    combo = Label(miFrame, text = "ID: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    combo = ttk.Combobox(miFrame, values = listaContactos, state = "readonly")
    combo.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    global nombreact, descripcionact, stockact, precio_unitarioact
    nombreact = StringVar()
    nombreact2 = Entry(miFrame, textvariable = nombreact)
    nombreact2.grid(row = row, column = 1, padx=10, pady=10)
    nombreact2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    descripcionact = StringVar()
    descripcionact2 = Entry(miFrame, textvariable = descripcionact)
    descripcionact2.grid(row = row, column = 1, padx=10, pady=10)
    descripcionact2 = Label(miFrame, text = "Descripcion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    stockact = StringVar()
    stockact2 = Entry(miFrame, textvariable = stockact)
    stockact2.grid(row = row, column = 1, padx=10, pady=10)
    stockact2 = Label(miFrame, text = "Stock: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    
    row += 1

    precio_unitarioact = StringVar()
    precio_unitarioact2 = Entry(miFrame, textvariable = precio_unitarioact)
    precio_unitarioact2.grid(row = row, column = 1, padx=10, pady=10)
    precio_unitarioact2 = Label(miFrame, text = "Precio Unitario: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1
    
    botonCancelar = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_actualizar_var))
    botonCancelar.grid(row = row, column = 0)

    botonBuscar = Button (miFrame, text="Buscar", command=lambda:getSelectionUpdate(combo=combo))
    botonBuscar.grid(row = row, column = 1)

    row += 1

    botonEnvio = Button (miFrame, text="Actualizar", command=lambda:update(combo=combo, nombre=nombreact.get(), descripcion=descripcionact.get(), stock=stockact.get(), precio_unitario=precio_unitarioact.get()))
    botonEnvio.grid(row = row, column = 1)