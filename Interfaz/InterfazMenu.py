import os.path
import pickle
import tkinter as tk

from Interfaz import InterfazCategorias, InterfazGHormiga
from framePrincipal import Principal
from Menus import MenuRegistro
from Clases.Datos import Color

class UI(tk.Frame):
    def __init__(self, parent: Principal, tkmaster: tk.Tk):
        color = Color()

        tk.Frame.__init__(self, tkmaster)
        self.config(width=tkmaster.winfo_width(), bg=color.BLANCO)
        self.pack(fill="y", expand=True)
        self.update()

        self.tkmaster = tkmaster
        self.parent = parent
        self.parent.DesactivarVolver()

        self.initcomponents()

    def initcomponents(self):
        self.bt_AbCat = tk.Button(self, text="Categorias", command=self.ActionAbCat)
        self.bt_AbCat.config(width=30, height=2, font=("Arial", 14))
        self.bt_AbCat.place(x=130, y=60)

        self.bt_AbGH = tk.Button(self, text="Gastos Hormiga", command=self.ActionAbGH)
        self.bt_AbGH.config(width=30, height=2, font=("Arial", 14))
        self.bt_AbGH.place(x=130, y=180)

        self.bt_AbRG = tk.Button(self, text="Registro de Gastos", command=self.ActionAbRG)
        self.bt_AbRG.config(width=30, height=2, font=("Arial", 14))
        self.bt_AbRG.place(x=130, y=300)

    def ActionAbCat(self):
        self.destroy()
        InterfazCategorias.Iniciar(self.parent, self.tkmaster)

    def ActionAbGH(self):
        InterfazGHormiga.FormMenu(self.parent, self.tkmaster, "Gastos Horimiga")

    def ActionAbRG(self):
        MenuRegistro.FormMenu(self.tkmaster, "Principal", self.parent.getRegistros())


def CargarArchivos() -> Principal:
    p = Principal()
    return p


def Iniciar(Base: Principal, root: tk.Tk):
    root.title("Menu")
    root.update()
    UI(Base, root)


if __name__ == "__main__":
    Base = CargarArchivos()
    root = tk.Tk()
    root.geometry("600x550")
    root.resizable(width=False, height=False)
    root.update()
    Base.initFormMenu(root)
    Iniciar(Base, root)
    root.mainloop()