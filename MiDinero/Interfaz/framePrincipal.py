import pickle
import tkinter as tk
from Clases.Datos import *
from Interfaz.frameCategoria import Categoria
from Menus import MenuMovimiento, MenuGasto


class Form(tk.Frame):
    def __init__(self, parent: "Principal", tkmaster: tk.Tk):
        color = Color()
        tk.Frame.__init__(self, tkmaster)
        self.config(width=tkmaster.winfo_width(), height=80, bg=color.AZUL)
        self.pack_propagate(False)
        self.pack()
        self.update()

        self.tkmaster = tkmaster
        self.parent = parent

        self.initcomponents()

    def initcomponents(self):
        color = Color()
        self.bt_Volver = None

        tk.Label(self, text="Mi dinero:", bg=color.AZUL,
                 fg=color.BLANCO, font=('Arial', 14)).place(x=150, y=30)

        self.tf_Dinero = tk.Entry(self)
        self.tf_Dinero.place(x=240, y=35)

        self.bt_Agr = tk.Button(self, text="Agregar", command=self.ActionAgr)
        self.bt_Agr.place(x=370, y=32)

        self.bt_Mover = tk.Button(self, text="Movimiento", command=self.ActionMov)
        self.bt_Mover.place(x=428, y=32)

    def ActualizarSaldo(self) -> None:
        self.tf_Dinero["state"] = "normal"
        self.tf_Dinero.delete(0, "end")
        self.tf_Dinero.insert(0, self.parent.Saldo)
        self.tf_Dinero["state"] = "readonly"

    def ActionAgr(self) -> None:
        MenuGasto.FormMenu(self.parent, self.tkmaster, "Principal")

    def ActionMov(self) -> None:
        MenuMovimiento.FormMenu(self.parent, self.tkmaster, "Movimiento")

    def ActivarVolver(self, IniciarVentana) -> None:
        self.bt_Volver = tk.Button(self, text="Volver", command=IniciarVentana)
        self.bt_Volver.place(x=10, y=32)

    def DesactivarVolver(self) -> None:
        if self.bt_Volver is not None:
            self.bt_Volver.destroy()

class Principal:
    def __init__(self):
        self.listCategorias: List[Categoria] = []
        self.listGHormiga: List[GHormiga] = []
        self.regPrincipal = Registro()
        self.Saldo = 0

    def initFormMenu(self, root: tk.Tk):
        self.formMenu = Form(self, root)
        self.formMenu.ActualizarSaldo()

    def delFormMenu(self):
        del(self.formMenu)
        for c in self.getListCategorias():
            del(c.formMenu)

    def ActivarVolver(self, IniciarVentana) -> None:
        self.formMenu.ActivarVolver(IniciarVentana)

    def DesactivarVolver(self) -> None:
        self.formMenu.DesactivarVolver()

    def nwIngreso(self, T: Ingreso) -> None:
        self.Saldo += T.getCantidad()
        self.regPrincipal.addTransaccion(T)
        self.formMenu.ActualizarSaldo()

    def nwGasto(self, T: Gasto) -> None:
        valor = T.getCantidad()
        self.Saldo -= valor
        self.regPrincipal.addTransaccion(T)
        self.formMenu.ActualizarSaldo()

    def nwMovimiento(self, T: Movimiento) -> None:
        cat = self.getCategoria(T.getNomCat())
        Dinero = T.getCantidad()

        if T.getMod() == "+":
            self.Saldo -= Dinero
            cat.Saldo += Dinero
        elif T.getMod() == "-":
            self.Saldo += Dinero
            cat.Saldo -= Dinero

        cat.regCategoria.addTransaccion(T)
        cat.formMenu.ActualizarSaldo()

        self.regPrincipal.addTransaccion(T)
        self.formMenu.ActualizarSaldo()

    def CrearCategoria(self, Nombre: str, Descripcion: str = "") -> Categoria:
        cat = Categoria(self, Nombre, Descripcion)
        self.listCategorias.append(cat)
        return cat

    def EliminarCategoria(self, Nombre: str) -> None:
        encontrado = False
        for cat in self.listCategorias:
            if cat.Nombre == Nombre:
                self.Saldo += cat.Saldo
                self.listCategorias.remove(cat)
                self.formMenu.ActualizarSaldo()
                encontrado = True
                break

        if not encontrado:
            print("La categoria no encontrada para eliminar.")

    def getListCategorias(self) -> List[Categoria]:
        return self.listCategorias

    def getCategoria(self, Nombre: str) -> Categoria:
        for cat in self.listCategorias:
            if cat.Nombre == Nombre:
                return cat
        print("Categoria no encontrada.")
        return None

    def getRegistros(self) -> Registro:
        return self.regPrincipal

    def nwGHormiga(self, Valor: int, Fecha: Date, Descripcion: str) -> None:
        if Valor <= self.Saldo:
            self.Saldo -= Valor
            gh = GHormiga(Valor, Fecha, Descripcion)
            self.listGHormiga.append(gh)
            if self.formMenu is not None:
                self.formMenu.ActualizarSaldo()
        else:
            print(f"El saldo para '{Descripcion}' es insuficiente.")

    def getGHormigas(self) -> List:
        return self.listGHormiga
