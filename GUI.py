import sqlite3
from textwrap import wrap
from tkinter import *
import port_5 
class Application:
    def __init__(self, master=None):
        self.containerTitulo = Frame(master)
        self.containerTitulo.pack()

        self.containerCompliance = Frame(master)
        self.containerCompliance.pack()

        self.titulo = Label(self.containerTitulo,text='Testes de compliance da Total Health',bg = '#000000')
        self.titulo['font'] = ("Consolas", "15", "bold")
        self.titulo.pack()


root = Tk()
Application(root)
root.mainloop()