import abc
from sqlite3 import Date
from typing import List


class Color:
    def __init__(self):
        self.AZUL = "#2155CD"
        self.BLANCO = "#E8F9FD"
        self.AZULCLARO = "#0AA1DD"

class Transaccion(abc.ABC):
    @abc.abstractmethod
    def getTipo(self):
        ...

    @abc.abstractmethod
    def getCantidad(self) -> float:
        ...

    @abc.abstractmethod
    def getDescripcion(self) -> str:
        ...

    @abc.abstractmethod
    def getFecha(self) -> Date:
        ...

class Ingreso(Transaccion):
    def __init__(self, Valor: float, Fecha: Date, Descripcion: str = ""):
        self.Valor = Valor
        self.Fecha = Fecha
        self.Descripcion = Descripcion

    def getTipo(self) -> str:
        return "Ingreso"

    def getCantidad(self) -> float:
        return self.Valor

    def getDescripcion(self) -> str:
        return self.Descripcion

    def getFecha(self) -> Date:
        return self.Fecha

class Gasto(Transaccion):
    def __init__(self, Valor: float, Fecha: Date, Descripcion: str = ""):
        self.Valor = Valor
        self.Fecha = Fecha
        self.Descripcion = Descripcion

    def getTipo(self) -> str:
        return "Gasto"

    def getCantidad(self) -> float:
        return self.Valor

    def getDescripcion(self) -> str:
        return self.Descripcion

    def getFecha(self) -> Date:
        return self.Fecha

class Movimiento(Transaccion):
    def __init__(self, NomCat: str, Valor: float, Fecha: Date, Descripcion: str = ""):
        self.Mod = "+" if Valor >= 0 else "-"
        self.Valor = abs(Valor)
        self.Fecha = Fecha
        self.NomCat = NomCat
        self.Descripcion = Descripcion

    def getTipo(self) -> str:
        return "Movimiento"

    def getMod(self) -> str:
        return self.Mod

    def getCantidad(self) -> float:
        return self.Valor

    def getNomCat(self) -> str:
        return self.NomCat

    def getDescripcion(self) -> str:
        return self.Descripcion

    def getFecha(self) -> Date:
        return self.Fecha

class GHormiga:
    def __init__(self, Valor: float, Fecha: Date, Descripcion: str = ""):
        self.Valor = Valor
        self.Fecha = Fecha
        self.Descripcion = Descripcion

    def getCantidad(self) -> float:
        return self.Valor

    def getDescripcion(self) -> str:
        return self.Descripcion

    def getFecha(self) -> Date:
        return self.Fecha

class Registro:
    def __init__(self):
        self.Registros: List[Transaccion] = []

    def __str__(self) -> str:
        cad = "Los registros guardados son:\n"
        for r in self.Registros:
            cad += "    - " + r.getTipo() + " = " + str(r.getDescripcion()) + " => " + str(r.getCantidad()) + "\n"
        return cad

    def addTransaccion(self, T: Transaccion) -> None:
        self.Registros.append(T)

    def getRegistros(self) -> List:
        return self.Registros
