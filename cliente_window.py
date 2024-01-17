import tkinter as tk
from tkinter import *

def ventana_añadir():
    global ventana_añadir_var
    ventana_añadir_var = tk.Toplevel()
    miFrame = Frame(ventana_añadir_var, width=700, height=500)
    miFrame.pack()
    ventana_añadir_var.title("Nuevo Cliente")