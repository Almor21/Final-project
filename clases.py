from sqlite3 import Date
from typing import List
from typing_extensions import Self

class Gasto:
    def __init__(self, Valor: float, Descripcion: str = None):
        self.Valor = Valor
        self.Descripcion = Descripcion

    def getCantidad(self):
        return self.Valor
    
    def getDescripcion(self):
        return self.Descripcion

class Registro:
    def __init__(self, Descripcion: str):
        self.Descripcion = Descripcion
        self.Registros: List[Gasto] = []
    
    def addGasto(self, gasto: Gasto):
        self.Registros.append(gasto)

    def verRegistros(self):
        pass


class Categoria:
    def __init__(self, Nombre: str, Descripcion: str = None, SaldoInc: float = 0.0):
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.Saldo = SaldoInc
        self.regGastos = Registro()

    def getNombre(self) -> str:
        return self.Nombre

    def getDescripcion(self) -> str:
        return self.Descripcion
    
    def getSaldo(self) -> float:
        return self.Saldo
    
    def Ingreso(self, valor: float):
        self.Saldo += valor

    def Retiro(self, gasto: Gasto):
        valor = gasto.getCantidad
        if valor <= self.Saldo:
            self.Saldo -= valor
            self.regGastos.addGasto(gasto)
        else:
            print("El saldo es insuficiente.")

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

    def Ingreso(self, valor: float):
        self.DineroMes += valor
    
    def Retiro(self, valor: float, descripcion: str):
        if valor <= self.Saldo:
            self.Saldo -= valor
            nwGasto = Gasto(valor, descripcion)
            self.regGastos.addGasto(nwGasto)
        else:
            print("El saldo es insuficiente.")

    def CrearCategoria(self, Nombre: str, Descripcion: str = None, SaldoInc: float = 0.0):
        nwCategoria = Categoria(Nombre, Descripcion, SaldoInc)
        self.lisCategoria.append(nwCategoria)

    def EliminarCategoria(self, Nombre: str):
        encontrado = False
        for cat in self.lisCategoria:
            if cat.Nombre == Nombre:
                self.lisCategorias.remove(cat)
                encontrado = True
                break
        
        if not encontrado:
            print("La categoria no fue encontrada")
