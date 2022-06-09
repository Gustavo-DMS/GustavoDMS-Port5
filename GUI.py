from ast import While
import sqlite3
from tkinter import *

from sqlalchemy import false
# import port_5 
class Application:
    def __init__(self, master):
        self.child_window = None
        self.master = master
        self.toplevels = 0
        self.containerTitulo = Frame(master)
        self.containerTitulo.pack()

        self.containerCompliance = Frame(master)
        self.containerCompliance.pack()

        self.titulo = Label(self.containerTitulo,text='Testes de compliance da Total Health')
        self.titulo['font'] = ("Consolas", "15", "bold")
        self.titulo.pack()

        self.botao1 = Button(self.containerCompliance,text="omegalol")
        self.botao1['command'] = self.janelaNova
        self.botao1.pack()

        self.botao2 = Button(self.containerCompliance,text="omegalol")
        self.botao2['command'] = self.janelaNova2
        self.botao2.pack()
       

    def janelaNova(self):
        if not self.child_window:
            nova = Toplevel(self.master)
            self.child_window = nova
            self.containerTitulo2 = Frame(nova)
            self.containerTitulo2.pack()

            self.containerCompliance2 = Frame(nova)
            self.containerCompliance2.pack()

            self.titulo2 = Label(self.containerTitulo2,text='janela2')
            self.titulo2['font'] = ("Consolas", "15", "bold")
            self.titulo2.pack()

            self.botao1 = Button(self.containerCompliance2,text="omegalol")
                
            self.botao1.pack()

            def doSomething():
                nova.destroy()
                self.child_window = None

            nova.protocol('WM_DELETE_WINDOW', doSomething)

            
    def janelaNova2(self):
        if not self.child_window:
            nova2 = Toplevel(self.master)
            self.child_window = nova2
            self.containerTitulo2 = Frame(nova2)
            self.containerTitulo2.pack()

            self.containerCompliance2 = Frame(nova2)
            self.containerCompliance2.pack()

            self.titulo2 = Label(self.containerTitulo2,text='janela2')
            self.titulo2['font'] = ("Consolas", "15", "bold")
            self.titulo2.pack()

            self.botao1 = Button(self.containerCompliance2,text="omegalol")
                
            self.botao1.pack()

            def doSomething():
                nova.destroy()
                self.child_window = None

            nova.protocol('WM_DELETE_WINDOW', doSomething)


root = Tk()
Application(root)
root.mainloop()