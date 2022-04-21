# Final-project

Selected funcional requirement: "Distribute the money in categories, created and configured by the user himself, which have the amount of money available for each activity registered in the month."

## Uml Code
```
@startuml

class Principal{
+ DineroMes: float
...Metodos...
+ Ingreso()
+ Retiro()
+ CrearCategoria()
+ EliminarCategoria()
}

class Categoria {
+ Nombre: str
+ Descripcion: str
+ Saldo: float
...Metodos...
+ Ingreso()
+ Retiro()
}

class Gasto{
+ Valor: float
+ Descripcion: str
}

class Horarios{
+ Tipo:str
+ Descripcion: str
+ Fecha:Date
+ Cantidad: Float
}

class Registro {
+ addGasto()
+ VisualizarRegistro()
}

Principal "1" --- "0...*" Categoria
Principal "1" --- "0...*" Horarios
Horarios "1" --- "0...*" Gasto
Principal "1" --- "1" Registro
Categoria "1" --- "1" Registro
@enduml
```
## uml
![uml](/uml.png)

