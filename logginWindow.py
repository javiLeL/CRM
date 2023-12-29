from tkinter import *
import logginManager
import logginBBDDWindw

def loggin(empresa, correo_electronico, password, confimacion_password):
    if(password == confimacion_password):
        log = logginManager.log(empresa, correo_electronico, password)
        # print(log)
        if(log.isLoggin()):
            logginWindow.destroy()
            logginBBDDWindw.logginBBDD(log.empresa)

def functionLogginWindow():
    global logginWindow
    logginWindow = Tk()
    miFrame = Frame(logginWindow, width=700, height=500)
    miFrame.pack()  

    logginWindow.title("Loggin CRM")

    row = 0

    empresa = StringVar()
    empresa2 = Entry(miFrame, textvariable = empresa)
    empresa2.grid(row = row, column = 1, padx=10, pady=10)
    empresa2 = Label(miFrame, text = "Empresa: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row+=1

    correo_electronico = StringVar()
    correo_electronico2 = Entry(miFrame, textvariable = correo_electronico)
    correo_electronico2.grid(row = row, column = 1, padx=10, pady=10)
    correo_electronico2 = Label(miFrame, text = "Correo Electronico: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row+=1

    password = StringVar()
    password2 = Entry(miFrame, textvariable = password)
    password2.grid(row = row, column = 1, padx=10, pady=10)
    password2 = Label(miFrame, text = "Password: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row+=1

    confirmar_password = StringVar()
    confirmar_password2 = Entry(miFrame, textvariable = confirmar_password)
    confirmar_password2.grid(row = row, column = 1, padx=10, pady=10)
    confirmar_password2 = Label(miFrame, text = "Confirmar Password: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    row+=1

    botonCancelar = Button (miFrame, text="Cancelar", command=lambda:logginWindow.destroy())
    botonCancelar.grid(row = row, column = 0, pady=20)

    botonEnvio = Button (miFrame, text="Enviar", command=lambda:loggin(empresa=empresa.get(), correo_electronico=correo_electronico.get(), password=password.get(), confimacion_password=confirmar_password.get()))
    botonEnvio.grid(row = row, column = 1)

    logginWindow.mainloop()