from tkinter import *
from tkinter import ttk
import sqlite3

def getSelection(combo):
    id = str(combo.get()).split(" ")[0]
    print(id)
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT nombre, calle, codigo_postal, ciudad, pais, telefono, persona_de_contacto, correo_electronico, iva FROM CLIENTE WHERE id_cliente=?", [(id)])
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    print(lista)
    nombrever.set(lista[0][0])
    callever.set(lista[0][1])
    codigo_postalver.set(lista[0][2])
    ciudadver.set(lista[0][3])
    paisver.set(lista[0][4])
    telefonover.set(lista[0][5])
    persona_contactover.set(lista[0][6])
    correo_electronicover.set(lista[0][7])
    ivaver.set(lista[0][8])

def update(combo, nombre, calle, codigo_postal, ciudad, pais, telefono, persona_de_contacto, correo_electronico, iva):
    id = str(combo.get()).split(" ")[0]
    print((str(nombre), str(calle), str(codigo_postal), str(ciudad), str(pais), str(telefono), str(persona_de_contacto), str(correo_electronico), int(iva), int(id)))
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.executemany("UPDATE CLIENTE SET nombre=?, calle=?, codigo_postal=?, ciudad=?, pais=?, telefono=?, persona_de_contacto=?, correo_electronico=?, iva=? WHERE id_cliente=?", [(str(nombre), str(calle), str(codigo_postal), str(ciudad), str(pais), str(telefono), str(persona_de_contacto), str(correo_electronico), str(iva), str(id))])
        miConexion.commit()
        miConexion.close()
        print("Actualizado")
        exit_btn(ventana_actualizar_var)
    except:
        print("Error al modificar el registro")

def getSelectionUpdate(combo):
    id = str(combo.get()).split(" ")[0]
    print(id)
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT nombre, calle, codigo_postal, ciudad, pais, telefono, persona_de_contacto, correo_electronico, iva FROM CLIENTE WHERE id_cliente=?", [(id)])
        lista = miCursor.fetchall()
    except:
        print("Error al buscar los datos")
    print(lista)
    nombreact.set(lista[0][0])
    calleact.set(lista[0][1])
    codigo_postalact.set(lista[0][2])
    ciudadact.set(lista[0][3])
    paisact.set(lista[0][4])
    telefonoact.set(lista[0][5])
    persona_contactoact.set(lista[0][6])
    correo_electronicoact.set(lista[0][7])
    ivaact.set(lista[0][8])

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
        exit_btn(ventana_añadir_var)
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

    row += 1

    global nombrever, callever, codigo_postalver, ciudadver, paisver, telefonover, persona_contactover, correo_electronicover, ivaver
    nombrever = StringVar()
    nombrever2 = Entry(miFrame, textvariable = nombrever)
    nombrever2.grid(row = row, column = 1, padx=10, pady=10)
    nombrever2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    callever = StringVar()
    callever2 = Entry(miFrame, textvariable = callever)
    callever2.grid(row = row, column = 1, padx=10, pady=10)
    callever2 = Label(miFrame, text = "Calle: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    codigo_postalver = StringVar()
    codigo_postalver2 = Entry(miFrame, textvariable = codigo_postalver)
    codigo_postalver2.grid(row = row, column = 1, padx=10, pady=10)
    codigo_postalver2 = Label(miFrame, text = "Codigo Postal: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    ciudadver = StringVar()
    ciudadver2 = Entry(miFrame, textvariable = ciudadver)
    ciudadver2.grid(row = row, column = 1, padx=10, pady=10)
    ciudadver2 = Label(miFrame, text = "Ciudad: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    paisver = StringVar()
    paisver2 = Entry(miFrame, textvariable = paisver)
    paisver2.grid(row = row, column = 1, padx=10, pady=10)
    paisver2 = Label(miFrame, text = "Pais: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    telefonover = StringVar()
    telefonover2 = Entry(miFrame, textvariable = telefonover)
    telefonover2.grid(row = row, column = 1, padx=10, pady=10)
    telefonover2 = Label(miFrame, text = "Telefono: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    persona_contactover = StringVar()
    persona_contactover2 = Entry(miFrame, textvariable = persona_contactover)
    persona_contactover2.grid(row = row, column = 1, padx=10, pady=10)
    persona_contactover2 = Label(miFrame, text = "Persona de Contacto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    correo_electronicover = StringVar()
    correo_electronicover2 = Entry(miFrame, textvariable = correo_electronicover)
    correo_electronicover2.grid(row = row, column = 1, padx=10, pady=10)
    correo_electronicover2 = Label(miFrame, text = "Correo Electronico: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    ivaver = StringVar()
    iva2ver = Entry(miFrame, textvariable = ivaver)
    iva2ver.grid(row = row, column = 1, padx=10, pady=10)
    iva2ver = Label(miFrame, text = "IVA: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    botonCancelar = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_ver_var))
    botonCancelar.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Buscar", command=lambda:getSelection(combo=combo))
    botonEnvio.grid(row = row, column = 1)

def ventana_actualizar(bbdd):
    global ventana_actualizar_var
    global empresa
    empresa = bbdd
    ventana_actualizar_var = Toplevel()
    miFrame = Frame(ventana_actualizar_var, width=700, height=500)
    miFrame.pack()
    ventana_actualizar_var.title("Actualizar Cliente")
    
    row = 0

    listaContactos = select_clientes()
    combo = Label(miFrame, text = "ID: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    combo = ttk.Combobox(miFrame, values = listaContactos, state = "readonly")
    combo.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    global nombreact, calleact, codigo_postalact, ciudadact, paisact, telefonoact, persona_contactoact, correo_electronicoact, ivaact
    nombreact = StringVar()
    nombreact2 = Entry(miFrame, textvariable = nombreact)
    nombreact2.grid(row = row, column = 1, padx=10, pady=10)
    nombreact2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    calleact = StringVar()
    calleact2 = Entry(miFrame, textvariable = calleact)
    calleact2.grid(row = row, column = 1, padx=10, pady=10)
    calleact2 = Label(miFrame, text = "Calle: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    codigo_postalact = StringVar()
    codigo_postalact2 = Entry(miFrame, textvariable = codigo_postalact)
    codigo_postalact2.grid(row = row, column = 1, padx=10, pady=10)
    codigo_postalact2 = Label(miFrame, text = "Codigo Postal: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    ciudadact = StringVar()
    ciudadact2 = Entry(miFrame, textvariable = ciudadact)
    ciudadact2.grid(row = row, column = 1, padx=10, pady=10)
    ciudadact2 = Label(miFrame, text = "Ciudad: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    paisact = StringVar()
    paisact2 = Entry(miFrame, textvariable = paisact)
    paisact2.grid(row = row, column = 1, padx=10, pady=10)
    paisact2 = Label(miFrame, text = "Pais: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    telefonoact = StringVar()
    telefonoact2 = Entry(miFrame, textvariable = telefonoact)
    telefonoact2.grid(row = row, column = 1, padx=10, pady=10)
    telefonoact2 = Label(miFrame, text = "Telefono: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    persona_contactoact = StringVar()
    persona_contactoact2 = Entry(miFrame, textvariable = persona_contactoact)
    persona_contactoact2.grid(row = row, column = 1, padx=10, pady=10)
    persona_contactoact2 = Label(miFrame, text = "Persona de Contacto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    correo_electronicoact = StringVar()
    correo_electronicoact2 = Entry(miFrame, textvariable = correo_electronicoact)
    correo_electronicoact2.grid(row = row, column = 1, padx=10, pady=10)
    correo_electronicoact2 = Label(miFrame, text = "Correo Electronico: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    ivaact = StringVar()
    ivaact2 = Entry(miFrame, textvariable = ivaact)
    ivaact2.grid(row = row, column = 1, padx=10, pady=10)
    ivaact2 = Label(miFrame, text = "IVA: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    botonCancelar = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_actualizar_var))
    botonCancelar.grid(row = row, column = 0)

    botonBuscar = Button (miFrame, text="Buscar", command=lambda:getSelectionUpdate(combo=combo))
    botonBuscar.grid(row = row, column = 1)

    row += 1

    botonEnvio = Button (miFrame, text="Actualizar", command=lambda:update(combo=combo, nombre=nombreact.get(), calle=calleact.get(), codigo_postal=codigo_postalact.get(), ciudad=ciudadact.get(), pais=paisact.get(), telefono=telefonoact.get(), persona_de_contacto=persona_contactoact.get(), correo_electronico=correo_electronicoact.get(), iva=ivaact.get()))
    botonEnvio.grid(row = row, column = 1)