
matrizProductos = [[1, "Cortado", 122.0, 5, True], [2, "Americano", 125.0, 10, True]]

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

        opcion = int(input("Ingresa un numero: "))
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
            print("Se ingresaron: "+ cont + "producto/s correctamente")
        

            





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
    for fila in matrizProductos:
        for elemento in fila:
            print(elemento, end=" ")
        print()

def mostrarProducto():
    if not matrizProductos:
        print("No se encuentra el Producto.")
    else:
        idProducto = int(input("Ingrese el ID del producto para buscar: "))

        for i in range(len(matrizProductos)): 
            if matrizProductos[i][0] == idProducto:
                id, nombre, precio, stock, activo = matrizProductos[i]
                if activo:
                    estado = "Activo"
                else:
                    estado = "Inactivo"
                
                print(f'''
                ----Producto encontrado----
                    ID: {id}
                    NOMBRE: {nombre}
                    PRECIO: {precio}
                    STOCK: {stock}
                    ESTADO: {estado}
                ---------------------------
                ''')
                return
