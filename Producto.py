
def productoMenu():
    opcion = 1
    while opcion != 0:
        print('Menu Producto\n' 
        '1 - Alta Producto\n' 
        '2 - Baja Producto\n' 
        '3 - Modificacion Producto\n'
        '4 - Mostrar Productos\n'
        '0 - Volver al menu principal\n')

        opcion = int(input("Ingresa un numero: "))
        if opcion == 1:
            altaProducto()
        if opcion == 2:
            bajaProducto()
        if opcion == 3:
            modificacionProducto()
        if opcion == 4:
            mostrarListaProducto()
        if opcion == 0:
            print("Adios!") 
        
        
    
def altaProducto():
    productoNombre = input("Ingrese el nombre del producto: ")
    productoPrecio = input("Ingrese el precio del producto: ")
    productoCantidad = input("Ingrese el stock del producto: ")

def bajaProducto():
    idProducto = input("Ingrese el ID del producto: ")

def modificacionProducto():
    idProducto = input("Ingrese el ID del producto: ")

def mostrarListaProducto():
    print("Listado")