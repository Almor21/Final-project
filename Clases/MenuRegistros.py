import tkinter as tk

class UI(tk.Frame):
    def __init__(self, master, txt):
        tk.Frame.__init__(self, master)
        self.config(width=master.winfo_width(), height=master.winfo_height())
        self.parent = master
        self.txt = txt
        self.grid()
        self.update()

        self.initcomponents()

    def initcomponents(self):
        tk.Label(self, text="Registros").grid(row=0, column=0, padx=10, pady=10)
        self.textArea = tk.Text(self, width=15, height=5)
        print(self.txt)
        self.textArea.insert(tk.INSERT, self.txt)

        self.textArea.grid(row=1, column=0, padx=10, pady=10)

    def btAction(self):
        self.metodo(self.tf_Nom.get(), self.textArea.get("1.0", "end"), int(self.tf_Dinero.get()))

class FormMenu:
    def __init__(self, master, txt):
        root = tk.Toplevel(master)
        root.geometry("250x230")
        root.update()
        root.title("Agregar")
        app = UI(root, txt)
        root.mainloop()
