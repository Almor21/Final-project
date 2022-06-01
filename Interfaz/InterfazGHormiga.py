import tkinter as tk
from sqlite3 import Date

from Clases.Datos import Registro, Color
from Menus import MenuGHormiga


class UI(tk.Frame):
    def __init__(self, parent, master):
        tk.Frame.__init__(self, master)
        self.config(width=master.winfo_width(), height=master.winfo_height())
        self.pack_propagate(False)
        self.pack()
        self.update()

        self.parent = parent
        self.tkmaster = master

        self.initcomponents()

    def initcomponents(self):
        color = Color()
        fm_top = tk.Frame(self, bg=color.AZUL)
        fm_top.pack(fill="x")

        tk.Label(fm_top, text="Gastos Hormiga", bg=color.AZUL,
                 fg=color.BLANCO, font=('Arial', 14)).pack(pady=5)

        self.bt = tk.Button(fm_top, text="Agregar", command=self.ActionAgr)
        self.bt.place(x=240, y=6)

        self.cvR = tk.Canvas(self, width=self.winfo_width()-20)
        sb = tk.Scrollbar(self, orient="vertical", command=self.cvR.yview)
        self.cvR.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y", expand=True)
        self.cvR.pack(side="left", fill="y", expand=True)
        self.cvR.update()

        self.scrollable_frame = None
        self.Actualizar()

    def Actualizar(self):
        if self.scrollable_frame is not None:
            self.scrollable_frame.destroy()

        self.scrollable_frame = tk.Frame(self.cvR)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.cvR.configure(
                scrollregion=self.cvR.bbox("all")
            )
        )
        self.cvR.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        for gh in self.parent.getGHormigas():
            fm = tk.Frame(self.scrollable_frame, width=self.cvR.winfo_width(), height=50)
            fm.grid_propagate(False)
            fm.pack()

            tk.Label(
                fm,
                text=str(gh.getCantidad()),
                font=("Arial", 11),
                fg="red"
            ).grid(row=0, column=0)

            f = gh.getFecha()
            txt = str(f.day) + "/" + str(f.month) + "/" + str(f.year)
            fm.columnconfigure(1, weight=2)
            tk.Label(fm, text=txt, fg="gray", font=("Arial", 8)).grid(row=0, column=1, sticky="e")

            tk.Label(fm, text=gh.getDescripcion()).grid(row=1, column=0, columnspan=2, sticky="w")

    def ActionAgr(self):
        MenuGHormiga.FormMenu(self, self.tkmaster, "Gastos Hormiga")

    def nwGHormiga(self, Valor: int, Fecha: Date, Descripcion: str):
        self.parent.nwGHormiga(Valor, Fecha, Descripcion)
        self.Actualizar()

class FormMenu:
    def __init__(self, parent, tkmaster: tk.Tk, title: str):
        root = tk.Toplevel(tkmaster)
        root.geometry("300x350")
        root.title(title)
        root.resizable(width=False, height=False)
        root.update()
        UI(parent, root)
        root.mainloop()