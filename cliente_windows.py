from tkinter import *
from tkinter import ttk
import sqlite3

def p(combo):
    id = str(combo.get())
    id = id.split(" ")
    print(id[0])


def exit_btn(ventana):
    ventana.destroy()
    ventana.update()

def new_cliente(nombre, calle, codigo_postal, ciudad, pais, telefono, persona_de_contacto, correo_electronico, iva):
    print([(str(nombre), str(calle), str(codigo_postal), str(ciudad), str(pais), str(telefono), str(persona_de_contacto), str(correo_electronico))])
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.executemany("INSERT INTO CLIENTE (nombre, calle, codigo_postal, ciudad, pais, telefono, persona_de_contacto, correo_electronico, iva) VALUES (?,?,?,?,?,?,?,?,?)", [(str(nombre), str(calle), str(codigo_postal), str(ciudad), str(pais), str(telefono), str(persona_de_contacto), str(correo_electronico), int(iva))])
        miConexion.commit()
        miConexion.close()
        print("Introducido")
        exit_btn()
    except:
        print("Error al crear el registro")

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

def ventana_añadir(bbdd):
    global ventana_añadir_var
    global empresa
    empresa = bbdd
    ventana_añadir_var = Toplevel()
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
    iva2 = Label(miFrame, text = "IVA: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_añadir_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Enviar", command=lambda:new_cliente(nombre=nombre.get(), calle=calle.get(), codigo_postal=codigo_postal.get(), ciudad=ciudad.get(), pais=pais.get(), telefono=telefono.get(), persona_de_contacto=persona_contacto.get(), correo_electronico=correo_electronico.get(), iva=iva.get()))
    botonEnvio.grid(row = row, column = 1)

def ventana_ver(bbdd):
    global ventana_ver_var
    global empresa
    empresa = bbdd
    ventana_ver_var = Toplevel()
    miFrame = Frame(ventana_ver_var, width=700, height=500)
    miFrame.pack()
    ventana_ver_var.title("Ver Clientes")
    
    row = 0

    listaContactos = select_clientes()
    combo = Label(miFrame, text = "ID: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    combo = ttk.Combobox(miFrame, values = listaContactos, state = "readonly")
    combo.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    print(combo.get())

    row += 1

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
    iva2 = Label(miFrame, text = "IVA: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_ver_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Buscar", command=lambda:p(combo=combo))
    botonEnvio.grid(row = row, column = 1)