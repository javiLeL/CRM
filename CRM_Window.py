from tkinter import *

def CRM_Window():
    global CRM_Window_VAR
    CRM_Window_VAR = Tk()
    miFrame = Frame(CRM_Window_VAR, width=700, height=500)
    miFrame.pack()
    CRM_Window_VAR.title("CRM")
    
    row = 0
    
    empresa = StringVar()
    empresa2 = Entry(miFrame, textvariable = empresa)
    empresa2.grid(row = row, column = 1, padx=10, pady=10)
    empresa2 = Label(miFrame, text = "Empresa: ").grid(row = row, column = 0, sticky="e", padx=10, pady=10)

    CRM_Window_VAR.mainloop()