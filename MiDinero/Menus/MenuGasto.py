import tkinter as tk
import tkinter.messagebox
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
        tk.Label(self, text="Tipo: ").grid(row=0, column=0, padx=10, pady=10)
        self.cb_Tipo = ttk.Combobox(self, width=15, state="readonly", values=["Ingreso", "Gasto"])
        self.cb_Tipo.current(0)
        self.cb_Tipo.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

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

    def ActionBt(self) -> None:
        try:
            tipo = self.cb_Tipo.get()
            val = int(self.tf_Valor.get())
            fecha = Date(int(self.tf_FAño.get()), int(self.tf_FMes.get()), int(self.tf_FDia.get()))
            des = self.ta.get("1.0", "end")
        except ValueError:
            tkinter.messagebox.showinfo(message="Datos Invalidos")
            return

        if tipo == "Ingreso":
            ing = Ingreso(val, fecha, des)
            self.parent.nwIngreso(ing)
        elif tipo == "Gasto":
            gas = Gasto(val, fecha, des)
            if val <= self.parent.Saldo:
                self.parent.nwGasto(gas)
            else:
                tkinter.messagebox.showinfo(message="Saldo Insuficiente")

class FormMenu:
    def __init__(self, parent, tkmaster, title: str):
        root = tk.Toplevel(tkmaster)
        root.title(title)
        root.update()
        app = UI(root, parent)
        root.mainloop()
