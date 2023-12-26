from tkinter import *
from tkinter import messagebox
import logginManager

root = Tk()
miFrame = Frame(root, width=700, height=500)
miFrame.pack()

root.title("Loggin CRM")

row = 0

empresa = StringVar()
empresa2 = Entry(miFrame, textvariable = empresa)
empresa2.grid(row = row, column = 1, padx=10, pady=10)
empresa2 = Label(miFrame, text = "Empresa: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

row+=1

nombre = StringVar()
nombre2 = Entry(miFrame, textvariable = nombre)
nombre2.grid(row = row, column = 1, padx=10, pady=10)
nombre2 = Label(miFrame, text = "Nombre: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

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

botonCancelar = Button (miFrame, text="Cancelar")
botonCancelar.grid(row = row, column = 0, pady=20)

botonEnvio = Button (miFrame, text="Enviar")
botonEnvio.grid(row = row, column = 1)

root.mainloop()