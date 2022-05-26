from sqlite3 import Date
from typing import List


class Gasto:
    def __init__(self, Valor: float, Descripcion: str = None):
        self.Valor = Valor
        self.Descripcion = Descripcion

    def getCantidad(self) -> float:
        return self.Valor

    def getDescripcion(self) -> str:
        return self.Descripcion


class Registro:
    def __init__(self):
        self.Registros: List[Gasto] = []

    def __str__(self) -> str:
        cad = "Los gastos guardados son:\n"
        for gasto in self.Registros:
            cad += "    - " + str(gasto.getDescripcion()) + " => " + str(gasto.getCantidad()) + "\n"
        return cad

    def addGasto(self, gasto: Gasto):
        self.Registros.append(gasto)

    def verRegistros(self) -> None:
        cad = ""
        for gasto in self.Registros:
            cad += f"{gasto.getDescripcion()} => {gasto.getCantidad()}"
        return cad


class Categoria:
    def __init__(self, Nombre: str, Descripcion: str = None, SaldoInc: float = 0.0):
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.Saldo = SaldoInc
        self.regGastos = Registro()

    def __repr__(self):
        r = {'Nombre': self.getNombre, 'Descripcion': self.getDescripcion(), 'SaldoActual': self.getSaldo()}
        return r

    def __str__(self) -> str:
        cad = f"Nombre: {self.getNombre()}\n"
        cad += f"Saldo Actual: {self.getSaldo()}\n"
        return cad

    def getNombre(self) -> str:
        return self.Nombre

    def getDescripcion(self) -> str:
        return self.Descripcion

    def getSaldo(self) -> float:
        return self.Saldo

    def Ingreso(self, valor: float):
        self.Saldo += valor

    def getRegGastos(self) -> Registro:
        return self.regGastos

    def Retiro(self, gasto: Gasto):
        valor = gasto.getCantidad()
        if valor <= self.Saldo:
            self.Saldo -= valor
            self.regGastos.addGasto(gasto)
            print(f"El gasto '{gasto.getDescripcion()}' se ha registrado correctamente.")
        else:
            print(f"El saldo para '{gasto.getDescripcion()}' es insuficiente.")


class Horario:
    def __init__(self, Tipo: str, Fecha: Date, Cantidad: Gasto, Descripcion: str = None):
        self.Tipo = Tipo
        self.Fecha = Fecha
        self.Cantidad = Cantidad
        self.Descripcion = Descripcion


class Principal:
    def __init__(self):
        self.DineroMes = 0.0
        self.lisCategorias: List[Categoria] = []
        self.regGastos = Registro()

    def Ingreso(self, valor: float, NomCat: str = None):
        self.DineroMes += valor
        if NomCat != None:
            self.getCategoria(NomCat).Ingreso(valor)

    def Retiro(self, valor: float, descripcion: str, NomCat: str = None):
        if NomCat != None:
            cat = self.getCategoria(NomCat)

            if cat.valor <= cat.Saldo:
                cat.Saldo -= valor
                nwGasto = Gasto(valor, descripcion)
                cat.regGastos.addGasto(nwGasto)
            else:
                print("El saldo es insuficiente.")
        elif valor <= self.Saldo:
            self.Saldo -= valor
            nwGasto = Gasto(valor, descripcion)
            self.regGastos.addGasto(nwGasto)
        else:
            print("El saldo es insuficiente.")

    def CrearCategoria(self, Nombre: str, Descripcion: str = None, SaldoInc: float = 0.0):
        nwCategoria = Categoria(Nombre, Descripcion, SaldoInc)
        self.lisCategorias.append(nwCategoria)

    def getLisCategorias(self):
        return self.lisCategorias

    def getCategoria(self, nombre):
        for cat in self.lisCategorias:
            if cat.getNombre() == nombre:
                return cat
        return "Categoria no encontrada."

    def EliminarCategoria(self, Nombre: str):
        encontrado = False
        for cat in self.lisCategorias:
            if cat.Nombre == Nombre:
                self.lisCategorias.remove(cat)
                encontrado = True
                break

        if not encontrado:
            print("La categoria no fue encontrada")