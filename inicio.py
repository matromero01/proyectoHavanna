import Producto
import Cliente

#print("Inicio de Havanna")

opcion = 1
while opcion != 0:
    print('''Menu principal 
    '1 - Menu Producto
    '2 - Menu Cliente
    '3 - Menu ...
    '0 - Salir''')

    opcion = int(input("Ingresa una opción: "))
    if opcion == 1:
        Producto.productoMenu()     
    elif opcion == 2: #Este es el nuevo menu de clientes
        Cliente.menuInicio()
    if opcion == 0:
        print("Adios!")     
