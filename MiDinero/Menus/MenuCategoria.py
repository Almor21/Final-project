import tkinter as tk


class UI(tk.Frame):
    def __init__(self, master, parent):
        tk.Frame.__init__(self, master)
        self.tkmaster = master
        self.parent = parent
        self.grid()
        self.update()

        self.initcomponents()

    def initcomponents(self):
        tk.Label(self, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        self.tf_Nom = tk.Entry(self)
        self.tf_Nom.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Descripcion").grid(row=1, column=0, padx=10, pady=10)
        self.textArea = tk.Text(self, width=15, height=5)
        self.textArea.grid(row=1, column=1, padx=10, pady=10)

        self.bt = tk.Button(self, text="Agregar")
        self.bt.config(command=self.btAction)
        self.bt.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def btAction(self):
        self.parent.nwCategoria(self.tf_Nom.get(), self.textArea.get("1.0", "end"))

class FormMenu:
    def __init__(self, parent, master):
        root = tk.Toplevel(master)
        root.update()
        root.title("Agregar")
        app = UI(root, parent)
        root.mainloop()
