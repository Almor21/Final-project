# Final-project

## uml
![uml](/UML.png)

## unit test
Selected funcional requirement: "Distribute the money in categories, created and configured by the user himself, which have the amount of money available for each activity registered in the month."

1. First the category is created with a name, description and available money. For example:
```
testCat = Categoria("Transporte", "Dinero destinado al transporte en el mes",
                    120000)
```
2. Expenses are then created and saved within the category:
```
testGasto = Gasto(1500, "Bus")
testCat.Retiro(testGasto)
testGasto = Gasto(10000, "Taxi")
testCat.Retiro(testGasto)
```
3. To check the balance availability validation algorithm:
```
testGasto = Gasto(110000, "Viaje de trabajo")
testCat.Retiro(testGasto)
```
4. Finally, the expense record within the category and the current balance in the category are displayed on the screen.
```
print(testCat.regGastos.__str__())
print(f"El saldo de la categoria '{testCat.getDescripcion()}' es {testCat.getSaldo()}")
```
  
