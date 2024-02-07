# Esta pantalla es muy parecida a la de cliente porfavor revisar 
# los comentarios en el arhivo "cliente_windows.py
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def exit_btn(ventana):
    ventana.destroy()
    ventana.update()

def delete(combo):
    id = str(combo.get()).split(" ")[0]
    print(id)
    try:
        miConexion = sqlite3.connect(empresa)
        miConexion.execute("PRAGMA foreign_keys=ON")
        miConexion.executemany("DELETE FROM PRESUPUESTO WHERE id_presupuesto=?", [(str(id))])
        miConexion.commit()
        miConexion.close()
        print("Borrado")
        exit_btn(ventana_borrar_var)
    except:
        messagebox.showerror("Error", "Error al borrar el registro")
        print("Error al borrar el registro")

def getSelection(combo):
    id = str(combo.get()).split(" ")[0]
    print(id)
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT nombre, fecha_creacion, fecha_expiracion FROM PRESUPUESTO WHERE id_presupuesto=?", [(id)])
        lista = miCursor.fetchall()
    except:
        messagebox.showerror("Error", "Error al buscar los datos")
        print("Error al buscar los datos")
    print(lista)
    nombrever.set(lista[0][0])
    fecha_creacionver.set(lista[0][1])
    fecha_expiracionver.set(lista[0][2])

def update(combo, nombre, fecha_creacion, fecha_expiracion):
    id = str(combo.get()).split(" ")[0]
    if(len(str(id))==0):
        messagebox.showerror("Error", "Selecciona alguna presupuesto a modificar")
    else:
        if(len(str(nombre))==0 or len(str(fecha_creacion))==0 or len(str(fecha_expiracion))==0):
            messagebox.showerror("Error", "No se olvide de rellenar todos los datos")
        else:
            try:
                miConexion = sqlite3.connect(empresa)
                miCursor = miConexion.cursor()
                miCursor.executemany("UPDATE PRESUPUESTO SET nombre=?, fecha_creacion=?, fecha_expiracion=? WHERE id_presupuesto=?", [(str(nombre), str(fecha_creacion), str(fecha_expiracion), str(id))])
                miConexion.commit()
                miConexion.close()
                print("Actualizado")
                exit_btn(ventana_actualizar_var)
            except:
                messagebox.showerror("Error", "Error al modificar el registro")
                print("Error al modificar el registro")

def getSelectionUpdate(combo):
    id = str(combo.get()).split(" ")[0]
    print(id)
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT nombre, fecha_creacion, fecha_expiracion FROM PRESUPUESTO WHERE id_presupuesto=?", [(id)])
        lista = miCursor.fetchall()
    except:
        messagebox.showerror("Error", "Error al buscar los datos")
        print("Error al buscar los datos")
    print(lista)
    nombreact.set(lista[0][0])
    fecha_creacionact.set(lista[0][1])
    fecha_expiracionact.set(lista[0][2])

def select_presupuesto():
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT id_presupuesto, nombre FROM PRESUPUESTO")
        lista = miCursor.fetchall()
    except:
        messagebox.showerror("Error", "Error al buscar los datos")
        print("Error al buscar los datos")
    print(lista)
    return(lista)

def new_presupuesto(nombre, fecha_creacion, fecha_expiracion):
    if(len(str(nombre))==0 or len(str(fecha_creacion))==0 or len(str(fecha_expiracion))==0):
        messagebox.showerror("Error", "No se olvide de rellenar todos los datos")
    else:
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
            messagebox.showerror("Error", "Error al crear el registro")
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

def ventana_ver(bbdd):
    global ventana_ver_var
    global empresa
    empresa = bbdd
    ventana_ver_var = Toplevel()
    miFrame = Frame(ventana_ver_var, width=700, height=500)
    miFrame.pack()
    ventana_ver_var.title("Ver Presupuestos")

    row = 0

    combo = Label(miFrame, text = "ID: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    combo = ttk.Combobox(miFrame, values = select_presupuesto(), state = "readonly")
    combo.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    global nombrever, fecha_creacionver, fecha_expiracionver

    nombrever = StringVar()
    nombrever2 = Entry(miFrame, textvariable = nombrever)
    nombrever2.grid(row = row, column = 1, padx=10, pady=10)
    nombrever2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    fecha_creacionver = StringVar()
    fecha_creacionver2 = Entry(miFrame, textvariable = fecha_creacionver)
    fecha_creacionver2.grid(row = row, column = 1, padx=10, pady=10)
    fecha_creacionver2 = Label(miFrame, text = "Fecha de Creacion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    fecha_expiracionver = StringVar()
    fecha_expiracionver2 = Entry(miFrame, textvariable = fecha_expiracionver)
    fecha_expiracionver2.grid(row = row, column = 1, padx=10, pady=10)
    fecha_expiracionver2 = Label(miFrame, text = "Fecha de Expiracion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    
    row += 1

    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_ver_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Buscar", command=lambda:getSelection(combo))
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

    combo = Label(miFrame, text = "ID: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    combo = ttk.Combobox(miFrame, values = select_presupuesto(), state = "readonly")
    combo.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    global nombreact, fecha_creacionact, fecha_expiracionact

    nombreact = StringVar()
    nombreact2 = Entry(miFrame, textvariable = nombreact)
    nombreact2.grid(row = row, column = 1, padx=10, pady=10)
    nombreact2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    fecha_creacionact = StringVar()
    fecha_creacionact2 = Entry(miFrame, textvariable = fecha_creacionact)
    fecha_creacionact2.grid(row = row, column = 1, padx=10, pady=10)
    fecha_creacionact2 = Label(miFrame, text = "Fecha de Creacion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    fecha_expiracionact = StringVar()
    fecha_expiracionact2 = Entry(miFrame, textvariable = fecha_expiracionact)
    fecha_expiracionact2.grid(row = row, column = 1, padx=10, pady=10)
    fecha_expiracionact2 = Label(miFrame, text = "Fecha de Expiracion: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    
    row += 1
    
    botonCancelar = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_actualizar_var))
    botonCancelar.grid(row = row, column = 0)

    botonBuscar = Button (miFrame, text="Buscar", command=lambda:getSelectionUpdate(combo=combo))
    botonBuscar.grid(row = row, column = 1)

    row += 1

    botonEnvio = Button (miFrame, text="Actualizar", command=lambda:update(combo=combo, nombre=nombreact.get(), fecha_creacion=fecha_creacionact.get(), fecha_expiracion=fecha_expiracionact.get()))
    botonEnvio.grid(row = row, column = 1)

def ventana_borrar(bbdd):
    global ventana_borrar_var
    global empresa
    empresa = bbdd
    ventana_borrar_var = Toplevel()
    miFrame = Frame(ventana_borrar_var, width=700, height=500)
    miFrame.pack()
    ventana_borrar_var.title("Borrar Cliente")

    row = 0

    combo = Label(miFrame, text = "ID: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    combo = ttk.Combobox(miFrame, values = select_presupuesto(), state = "readonly")
    combo.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    botonCancelar = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_borrar_var))
    botonCancelar.grid(row = row, column = 0)

    botonBuscar = Button (miFrame, text="Borrar", command=lambda:delete(combo=combo))
    botonBuscar.grid(row = row, column = 1)