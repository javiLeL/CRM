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
        miCursor.execute("SELECT nombre, ingreso, estado, id_cliente, id_presupuesto FROM OPORTUNIDAD WHERE id_oportunidad=?", [(id)])
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    print(lista)
    nombrever.set(lista[0][0])
    ingresover.set(lista[0][1])
    estadover.set(lista[0][2])
    clientever.set(lista[0][3])
    presupuestover.set(lista[0][4])

def select_oportunidad():
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT id_oportunidad, nombre FROM OPORTUNIDAD")
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    # print(lista)
    return(lista)

def select_clientes():
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT id_cliente, nombre FROM CLIENTE")
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    # print(lista)
    return(lista)

def select_presupuesto():
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT id_presupuesto, nombre FROM PRESUPUESTO")
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    # print(lista)
    return(lista)

def new_oportunidad(nombre, ingreso, estado, id_cliente, id_presupuesto):
    print([(str(nombre), str(ingreso), str(estado), str(id_cliente.get()).split(" ")[0], str(id_presupuesto.get()).split(" ")[0])])
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.executemany("INSERT INTO OPORTUNIDAD (nombre, ingreso, estado, id_cliente, id_presupuesto) VALUES (?, ?, ?, ?, ?)", [(str(nombre), str(ingreso), str(estado), str(id_cliente.get()).split(" ")[0], str(id_presupuesto.get()).split(" ")[0])])
        miConexion.commit()
        miConexion.close()
        print("Introducido")
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
    ventana_añadir_var.title("Nueva Oportunidad")

    row = 0

    nombre = StringVar()
    nombre2 = Entry(miFrame, textvariable = nombre)
    nombre2.grid(row = row, column = 1, padx=10, pady=10)
    nombre2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    ingreso = StringVar()
    ingreso2 = Entry(miFrame, textvariable = ingreso)
    ingreso2.grid(row = row, column = 1, padx=10, pady=10)
    ingreso2 = Label(miFrame, text = "Ingreso esperado: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    comboEstado = Label(miFrame, text = "Presupuesto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    comboEstado = ttk.Combobox(miFrame, values = ["NUEVO", "CALIFICADO", "PROPUESTA", "GANADO"], state = "readonly")
    comboEstado.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    listaClientes = select_clientes()
    comboClientes = Label(miFrame, text = "Cliente: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    comboClientes = ttk.Combobox(miFrame, values = listaClientes, state = "readonly")
    comboClientes.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    listaPresupuesto = select_presupuesto()
    comboPresupuesto = Label(miFrame, text = "Presupuesto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    comboPresupuesto = ttk.Combobox(miFrame, values = listaPresupuesto, state = "readonly")
    comboPresupuesto.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    botonCancelar = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_añadir_var))
    botonCancelar.grid(row = row, column = 0)

    botonBuscar = Button (miFrame, text="Añadir", command=lambda:new_oportunidad(nombre=nombre.get(), ingreso=ingreso.get(), estado=comboEstado.get(), id_cliente=comboClientes, id_presupuesto=comboPresupuesto))
    botonBuscar.grid(row = row, column = 1)

def ventana_ver(bbdd):
    global ventana_ver_var
    global empresa
    empresa = bbdd
    ventana_ver_var = Toplevel()
    miFrame = Frame(ventana_ver_var, width=700, height=500)
    miFrame.pack()
    ventana_ver_var.title("Ver Oportunidad")

    row = 0

    listaContactos = select_oportunidad()
    combo = Label(miFrame, text = "ID: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    combo = ttk.Combobox(miFrame, values = listaContactos, state = "readonly")
    combo.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    global nombrever, ingresover, estadover, clientever, presupuestover
    nombrever = StringVar()
    nombrever2 = Entry(miFrame, textvariable = nombrever)
    nombrever2.grid(row = row, column = 1, padx=10, pady=10)
    nombrever2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    ingresover = StringVar()
    ingresover2 = Entry(miFrame, textvariable = ingresover)
    ingresover2.grid(row = row, column = 1, padx=10, pady=10)
    ingresover2 = Label(miFrame, text = "Ingreso esperado: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    
    row += 1

    estadover = StringVar()
    estadover2 = Entry(miFrame, textvariable = estadover)
    estadover2.grid(row = row, column = 1, padx=10, pady=10)
    estadover2 = Label(miFrame, text = "Estado: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    clientever = StringVar()
    clientever2 = Entry(miFrame, textvariable = clientever)
    clientever2.grid(row = row, column = 1, padx=10, pady=10)
    clientever2 = Label(miFrame, text = "Cliente: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    presupuestover = StringVar()
    presupuestover2 = Entry(miFrame, textvariable = presupuestover)
    presupuestover2.grid(row = row, column = 1, padx=10, pady=10)
    presupuestover2 = Label(miFrame, text = "Presupuesto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    botonCancelar = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_ver_var))
    botonCancelar.grid(row = row, column = 0)

    botonBuscar = Button (miFrame, text="Buscar", command=lambda:getSelection(combo=combo))
    botonBuscar.grid(row = row, column = 1)