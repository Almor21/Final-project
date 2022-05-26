import tkinter as tk
import MenuCategoria
from Clases import MenuRegistros
from Clases.Datos import Principal
from frameCategoria import pn_Categoria

class Color:
    def __init__(self):
        self.AZUL = "#2155CD"
        self.BLANCO = "#E8F9FD"

class UI(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(width=master.winfo_width(), height=master.winfo_height())
        self.parent = master
        self.pack_propagate(False)
        self.pack()
        self.update()

        self.fila = 0
        self.columna = 0
        self.Base = Principal()

        self.initcomponents()

    def nwCategoria(self, Nombre, Descripcion,  Dinero):
        self.Base.CrearCategoria(Nombre, Descripcion, Dinero)
        pn_Categoria(self.fm_cat, self.ActionAC, self.Base.getCategoria(Nombre)).grid(row=self.fila, column=self.columna, padx=10, pady=10)
        self.columna += 1
        if self.columna > 3:
            self.fila += 1
            self.columna = 0

    def ActionAC(self, Nombre):
        self.Base.Ingreso(int(self.tf_Dinero.get()), Nombre)

    def abrirVentanaReg(self):
        MenuRegistros.FormMenu(self.parent, self.Base.regGastos.verRegistros())

    def abrirVentanaCat(self):
        MenuCategoria.FormMenu(self.parent, self.nwCategoria)

    def initcomponents(self):
        cl = Color()

        self.fm_top = tk.Frame(self)
        self.fm_top.config(width=self.winfo_width(), height=80, bg=cl.AZUL)
        self.fm_top.pack()
        self.fm_top.update()

        self.fm_cat = tk.Frame(self)
        aux = self.winfo_height() - 80 - 150
        self.fm_cat.config(width=self.winfo_width(), height=aux, bg=cl.BLANCO)
        self.fm_cat.grid_propagate(False)
        self.fm_cat.pack()

        self.fm_bot = tk.Frame(self)
        self.fm_bot.config(width=self.winfo_width(), height=150, bg=cl.AZUL)
        self.fm_bot.pack()

        tk.Label(self, text="Mi dinero:", bg=cl.AZUL, fg="#E8F9FD", font=('Arial', 14)).place(x=230, y=30)

        self.tf_Dinero = tk.Entry(self)
        self.tf_Dinero.place(x=320, y=35)

        self.bt_Agr = tk.Button(self)
        self.bt_Agr.config(text="Agregar")
        self.bt_Agr.place(x=450, y=32)

        self.bt_Qt = tk.Button(self)
        self.bt_Qt.config(text="Quitar")
        self.bt_Qt.place(x=508, y=32)

        tk.Label(self.fm_bot, text="Categoria", bg=cl.AZUL, fg="#E8F9FD", font=('Arial', 11)).place(x=10, y=20)

        self.bt_CAgr = tk.Button(self.fm_bot)
        self.bt_CAgr.config(text="Añadir", command=self.abrirVentanaCat)
        self.bt_CAgr.place(x=18, y=65)

        self.bt_CQt = tk.Button(self.fm_bot)
        self.bt_CQt.config(text="Eliminar")
        self.bt_CQt.place(x=18, y=100)

        tk.Label(self.fm_bot, text="Gastos Hormiga", bg=cl.AZUL, fg="#E8F9FD", font=('Arial', 11)).place(x=300, y=20)

        self.bt_HVer = tk.Button(self.fm_bot)
        self.bt_HVer.config(text="Ver")
        self.bt_HVer.place(x=320, y=65)

        self.bt_HAgr = tk.Button(self.fm_bot)
        self.bt_HAgr.config(text="Añadir")
        self.bt_HAgr.place(x=320, y=100)

        self.bt_VTReg = tk.Button(self.fm_bot)
        self.bt_VTReg.config(text="Ver todos los registros", command=self.abrirVentanaReg)
        self.bt_VTReg.place(x=550, y=100)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("760x600")
    root.title("Categoria")
    root.update()
    app = UI(root)
    root.mainloop()
