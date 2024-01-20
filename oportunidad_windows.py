from tkinter import *
from tkinter import ttk
import sqlite3

def exit_btn(ventana):
    ventana.destroy()
    ventana.update()

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
    ventana_añadir_var.title("Nuevo Oportunidad")

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