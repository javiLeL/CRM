from tkinter import *
from tkinter import ttk
import sqlite3
import cliente_windows
import producto_windows
import oportunidad_windows
import presupuesto_windows
import pedidos_windows
# Este metodod actualiza los campos de la PIPELINES de CRM
def updateCampos(miFrame):
    listaNuevo = []
    listaCalificado = []
    listaPropuesta = []
    listaGanado = []
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT id_oportunidad, nombre FROM OPORTUNIDAD WHERE estado=?", [(str("NUEVO"))])
        listaNuevo = miCursor.fetchall()
        miCursor.execute("SELECT id_oportunidad, nombre FROM OPORTUNIDAD WHERE estado=?", [(str("CALIFICADO"))])
        listaCalificado = miCursor.fetchall()
        miCursor.execute("SELECT id_oportunidad, nombre FROM OPORTUNIDAD WHERE estado=?", [(str("PROPUESTA"))])
        listaPropuesta = miCursor.fetchall()
        miCursor.execute("SELECT id_oportunidad, nombre FROM OPORTUNIDAD WHERE estado=?", [(str("GANADO"))])
        listaGanado = miCursor.fetchall()
    except:
        print("Error al buscar los datos")

    comboNuevo = Label(miFrame, text = "Nuevos").grid(row = 0, column = 1, sticky="e", padx=10, pady=10)
    comboNuevo = ttk.Combobox(miFrame, values = listaNuevo, state = "readonly")
    comboNuevo.grid(row = 1, column = 0, columnspan=3, sticky="e", padx=10, pady=10)

    comboCalificado = Label(miFrame, text = "Calificados").grid(row = 0, column = 4, sticky="e", padx=10, pady=10)
    comboCalificado = ttk.Combobox(miFrame, values = listaCalificado, state = "readonly")
    comboCalificado.grid(row = 1, column = 4, columnspan=3, sticky="e", padx=10, pady=10)

    comboPropuesta = Label(miFrame, text = "Propuesta").grid(row = 0, column = 7, sticky="e", padx=10, pady=10)
    comboPropuesta = ttk.Combobox(miFrame, values = listaPropuesta, state = "readonly")
    comboPropuesta.grid(row = 1, column = 7, columnspan=3, sticky="e", padx=10, pady=10)

    comboGanado = Label(miFrame, text = "Ganado").grid(row = 0, column = 10, sticky="e", padx=10, pady=10)
    comboGanado = ttk.Combobox(miFrame, values = listaGanado, state = "readonly")
    comboGanado.grid(row = 1, column = 10, columnspan=3, sticky="e", padx=10, pady=10)
# Este metodo lanza la ventana que sustenta todo el CRM
def CRM_Window(bbdd):
    global CRM_Window_VAR, empresa
    empresa = bbdd
    CRM_Window_VAR = Tk()
    miFrame = Frame(CRM_Window_VAR, width=700, height=500)
    CRM_Window_VAR.geometry("700x500")
    miFrame.pack()
    CRM_Window_VAR.title("CRM de " + empresa)

    botonBorrar = Button (text="Actualizar", command=lambda:updateCampos(miFrame=miFrame))
    botonBorrar.place(x=600, y=450)

    updateCampos(miFrame=miFrame)

    barraMenu = Menu(CRM_Window_VAR)
    CRM_Window_VAR.config(menu=barraMenu, width="300", height="200")

    clientesMenu = Menu(barraMenu, tearoff=0)
    clientesMenu.add_command(label = "Nuevo", command=lambda:cliente_windows.ventana_añadir(empresa))
    clientesMenu.add_command(label = "Modificar", command=lambda:cliente_windows.ventana_actualizar(empresa))
    clientesMenu.add_command(label = "Ver", command=lambda:cliente_windows.ventana_ver(empresa))
    clientesMenu.add_command(label = "Borrar", command=lambda:cliente_windows.ventana_borrar(empresa))

    oportunidadMenu = Menu(barraMenu, tearoff=0)
    oportunidadMenu.add_command(label = "Nueva", command=lambda:oportunidad_windows.ventana_añadir(empresa))
    oportunidadMenu.add_command(label = "Modificar", command=lambda:oportunidad_windows.ventana_actualizar(empresa))
    oportunidadMenu.add_command(label = "Ver", command=lambda:oportunidad_windows.ventana_ver(empresa))
    oportunidadMenu.add_command(label = "Borrar", command=lambda:oportunidad_windows.ventana_borrar(empresa))

    presupuestosMenu = Menu(barraMenu, tearoff=0)
    presupuestosMenu.add_command(label = "Nuevo", command=lambda:presupuesto_windows.ventana_añadir(empresa))
    presupuestosMenu.add_command(label = "Modificar", command=lambda:presupuesto_windows.ventana_actualizar(empresa))
    presupuestosMenu.add_command(label = "Ver", command=lambda:presupuesto_windows.ventana_ver(empresa))
    presupuestosMenu.add_command(label = "Borrar", command=lambda:presupuesto_windows.ventana_borrar(empresa))

    productosMenu = Menu(barraMenu, tearoff=0)
    productosMenu.add_command(label = "Nuevo", command=lambda:producto_windows.ventana_añadir(empresa))
    productosMenu.add_command(label = "Modificar", command=lambda:producto_windows.ventana_actualizar(empresa))
    productosMenu.add_command(label = "Ver", command=lambda:producto_windows.ventana_ver(empresa))
    productosMenu.add_command(label = "Borrar", command=lambda:producto_windows.ventana_borrar(empresa))

    pedidosMenu = Menu(barraMenu, tearoff=0)
    pedidosMenu.add_command(label = "Nuevo", command=lambda:pedidos_windows.ventana_añadir(empresa))
    pedidosMenu.add_command(label = "Modificar", command=lambda:pedidos_windows.ventana_actualizar(empresa))
    pedidosMenu.add_command(label = "Ver", command=lambda:pedidos_windows.ventana_ver(empresa))
    pedidosMenu.add_command(label = "Borrar", command=lambda:pedidos_windows.ventana_borrar(empresa))

    barraMenu.add_cascade(label = "Cliente", menu = clientesMenu)
    barraMenu.add_cascade(label = "Oportunidad", menu = oportunidadMenu)
    barraMenu.add_cascade(label = "Presupuestos", menu = presupuestosMenu)
    barraMenu.add_cascade(label = "Productos", menu = productosMenu)
    barraMenu.add_cascade(label = "Pedidos", menu = pedidosMenu)

    CRM_Window_VAR.mainloop()