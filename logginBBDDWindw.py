import sqlite3
from tkinter import *
import CRM_Window
import logginWindow

empresa = None

def cancelarLogginBBDD():
    logginToBBDD.destroy()
    logginWindow.functionLogginWindow()

def enviarLogginBBDD(name, passwd):
    try:
        miConexion = sqlite3.connect(empresa)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM USUARIOS WHERE nombre=?", [(name)])
        lista = miCursor.fetchall()
        # print(lista)
    except:
        print("Error al buscar los datos")

    if(lista[0][1]==passwd):
        logginToBBDD.destroy()
        CRM_Window.CRM_Window(empresa)

def logginBBDD(bbdd):
    global logginToBBDD
    global empresa
    if(bbdd!=None):
        empresa = bbdd.upper()
    logginToBBDD = Tk()
    miFrame = Frame(logginToBBDD, width=700, height=500)
    miFrame.pack()
    logginToBBDD.title("Loggin BBDD")
    
    row = 0

    name = StringVar()
    name2 = Entry(miFrame, textvariable = name)
    name2.grid(row = row, column = 1, padx=10, pady=10)
    name2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)
    
    row += 1

    password = StringVar()
    password2 = Entry(miFrame, textvariable = password)
    password2.grid(row = row, column = 1, padx=10, pady=10)
    password2 = Label(miFrame, text = "Password: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row += 1

    botonCancelar = Button (miFrame, text="Cancelar", command=cancelarLogginBBDD)
    botonCancelar.grid(row = row, column = 0, pady=20)

    botonEnvio = Button (miFrame, text="Enviar", command=lambda:enviarLogginBBDD(str(name.get()), str(password.get())))
    botonEnvio.grid(row = row, column = 1)

    logginToBBDD.mainloop()