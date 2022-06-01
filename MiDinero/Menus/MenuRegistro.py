import tkinter as tk
from sqlite3 import Date
from tkinter import ttk
from Clases.Datos import Registro, Color, Movimiento, Ingreso, Gasto


class UI(tk.Frame):
    def __init__(self, master, Regs: Registro):
        tk.Frame.__init__(self, master)
        self.config(width=master.winfo_width(), height=master.winfo_height())
        self.parent = master
        self.pack_propagate(False)
        self.pack()
        self.update()

        self.initcomponents(Regs)

    def initcomponents(self, Regs: Registro):
        color = Color()
        fm_top = tk.Frame(self, bg=color.AZUL)
        fm_top.pack(fill="x")

        tk.Label(fm_top, text="Registro", bg=color.AZUL,
                 fg=color.BLANCO, font=('Arial', 14)).pack(pady=5)

        cvR = tk.Canvas(self, width=self.winfo_width()-20)
        sb = tk.Scrollbar(self, orient="vertical", command=cvR.yview)
        cvR.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y", expand=True)
        cvR.pack(side="left", fill="y", expand=True)
        cvR.update()

        scrollable_frame = tk.Frame(cvR)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: cvR.configure(
                scrollregion=cvR.bbox("all")
            )
        )
        cvR.create_window((0, 0), window=scrollable_frame, anchor="nw")

        for reg in Regs.getRegistros():
            fm = tk.Frame(scrollable_frame, width=cvR.winfo_width(), height=50)
            fm.grid_propagate(False)
            fm.pack()

            if reg.getTipo() == "Movimiento":
                fm.config(height=70)
                txt = reg.getTipo() + ": " + str(reg.getMod()) + str(reg.getCantidad())
                tk.Label(
                    fm,
                    text=txt,
                    font=("Arial", 11),
                    fg="blue"
                ).grid(row=0, column=0)

                tk.Label(
                    fm,
                    text="Categoria: " + reg.getNomCat(),
                    font=("Arial", 8)
                ).grid(row=1, column=0, sticky="w")
            else:
                txt = reg.getTipo() + ": " + str(reg.getCantidad())
                tk.Label(
                    fm,
                    text=txt,
                    font=("Arial", 11),
                    fg="green" if reg.getTipo() == "Ingreso" else "red"
                ).grid(row=0, column=0)

            f = reg.getFecha()
            txt = str(f.day) + "/" + str(f.month) + "/" + str(f.year)
            fm.columnconfigure(1, weight=2)
            tk.Label(fm, text=txt, fg="gray", font=("Arial", 8)).grid(row=0, column=1, sticky="e")

            tk.Label(fm, text=reg.getDescripcion()).grid(row=2, column=0, columnspan=2, sticky="w")


class FormMenu:
    def __init__(self, master, title: str, Regs: Registro):
        root = tk.Toplevel(master)
        root.geometry("250x350")
        root.title(title)
        root.resizable(width=False, height=False)
        root.update()
        app = UI(root, Regs)
        root.mainloop()
