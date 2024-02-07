# Esta pantalla es muy parecida a la de cliente porfavor revisar 
# los comentarios en el arhivo "cliente_windows.py
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def exit_btn(ventana):
    ventana.destroy()
    ventana.update()

def delete(id_presupuesto1):
    id_presupuesto = str(id_presupuesto1.get()).split(" ")[0]
    id_producto = str(productodel.get()).split(" ")[0]
    print([(str(id_presupuesto), str(id_producto))])
    try:
        miConexion = sqlite3.connect(empresa)
        miConexion.execute("PRAGMA foreign_keys=ON")
        miConexion.executemany("DELETE FROM PEDIDO WHERE id_presupuesto=? AND id_producto=?", [(str(id_presupuesto), str(id_producto))])
        miConexion.commit()
        miConexion.close()
        print("Borrado")
        exit_btn(ventana_borrar_var)
    except:
        messagebox.showerror("Error", "Error al borrar el registro")
        print("Error al borrar el registro")

def update(id_presupuesto1, cantidad):
    id_presupuesto = str(id_presupuesto1.get()).split(" ")[0]
    id_producto = str(productoact.get()).split(" ")[0]
    if(len(str(id_presupuesto))==0 or len(str(id_producto))==0):
        messagebox.showerror("Error", "No se olvide de rellenar todos los datos")
    else:
        print([(str(id_presupuesto), str(id_producto), int(cantidad))])
        try:
            miConexion = sqlite3.connect(empresa)
            miCursor = miConexion.cursor()
            miCursor.executemany("UPDATE PEDIDO SET cantidad=? WHERE id_presupuesto=? AND id_producto=?", [(str(cantidad), str(id_presupuesto), str(id_producto))])
            miConexion.commit()
            miConexion.close()
            print("Actualizado")
            exit_btn(ventana_actualizar_var)
        except:
            messagebox.showerror("Error", "Error al crear el registro")
            print("Error al crear el registro")

def getSelectionDel(combo, miFrame):
    id = str(combo.get()).split(" ")[0]
    print(id)
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT PRODUCTO.id_producto, PRODUCTO.nombre, PEDIDO.cantidad FROM PEDIDO, PRODUCTO WHERE PEDIDO.id_producto=PRODUCTO.id_producto AND PEDIDO.id_presupuesto=?", [(id)])
        lista = miCursor.fetchall()
    except:
        messagebox.showerror("Error", "Error al buscar los datos")
        print("Error al buscar los datos")
    print(lista)
    global productodel
    productodel = ttk.Combobox(miFrame, values = lista, state = "readonly")
    productodel.grid(row = 1, column = 1, columnspan=2, sticky="e", padx=10, pady=10)
    productodel.set(lista[0])

def getSelection(combo, miFrame):
    id = str(combo.get()).split(" ")[0]
    print(id)
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT PRODUCTO.id_producto, PRODUCTO.nombre, PEDIDO.cantidad FROM PEDIDO, PRODUCTO WHERE PEDIDO.id_producto=PRODUCTO.id_producto AND PEDIDO.id_presupuesto=?", [(id)])
        lista = miCursor.fetchall()
    except:
        messagebox.showerror("Error", "Error al buscar los datos")
        print("Error al buscar los datos")
    print(lista)
    productover = ttk.Combobox(miFrame, values = lista, state = "readonly")
    productover.grid(row = 1, column = 1, columnspan=2, sticky="e", padx=10, pady=10)
    productover.set(lista[0])

def getSelectionUpdate(combo, miFrame):
    global productoact
    id = str(combo.get()).split(" ")[0]
    print(id)
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT PRODUCTO.id_producto, PRODUCTO.nombre, PEDIDO.cantidad FROM PEDIDO, PRODUCTO WHERE PEDIDO.id_producto=PRODUCTO.id_producto AND PEDIDO.id_presupuesto=?", [(id)])
        lista = miCursor.fetchall()
    except:
        messagebox.showerror("Error", "Error al buscar los datos")
        print("Error al buscar los datos")
    print(lista)
    productoact = ttk.Combobox(miFrame, values = lista, state = "readonly")
    productoact.grid(row = 1, column = 1, columnspan=2, sticky="e", padx=10, pady=10)
    productoact.set(lista[0])

def new_pedido(id_presupuesto1, id_producto1, cantidad):
    id_presupuesto = str(id_presupuesto1.get()).split(" ")[0]
    id_producto = str(id_producto1.get()).split(" ")[0]
    if(len(str(id_presupuesto))==0 or len(str(id_producto))==0):
        messagebox.showerror("Error", "No se olvide de rellenar todos los datos")
    else:
        # print([(str(id_presupuesto), str(id_producto), int(cantidad))])
        try:
            miConexion = sqlite3.connect(empresa)
            miConexion.execute("PRAGMA foreign_keys=ON")
            miConexion.executemany("INSERT INTO PEDIDO (id_presupuesto, id_producto, cantidad) VALUES (?, ?, ?)", [(str(id_presupuesto), str(id_producto), int(cantidad))])
            miConexion.commit()
            miConexion.close()
            print("Introducido")
            exit_btn(ventana_añadir_var)
        except:
            messagebox.showerror("Error", "Error al crear el registro")
            print("Error al crear el registro")

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

def select_producto():
    lista = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT id_producto, nombre FROM PRODUCTO")
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
    ventana_añadir_var.title("Nuevo Pedido")

    row = 0

    presupuesto = Label(miFrame, text = "Presupuesto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    presupuesto = ttk.Combobox(miFrame, values = select_presupuesto(), state = "readonly")
    presupuesto.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    producto = Label(miFrame, text = "Producto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    producto = ttk.Combobox(miFrame, values = select_producto(), state = "readonly")
    producto.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    cantidad = StringVar()
    cantidad2 = Entry(miFrame, textvariable = cantidad)
    cantidad2.grid(row = row, column = 1, padx=10, pady=10)
    cantidad2 = Label(miFrame, text = "Cantidad: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_añadir_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Enviar", command=lambda:new_pedido(id_presupuesto1=presupuesto, id_producto1=producto, cantidad=cantidad.get()))
    botonEnvio.grid(row = row, column = 1)

def ventana_ver(bbdd):
    global ventana_ver_var, productover
    global empresa
    empresa = bbdd
    ventana_ver_var = Toplevel()
    miFrame = Frame(ventana_ver_var, width=700, height=500)
    miFrame.pack()
    ventana_ver_var.title("Ver Pedidos")

    row = 0

    presupuesto = Label(miFrame, text = "Presupuesto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    presupuesto = ttk.Combobox(miFrame, values = select_presupuesto(), state = "readonly")
    presupuesto.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    Label(miFrame, text = "Producto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    productover = ttk.Combobox(miFrame, values = [" "], state = "readonly")
    productover.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_ver_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Buscar", command=lambda:getSelection(presupuesto, miFrame))
    botonEnvio.grid(row = row, column = 1)

def ventana_actualizar(bbdd):
    global ventana_actualizar_var
    global empresa
    empresa = bbdd
    ventana_actualizar_var = Toplevel()
    miFrame = Frame(ventana_actualizar_var, width=700, height=500)
    miFrame.pack()
    ventana_actualizar_var.title("Actualizar Pedido")

    row = 0

    presupuesto = Label(miFrame, text = "Presupuesto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    presupuesto = ttk.Combobox(miFrame, values = select_presupuesto(), state = "readonly")
    presupuesto.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    Label(miFrame, text = "Producto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    productoact = ttk.Combobox(miFrame, values = [" "], state = "readonly")
    productoact.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    cantidad = StringVar()
    cantidad2 = Entry(miFrame, textvariable = cantidad)
    cantidad2.grid(row = row, column = 1, padx=10, pady=10)
    cantidad2 = Label(miFrame, text = "Cantidad: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    botonEnvio = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_actualizar_var))
    botonEnvio.grid(row = row, column = 0)

    botonEnvio = Button (miFrame, text="Buscar", command=lambda:getSelectionUpdate(presupuesto, miFrame))
    botonEnvio.grid(row = row, column = 1)

    row += 1

    botonEnvio = Button (miFrame, text="Actualizar", command=lambda:update(id_presupuesto1=presupuesto, id_producto1=productoact, cantidad=cantidad.get()))
    botonEnvio.grid(row = row, column = 1)

def ventana_borrar(bbdd):
    global ventana_borrar_var
    global empresa
    empresa = bbdd
    ventana_borrar_var = Toplevel()
    miFrame = Frame(ventana_borrar_var, width=700, height=500)
    miFrame.pack()
    ventana_borrar_var.title("Borrar Presupuesto")

    row = 0

    presupuesto = Label(miFrame, text = "Presupuesto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    presupuesto = ttk.Combobox(miFrame, values = select_presupuesto(), state = "readonly")
    presupuesto.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    productodel = Label(miFrame, text = "Producto: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    productodel = ttk.Combobox(miFrame, values = [" "], state = "readonly")
    productodel.grid(row = row, column = 1, columnspan=2, sticky="e", padx=10, pady=10)

    row += 1

    botonCancelar = Button (miFrame, text="Cancelar", command=lambda:exit_btn(ventana_borrar_var))
    botonCancelar.grid(row = row, column = 0)

    botonBuscar = Button (miFrame, text="Buscar", command=lambda:getSelectionDel(combo=presupuesto, miFrame=miFrame))
    botonBuscar.grid(row = row, column = 1)

    row += 1

    botonBuscar = Button (miFrame, text="Borrar", command=lambda:delete(id_presupuesto1=presupuesto))
    botonBuscar.grid(row = row, column = 1)