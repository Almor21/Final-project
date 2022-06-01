import tkinter as tk
from tkinter import ttk
from Clases.Datos import *

class UI(tk.Frame):
    def __init__(self, master, parent):
        tk.Frame.__init__(self, master)
        self.config(width=master.winfo_width(), height=master.winfo_height())
        self.tkmaster = master
        self.parent = parent
        self.grid()
        self.update()

        self.initcomponents()

    def initcomponents(self):
        listCat = self.parent.getListCategorias()
        values = []
        for c in listCat:
            values.append(c.Nombre)

        tk.Label(self, text="Categoria: ").grid(row=0, column=0, padx=10, pady=10)
        self.cb_Cat = ttk.Combobox(self, width=15, state="readonly", values=values)
        self.cb_Cat.current(0)
        self.cb_Cat.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        tk.Label(self, text="Valor: ").grid(row=1, column=0, padx=10, pady=10)
        self.tf_Valor = tk.Entry(self, width=18)
        self.tf_Valor.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        tk.Label(self, text="Fecha: ").grid(row=2, column=0, padx=10, pady=10)
        self.tf_FDia = tk.Entry(self, width=3)
        self.tf_FMes = tk.Entry(self, width=3)
        self.tf_FAño = tk.Entry(self, width=6)
        self.tf_FDia.grid(row=2, column=1, pady=10)
        self.tf_FMes.grid(row=2, column=2, pady=10)
        self.tf_FAño.grid(row=2, column=3, pady=10)

        tk.Label(self, text="Descripcion: ").grid(row=3, column=0, padx=10, pady=10)
        self.ta = tk.Text(self, width=18, height=5)
        self.ta.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

        self.bt = tk.Button(self, text="Agregar", command=self.ActionBt)
        self.bt.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

    def ActionBt(self):
        cat = self.cb_Cat.get()
        val = int(self.tf_Valor.get())
        fecha = Date(int(self.tf_FAño.get()), int(self.tf_FMes.get()), int(self.tf_FDia.get()))
        des = self.ta.get("1.0","end")

        mov = Movimiento(cat, val, fecha, des)
        self.parent.nwMovimiento(mov)

class FormMenu:
    def __init__(self, parent, tkmaster, title: str):
        root = tk.Toplevel(tkmaster)
        root.title(title)
        root.update()
        app = UI(root, parent)
        root.mainloop()
