import tkinter as tk

class UI(tk.Frame):
    def __init__(self, master, metodo):
        tk.Frame.__init__(self, master)
        self.config(width=master.winfo_width(), height=master.winfo_height())
        self.parent = master
        self.metodo = metodo
        self.grid()
        self.update()

        self.initcomponents()

    def initcomponents(self):
        tk.Label(self, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        self.tf_Nom = tk.Entry(self)
        self.tf_Nom.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Dinero").grid(row=1, column=0, padx=10, pady=10)
        self.tf_Dinero = tk.Entry(self)
        self.tf_Dinero.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Descripcion").grid(row=2, column=0, padx=10, pady=10)
        self.textArea = tk.Text(self, width=15, height=5)
        self.textArea.grid(row=2, column=1, padx=10, pady=10)

        self.bt = tk.Button(self, text="Agregar")
        self.bt.config(command=self.btAction)
        self.bt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def btAction(self):
        self.metodo(self.tf_Nom.get(), self.textArea.get("1.0", "end"), int(self.tf_Dinero.get()))

class FormMenu:
    def __init__(self, master, metodo):
        root = tk.Toplevel(master)
        root.geometry("250x230")
        root.update()
        root.title("Agregar")
        app = UI(root, metodo)
        root.mainloop()
