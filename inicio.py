import Producto
import os

#print("Inicio de Havanna")

opcion = 1
while opcion != 0:
    print('Menu principal\n' 
    '1 - Menu Producto\n' 
    '2 - Menu ...\n' 
    '3 - Menu ...\n'
    '0 - Salir\n')

    opcion = int(input("Ingresa un numero: "))
    if opcion == 1:
        Producto.productoMenu()
    if opcion == 0:
        print("Adios!")     
