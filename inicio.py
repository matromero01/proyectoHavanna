import Producto
import os

#print("Inicio de Havanna")

opcion = 1
while opcion != 0:
    print('''Menu principal 
    '1 - Menu Producto
    '2 - Menu ... 
    '3 - Menu ...
    '0 - Salir''')

    opcion = int(input("Ingresa un numero: "))
    if opcion == 1:
        Producto.productoMenu()
    if opcion == 0:
        print("Adios!")     
