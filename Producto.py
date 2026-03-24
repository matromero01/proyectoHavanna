
matrizProductos = [[1, "Cortado", 122.0, 5, True], [2, "Americano", 125.0, 10, True]]

def productoMenu():
    opcion = 1
    while opcion != 0:
        print('''Menu Producto
        '1 - Alta Producto
        '2 - Baja Producto
        '3 - Modificacion Producto
        '4 - Mostrar Productos
        '0 - Volver al menu principal''')

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

    producto = [matrizProductos[-1][0] + 1, productoNombre, productoPrecio, productoCantidad, True]

    matrizProductos.append(producto)

def bajaProducto():
    if not matrizProductos:
        print("No hay productos para eliminar.")
    else:
      mostrarListaProducto()
      idProducto = int(input("Ingrese el ID del producto a dar de baja: "))

      encontrado = False

      for i in range(len(matrizProductos)): 
        if matrizProductos[i][0] == idProducto:
            nombre = matrizProductos[i][1]     
            matrizProductos[i][4] = False
            print(f"Producto '{nombre}' (ID: {idProducto}) dado de baja exitosamente.")
            encontrado = True      
            break 

    if not encontrado:
        print("Opción inválida: El ID ingresado no existe.") 

def modificacionProducto():
    idProducto = input("Ingrese el ID del producto: ")

def mostrarListaProducto():
    for fila in matrizProductos:
        for elemento in fila:
            print(elemento, end=" ")
        print()

