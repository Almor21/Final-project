import tkinter as tk
import tkinter.messagebox

from Interfaz import InterfazMenu
from framePrincipal import Principal
from Menus import MenuCategoria, MenuGasto
from Menus import MenuEliminar
from Clases.Datos import Color


class UI(tk.Frame):
    def __init__(self, parent: Principal, tkmaster: tk.Tk):
        tk.Frame.__init__(self, tkmaster)
        self.config(width=tkmaster.winfo_width())
        self.pack(fill="y", expand=True)
        self.update()

        self.tkmaster = tkmaster
        self.parent = parent
        self.parent.ActivarVolver(self.ActionVolver)

        self.fila = 0
        self.columna = 0

        self.initcomponents()

    def initcomponents(self):
        color = Color()

        self.fm_cat = tk.Frame(self)
        aux = self.winfo_height() - 80
        self.fm_cat.config(width=self.winfo_width(), height=aux, bg=color.BLANCO)
        self.fm_cat.grid_propagate(False)
        self.fm_cat.pack()

        self.fm_bot = tk.Frame(self)
        self.fm_bot.config(width=self.winfo_width(), height=80, bg=color.AZUL)
        self.fm_bot.pack()

        self.bt_CAgr = tk.Button(self.fm_bot)
        self.bt_CAgr.config(text="Añadir", width=8, command=self.abrirVentanaCat)
        self.bt_CAgr.place(x=120, y=35)

        self.bt_CQt = tk.Button(self.fm_bot)
        self.bt_CQt.config(text="Eliminar", width=8, command=self.abrirVentanaElm)
        self.bt_CQt.place(x=380, y=35)

        self.initCategorias()

    def ActionVolver(self):
        self.destroy()
        InterfazMenu.Iniciar(self.parent, self.tkmaster)

    def abrirVentanaCat(self):
        MenuCategoria.FormMenu(self, self.tkmaster)

    def abrirVentanaElm(self):
        MenuEliminar.FormMenu(self, self.tkmaster)

    def initCategorias(self) -> None:
        listCat = self.parent.getListCategorias()

        for c in listCat:
            c.initFormMenu(self.fm_cat)
            c.formMenu.grid(row=self.fila, column=self.columna, padx=10, pady=10)

            self.columna += 1
            if self.columna > 2:
                self.fila += 1
                self.columna = 0

    def nwCategoria(self, Nombre: str, Descripcion: str) -> None:
        cat = self.parent.CrearCategoria(Nombre, Descripcion)
        cat.initFormMenu(self.fm_cat)
        cat.formMenu.grid(row=self.fila, column=self.columna, padx=10, pady=10)

        self.columna += 1
        if self.columna > 2:
            self.fila += 1
            self.columna = 0

    def dlCategoria(self, Nombre: str) -> None:
        cat = self.parent.getCategoria(Nombre)
        if cat == None:
            tkinter.messagebox.showinfo(message="Categoria \"" + Nombre + " \" no encontrada.")
        else:
            cat.formMenu.destroy()
            self.parent.EliminarCategoria(Nombre)


def Iniciar(Base: Principal, root: tk.Tk):
    root.title("Categoria")
    root.update()
    UI(Base, root)

if __name__ == "__main__":
    Base = Principal()
    root = tk.Tk()
    root.geometry("600x550")
    root.resizable(width=False, height=False)
    Iniciar(Base, root)
    root.mainloop()
