from tkinter import *

def CRM_Window():
    global CRM_Window_VAR
    CRM_Window_VAR = Tk()
    miFrame = Frame(CRM_Window_VAR, width=700, height=500)
    miFrame.pack()
    CRM_Window_VAR.title("CRM")

    barraMenu = Menu(CRM_Window_VAR)
    CRM_Window_VAR.config(menu=barraMenu, width="300", height="200")

    clientesMenu = Menu(barraMenu, tearoff=0)
    clientesMenu.add_command(label = "Nuevo")
    clientesMenu.add_command(label = "Modificar")
    clientesMenu.add_command(label = "Ver")
    clientesMenu.add_command(label = "Borrar")

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
    productosMenu.add_command(label = "Nuevo")
    productosMenu.add_command(label = "Modificar")
    productosMenu.add_command(label = "Ver")
    productosMenu.add_command(label = "Borrar")

    barraMenu.add_cascade(label = "Cliente", menu = clientesMenu)
    barraMenu.add_cascade(label = "Contactos", menu = oportunidadMenu)
    barraMenu.add_cascade(label = "Presupuestos", menu = presupuestosMenu)
    barraMenu.add_cascade(label = "Productos", menu = productosMenu)

    CRM_Window_VAR.mainloop()