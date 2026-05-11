import utilidades

# ID | Nombre | Precio | Stock | Estado
encabezado = ["ID", "Nombre", "Precio", "Stock", "Activo"]
matrizProductos = [
    [1,  "Cortado",           122.0, 5,  True],
    [2,  "Americano",         125.0, 10, True],
    [3,  "Café con leche",    150.0, 8,  True],
    [4,  "Capuccino",         170.0, 6,  True],
    [5,  "Té con limón",      130.0, 12, True],
    [6,  "Medialunas x3",     120.0, 20, True],
    [7,  "Tostado de jamón",  180.0, 7,  True],
    [8,  "Jugo de naranja",   110.0, 15, True],
    [9,  "Cheesecake",        250.0, 4,  True],
    [10, "Agua mineral",       80.0, 30, True],
]

def productoMenu():
    opcion = 1
    while opcion != 0:
        print('''
        --Menu Producto--
        '1 - Alta Producto
        '2 - Baja Producto
        '3 - Modificacion Producto
        '4 - Mostrar Productos
        '5 - Leer Producto
        '6 - Nuevo Producto
        '0 - Volver al menu principal''')

        opcion = utilidades.pedirEntero("Ingresa una opción: ")
        if opcion == 1:
            altaProducto()
        elif opcion == 2:
            bajaProducto()
        elif opcion == 3:
            modificacionProducto()
        elif opcion == 4:
            mostrarListaProducto()
        elif opcion == 5:
            mostrarProducto()
        elif opcion == 6:
            nuevoProducto()
        elif opcion == 0:
            print("Adios!") 

def bajaProducto():
    if not matrizProductos:
        print("No hay productos para eliminar.")
    else:
        mostrarListaProducto()
        idProducto = int(input("Ingrese el ID del producto a dar de baja: "))
        encontrado = False
        i = 0

        while i < len(matrizProductos) and not encontrado:
            if matrizProductos[i][0] == idProducto:
                encontrado = True
                nombre = matrizProductos[i][1]
                if matrizProductos[i][4] == True:
                    matrizProductos[i][4] = False
                    print(f"Producto '{nombre}' (ID: {idProducto}) dado de baja exitosamente.")
                else:
                    print(f"Producto {nombre} (ID: {idProducto}) ya estaba dado de baja.")
            i += 1
        if not encontrado:
            print(f"No existe ningun producto con ID: {idProducto}.")

def altaProducto():
    mostrarListaProducto()
    idProducto = int(input("Ingrese el ID del producto a dar de alta: "))
    encontrado = False
    i = 0
    while i < len(matrizProductos) and not encontrado:
        if matrizProductos[i][0] == idProducto:
            encontrado = True
            nombre = matrizProductos[i][1]
            if matrizProductos[i][4] == False:
                matrizProductos[i][4] = True
                print (f"Producto '{nombre} (ID: {idProducto}) dado de alta exitosamente.'")
            else:
                print(f"El producto '{nombre}' (ID: {idProducto}) ya está activo.")
        i += 1
    if not encontrado:
        print(f"No existe ningun producto con ID: {idProducto}")

def nuevoProducto():
    productoNombre = input("Ingrese el nombre del producto: ")
    productoPrecio = float(input("Ingrese el precio del producto: "))
    productoCantidad = int(input("Ingrese el stock del producto: "))
    nuevo_id = matrizProductos[-1][0] + 1
    matrizProductos.append ([nuevo_id, productoNombre, productoPrecio, productoCantidad, True])
    print(f"Producto '{productoNombre}' agregado con ID: {nuevo_id}")

def modificacionProducto():
    if not matrizProductos:
        print("No hay productos para modificar.")
    else:
        mostrarListaProducto() 
        idProducto = int(input("Ingrese el ID del producto para modificar: "))

        for i in range(len(matrizProductos)): 
            if matrizProductos[i][0] == idProducto:
                id, nombre, precio, stock, activo =matrizProductos[i]

                datoModificado = input("Ingrese un nombre: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizProductos[i][1] = datoModificado
                
                datoModificado = input("Ingrese un precio: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizProductos[i][2] = float(datoModificado)
                
                datoModificado = input("Ingrese un stock: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizProductos[i][3] = int(datoModificado)

                print(f"Producto '{nombre}' (ID: {idProducto}) fue modificado correctamente")
                return
        print("Opción inválida: El ID ingresado no existe.")       


def mostrarListaProducto(es_cliente=False):
    
    if es_cliente:
        print("-"*50)  
        print(f'{"ID":<4}{"Nombre":<25}{"Precio":<10}{"Stock":<8}')
        print("-"*50)
    else:
        print("-"*55)  
        print(f'{"ID":<4}{"Nombre":<25}{"Precio":<10}{"Stock":<8}{"Activo":<6}')
        print("-"*55) 

    for fila in matrizProductos:
        id, nombre, precio, stock, activo = fila
        
        if activo:
            activoString = "SI"
        else:
            activoString = "NO"

        if es_cliente:
            print(f'{id:<4}{nombre:<25}{precio:<10}{stock:<8}')
        else:
            print(f'{id:<4}{nombre:<25}{precio:<10}{stock:<8}{activoString:<6}')
            
    if es_cliente:
        print("-"*50)
    else:
        print("-"*55)


def mostrarProducto():
    if not matrizProductos:
        print("No se encuentra el producto en el sistema.")
    else: 
        idProducto = int(input("Ingresa el ID del prodcuto para buscar: "))
        encontrado = False

        for i in range(len(matrizProductos)):
            if matrizProductos[i] [0] == idProducto:
                id, nombre, precio, stock, activo = matrizProductos[i]
                estado = "Activo" if activo else "Inactivo"
                
                print(f'''
                ----Producto encontrado----
                    ID: {id}
                    NOMBRE: {nombre}
                    PRECIO: {precio}
                    STOCK: {stock}
                    ESTADO: {estado}
                ---------------------------
                ''')
                encontrado = True
                return
        
        if not encontrado:
            print("No se encontró ningún producto con ese ID.")

def obtenerProducto(idProducto):
    i = 0
    while i < len(matrizProductos):
        if int(matrizProductos[i][0]) == int(idProducto):
            return matrizProductos[i]
        i += 1