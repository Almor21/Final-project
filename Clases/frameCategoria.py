import tkinter as tk

class Color:
    def __init__(self):
        self.AZUL = "#2155CD"
        self.BLANCO = "#E8F9FD"

class pn_Categoria(tk.Frame):
    def __init__(self, master, atAgregar, Cat):
        self.cl = Color()
        self.Cat = Cat
        self.Nombre = Cat.Nombre
        self.Dinero = Cat.Saldo
        tk.Frame.__init__(self, master)
        self.config(width=170, height=100, bg=self.cl.BLANCO, bd=2, relief="groove")
        self.parent = master

        self.atAgregar = atAgregar
        self.initcomponents()

    def initcomponents(self):
        tk.Label(self, text=self.Nombre, bg=self.cl.BLANCO).place(x=10, y=10)

        self.etq_Dinero = tk.Label(self, text="Dinero: " + str(self.Dinero), bg=self.cl.BLANCO)
        self.etq_Dinero.place(x=10, y=35)

        self.bt_Cal = tk.Button(self, text="Calendario")
        self.bt_Cal.place(x=10, y=60)

        self.bt_Agr = tk.Button(self, text="Agregar", command=self.ActionAgregar)
        self.bt_Agr.place(x=90, y=60)

    def ActionAgregar(self):
        self.atAgregar(self.Nombre)
        self.etq_Dinero.config(text="Dinero: " + str(self.Cat.Saldo))
