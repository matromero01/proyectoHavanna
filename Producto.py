
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
        '0 - Volver al menu principal''')

        opcion = int(input("Ingresa una opción: "))
        if opcion == 1:
            altaProducto()
        if opcion == 2:
            bajaProducto()
        if opcion == 3:
            modificacionProducto()
        if opcion == 4:
            mostrarListaProducto()
        if opcion == 5:
            mostrarProducto()
        if opcion == 0:
            print("Adios!") 
        
        
    
def altaProducto1():
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
                encontrado = True

                nombre = matrizProductos[i][1] 

                if matrizProductos[i][4] == True:
                    matrizProductos[i][4] = False
                    print(f"Producto '{nombre}' (ID: {idProducto}) dado de baja exitosamente.")
                else:
                    print(f"Producto '{nombre}' (ID: {idProducto}) ya fue dado de baja anteriormente")
                    condicionAlta = input("¿Quiere dar de alta el producto ahora? (si/no): \nProducto '{nombre}' (ID: {idProducto})").strip().lower()
                    
                    while condicionAlta != "si" and condicionAlta != "no":
                        print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
                        condicionAlta = input("¿Quiere darlo de alta ahora? (si/no): ").strip().lower()
                    
                    if condicionAlta == "si":
                        altaProducto()
                break

    if not encontrado:
        print("Opción inválida: El ID ingresado no existe.")

def altaProducto():
    if not matrizProductos:
        print("No hay productos para dar de alta.")
    else:
        mostrarListaProducto() 
        idProducto = int(input("Ingrese el ID del producto a dar de alta: "))
        encontrado = False

        for i in range(len(matrizProductos)): 
            if matrizProductos[i][0] == idProducto:
                encontrado = True
                nombre = matrizProductos[i][1] 
                
                if matrizProductos[i][4] == False:
                    matrizProductos[i][4] = True
                    print(f"Producto '{nombre}' (ID: {idProducto}) dado de alta exitosamente.")
                else:
                    print(f"El producto '{nombre}' (ID: {idProducto}) ya está activo.")
                    condicionBaja = input("¿Quiere darlo de baja ahora? (si/no): ").strip().lower()
                    
                    while condicionBaja != "si" and condicionBaja != "no":
                        print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
                        condicionBaja = input("¿Quiere darlo de baja ahora? (si/no): ").strip().lower()
                    
                    if condicionBaja == "si":
                        bajaProducto() 
                break 

    if not encontrado:
        print("Opción inválida: El ID {idProducto} ingresado no existe.") 
        seguirIngresando = input("¿Desea ingresar un nuevo producto? (si/no)").strip().lower()
        cont = 0
        while seguirIngresando != "si" and seguirIngresando != "no":
            print("ERROR DE TIPEO. Por favor ingrese "'si'" o "'no'"")
            seguirIngresando = input("¿Desea ingresar un nuevo producto? (si/no)").strip().lower()
        
        if seguirIngresando == "si":
            productoNombre = input("Ingrese el nombre del producto: ")
            productoPrecio = float(input("Ingrese el precio del producto: "))
            productoCantidad = int(input("Ingrese el stock del producto: "))
            cont = cont +1

            if matrizProductos:
                nuevo_id = matrizProductos[-1][0] + 1
            else:
                nuevo_id = 1

            producto = [matrizProductos[-1][0] + 1, productoNombre, productoPrecio, productoCantidad, True]
            matrizProductos.append(producto)

            print("Producto: "+productoNombre+" ¡Agregado correctamente!")
        else:
            print(f"Se ingresaron: {cont} producto/s correctamente")
        
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


def mostrarListaProducto():
    
    print("-"*55)  
    print(f'{"ID":<4}{"Nombre":<25}{"Precio":<10}{"Stock":<8}{"Activo":<6}')
    print("-"*55)       

    for fila in matrizProductos:
        id, nombre, precio, stock, activo = fila
        
        if activo:
            activoString = "SI"
        else:
            activoString = "NO"

        
        print(f'{id:<4}{nombre:<25}{precio:<10}{stock:<8}{activoString:<6}')

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
    for producto in matrizProductos:
        if int(producto[0]) == int(idProducto):
            return producto
        
#Visualización para clientes
def visualizarListaProducto():
    
    print("-"*50)  
    print(f'{"ID":<4}{"Nombre":<25}{"Precio":<10}{"Stock":<8}')
    print("-"*50)       

    for fila in matrizProductos:
        id, nombre, precio, stock, activo = fila
        
        if activo:
            activoString = "SI"
        else:
            activoString = "NO"

        
        print(f'{id:<4}{nombre:<25}{precio:<10}{stock:<8}')
    
    print("-"*50)  
     
