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
        self.tf_Dinero.insert(0, self.parent.Libre)
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
        self.Libre = 0
        self.formMenu: Form = None

    def initFormMenu(self, root: tk.Tk):
        self.formMenu = Form(self, root)
        self.formMenu.ActualizarSaldo()

    def ActivarVolver(self, IniciarVentana) -> None:
        self.formMenu.ActivarVolver(IniciarVentana)

    def DesactivarVolver(self) -> None:
        self.formMenu.DesactivarVolver()

    def Guardar(self):
        pass

    def nwIngreso(self, T: Ingreso) -> None:
        self.Libre += T.getCantidad()
        self.regPrincipal.addTransaccion(T)
        if self.formMenu is not None:
            self.formMenu.ActualizarSaldo()

    def nwGasto(self, T: Gasto) -> None:
        valor = T.getCantidad()

        if valor <= self.Libre:
            self.Libre -= valor
            self.regPrincipal.addTransaccion(T)
            if self.formMenu is not None:
                self.formMenu.ActualizarSaldo()
        else:
            print(f"El saldo para '{T.getDescripcion()}' es insuficiente.")

    def nwMovimiento(self, T: Movimiento) -> None:
        cat = self.getCategoria(T.getNomCat())
        Dinero = T.getCantidad()

        if T.getMod() == "+":
            if Dinero <= self.Libre:
                self.Libre -= Dinero
                cat.Saldo += Dinero
            else:
                print("Dinero (" + str(Dinero) + ") insuficiente para mover a " + cat.Saldo())
                return
        elif T.getMod() == "-":
            if Dinero <= cat.Saldo:
                self.Libre += Dinero
                cat.Saldo -= Dinero
            else:
                print("Dinero (" + str(Dinero) + ") insuficiente para sacar de " + cat.Saldo)
                return

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
                self.Libre += cat.Saldo
                self.listCategorias.remove(cat)
                self.formMenu.ActualizarSaldo()
                encontrado = True
                break

        if not encontrado:
            print("La categoria no encontrada para eliminar.")

    def getListCategorias(self) -> List:
        return self.listCategorias

    def getCategoria(self, Nombre: str) -> Categoria:
        for cat in self.listCategorias:
            if cat.Nombre == Nombre:
                return cat
        print("Categoria no encontrada.")

    def getRegistros(self) -> Registro:
        return self.regPrincipal

    def nwGHormiga(self, Valor: int, Fecha: Date, Descripcion: str) -> None:
        if Valor <= self.Libre:
            self.Libre -= Valor
            gh = GHormiga(Valor, Fecha, Descripcion)
            self.listGHormiga.append(gh)
            if self.formMenu is not None:
                self.formMenu.ActualizarSaldo()
        else:
            print(f"El saldo para '{Descripcion}' es insuficiente.")

    def getGHormigas(self) -> List:
        return self.listGHormiga
