from tkinter import *
import logginManager
import logginWindow

# Funcion de los botones 
def loggin(empresa, correo_electronico, password, confimacion_password):
    if(password == confimacion_password):
        log = logginManager.log(empresa, correo_electronico, password)
        # print(log)
        if(log.isLoggin()):
            print("paso")
            logginWindow.destroy()
            logginBBDD()

def cancelarLogginBBDD():
    logginToBBDD.destroy()
    logginWindow.functionLogginWindow()

def enviarLogginBBDD():
    pass

# Funcion de las ventanas
def logginBBDD():
    global logginToBBDD
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

    botonEnvio = Button (miFrame, text="Enviar")
    botonEnvio.grid(row = row, column = 1)

    logginToBBDD.mainloop()