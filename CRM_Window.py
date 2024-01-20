from tkinter import *
import cliente_windows
import producto_windows

def CRM_Window(bbdd):
    global CRM_Window_VAR
    global empresa
    empresa = bbdd
    CRM_Window_VAR = Tk()
    miFrame = Frame(CRM_Window_VAR, width=700, height=500)
    miFrame.pack()
    CRM_Window_VAR.title("CRM de " + empresa)

    barraMenu = Menu(CRM_Window_VAR)
    CRM_Window_VAR.config(menu=barraMenu, width="300", height="200")

    clientesMenu = Menu(barraMenu, tearoff=0)
    clientesMenu.add_command(label = "Nuevo", command=lambda:cliente_windows.ventana_añadir(empresa))
    clientesMenu.add_command(label = "Modificar", command=lambda:cliente_windows.ventana_actualizar(empresa))
    clientesMenu.add_command(label = "Ver", command=lambda:cliente_windows.ventana_ver(empresa))
    clientesMenu.add_command(label = "Borrar", command=lambda:cliente_windows.ventana_borrar(empresa))

    oportunidadMenu = Menu(barraMenu, tearoff=0)
    oportunidadMenu.add_command(label = "Nueva")
    oportunidadMenu.add_command(label = "Modificar")
    oportunidadMenu.add_command(label = "Ver")
    oportunidadMenu.add_command(label = "Borrar")

    presupuestosMenu = Menu(barraMenu, tearoff=0)
    presupuestosMenu.add_command(label = "Nuevo")
    presupuestosMenu.add_command(label = "Modificar")
    presupuestosMenu.add_command(label = "Ver")
    presupuestosMenu.add_command(label = "Borrar")

    productosMenu = Menu(barraMenu, tearoff=0)
    productosMenu.add_command(label = "Nuevo", command=lambda:producto_windows.ventana_añadir(empresa))
    productosMenu.add_command(label = "Modificar", command=lambda:producto_windows.ventana_actualizar(empresa))
    productosMenu.add_command(label = "Ver", command=lambda:producto_windows.ventana_ver(empresa))
    productosMenu.add_command(label = "Borrar")

    barraMenu.add_cascade(label = "Cliente", menu = clientesMenu)
    barraMenu.add_cascade(label = "Contactos", menu = oportunidadMenu)
    barraMenu.add_cascade(label = "Presupuestos", menu = presupuestosMenu)
    barraMenu.add_cascade(label = "Productos", menu = productosMenu)

    CRM_Window_VAR.mainloop()