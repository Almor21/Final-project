import tkinter as tk

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
        tk.Label(self, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        self.tf_Nom = tk.Entry(self)
        self.tf_Nom.grid(row=0, column=1, padx=10, pady=10)

        self.bt = tk.Button(self, text="Eliminar")
        self.bt.config(command=self.btAction)
        self.bt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def btAction(self):
        self.parent.dlCategoria(self.tf_Nom.get())

class FormMenu:
    def __init__(self, parent, tkmaster):
        root = tk.Toplevel(tkmaster)
        root.update()
        root.title("Eliminar")
        app = UI(root, parent)
        root.mainloop()
