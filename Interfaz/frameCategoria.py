import tkinter as tk
from typing import Dict
from Clases.Datos import *
from Menus import MenuRegistro, MenuGasto


class Form(tk.Frame):
    def __init__(self, parent: "Categoria", tkmaster):
        tk.Frame.__init__(self, tkmaster)
        color = Color()
        self.config(width=170, height=100, bg=color.BLANCO, bd=2, relief="groove")
        self.tkmaster = tkmaster
        self.parent = parent

        self.initcomponents()

    def initcomponents(self) -> None:
        color = Color()
        tk.Label(self, text=self.parent.Nombre, bg=color.BLANCO).place(x=10, y=10)

        self.etq_Dinero = tk.Label(self, text="Dinero: " + str(self.parent.Saldo), bg=color.BLANCO)
        self.etq_Dinero.place(x=10, y=35)

        self.bt_Cal = tk.Button(self, text="Calendario", width=8, command=self.ActionCal)
        self.bt_Cal.place(x=10, y=60)

        self.bt_Agr = tk.Button(self, text="Agregar", width=8, command=self.ActionAgr)
        self.bt_Agr.place(x=90, y=60)

    def ActualizarSaldo(self) -> None:
        self.etq_Dinero.config(text="Dinero: " + str(self.parent.Saldo))

    def ActionAgr(self) -> None:
        MenuGasto.FormMenu(self.parent, self.tkmaster, self.parent.Nombre)

    def ActionCal(self) -> None:
        MenuRegistro.FormMenu(self.tkmaster, self.parent.Nombre, self.parent.getRegistro())

class Categoria:
    def __init__(self, parent, Nombre: str, Descripcion: str = ""):
        self.parent = parent
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.Saldo = 0
        self.regCategoria = Registro()

    def initFormMenu(self, master):
        self.formMenu = Form(self, master)

    def __repr__(self) -> Dict:
        r = {'Nombre': self.Nombre, 'Descripcion': self.Descripcion, 'SaldoActual': self.Saldo}
        return r

    def __str__(self) -> str:
        cad = f"Nombre: {self.Nombre}\n"
        cad += f"Saldo Actual: {self.Nombre}\n"
        return cad

    def nwIngreso(self, T: Ingreso) -> None:
        self.Saldo += T.getCantidad()
        self.formMenu.ActualizarSaldo()
        self.regCategoria.addTransaccion(T)

    def nwGasto(self, T: Gasto) -> None:
        valor = T.getCantidad()

        if valor <= self.Saldo:
            self.Saldo -= valor
            self.formMenu.ActualizarSaldo()
            self.regCategoria.addTransaccion(T)
        else:
            print(f"El saldo para '{T.getDescripcion()}' es insuficiente.")

    def getRegistro(self) -> Registro:
        return self.regCategoria