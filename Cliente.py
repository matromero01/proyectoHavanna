import Producto, Venta, Ticket, Reporte

matrizCliente = [
    [1,  "Facundo Mello",      "facundomello34@gmail.com",  "1124084431", True],
    [2,  "Lionel Messi",       "messi@gmail.com",           "1122334455", True],
    [3,  "Juan Perez",         "juanperez@gmail.com",       "1156781234", True],
    [4,  "Maria Lopez",        "marialopez@hotmail.com",    "1167894321", True],
    [5,  "Carlos Gomez",       "carlosgomez@yahoo.com",     "1178905678", False],
    [6,  "Laura Fernandez",    "lauraf@gmail.com",          "1189016789", True],
    [7,  "Diego Martinez",     "diegom@outlook.com",        "1190127890", True],
    [8,  "Ana Rodriguez",      "anar@gmail.com",            "1101238901", False],
]


def menuAutenticacion():
    es_admin = ""
    while es_admin != "si" and es_admin != "no":
        print("\n¿Sos administrador? (si/no): ")
        es_admin = input("Respuesta: ").strip().lower()
        if es_admin != "si" and es_admin != "no":
            print("Respuesta inválida. Ingrese 'si' o 'no'.")
    
    if es_admin == "si":
        loginAdmin()
    elif es_admin == "no":
        loginCliente()


def loginAdmin():
    print("\n--- Login Administrador ---")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")

    if usuario == "admin" and contraseña == "admin123":
        print("Login completado exitosamente. Bienvenido, Administrador!")
        adminMenu()
    else: 
        print("Usuario o contraseña son incorrectos. Intente nuevamente.")
        menuAutenticacion()

def mostrarClientes():
    print("\nListado de clientes:")
    for cliente in matrizCliente:
        estado = "Activo" if cliente[4] else "Inactivo"
        print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}, Teléfono: {cliente[3]}, Estado: {estado}")


def cambiarEstadoCliente():
    mostrarClientes()
    id_cliente = int(input("\nIngrese el ID del cliente a modificar: "))
    for cliente in matrizCliente:
        if cliente[0] == id_cliente:
            if cliente[4]:
                confirmar = input(f"El cliente {cliente[1]} está activo. Desea darlo de baja? (si/no): ").strip().lower()
                if confirmar == "si":
                    cliente[4] = False
                    print(f"Cliente {cliente[1]} dado de baja.")
                else:
                    print("No se realizaron cambios.")
            else:
                confirmar = input(f"El cliente {cliente[1]} está inactivo. Desea darlo de alta? (si/no): ").strip().lower()
                if confirmar == "si":
                    cliente[4] = True
                    print(f"Cliente {cliente[1]} dado de alta.")
                else:
                    print("No se realizaron cambios.")
            return
    print("No se encontró el cliente con ese ID.")


def gestionarUsuarios():
    opcion = 1
    while opcion != 0:
        print('''\n-- Menú de Usuarios --
        1 - Ver Clientes
        2 - Activar / Dar de baja cliente
        3 - Buscar y Ver compras de cliente
        0 - Volver al menú anterior''')
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            mostrarClientes()
        elif opcion == 2:
            cambiarEstadoCliente()
        elif opcion == 3:
            buscarYVerCliente()
        elif opcion == 0:
            print("Volviendo al menú anterior...")
        else:
            print("Opción inválida. Intente nuevamente.")


def loginCliente():
    print("\n--- Login Cliente ---")
    email = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de contacto: ")
    for cliente in matrizCliente:
        if cliente[2] == email and cliente[3] == telefono and cliente[4] == True:
            print(f"Login completado exitosamente. Bienvenido, {cliente[1]}!")
            clienteMenu(cliente[0])
            return

    print("Correo electrónico o número de contacto incorrectos, o el cliente está dado de baja. Intente nuevamente.")
    menuAutenticacion()

def adminMenu():
    opcion = 1
    while opcion != 0:
        print('''Menu Principal
        '1 - Gestionar Productos/Stock
        '2 - Administrar Usuarios/Clientes
        '3 - Gestion de ventas
        '4 - Reportes
        '5 - Gestionar Ticket
        '0 - Salir del sistema''')
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            Producto.productoMenu()
        elif opcion == 2:
            gestionarUsuarios()
        elif opcion == 3:
            Venta.menuVenta()
        elif opcion == 4:
            Reporte.menuReportes()
        elif opcion == 5:
            Ticket.ticketMenu()
        elif opcion == 0:
            print("Volviendo al menú anterior...")
        else:
            print("Opción inválida. Intente nuevamente.")


def clienteMenu(idCliente):
    carrito = []
    opcion = 1
    while opcion != 0:
        print('''Menu Principal
        '1 - Ver Productos
        '2 - Agregar al Carrito
        '3 - Vaciar Carrito
        '4 - Ver Carrito
        '5 - Finalizar compra
        '0 - Salir del sistema''')

        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            Producto.mostrarListaProducto()
        elif opcion == 2:
            carrito.extend(agregarAlCarrito())
        elif opcion == 3:
            vaciarCarrito(carrito)
        elif opcion == 4:
            verCarrito(carrito)
        elif opcion == 5:
            if not carrito:
                print("El carrito está vacío. No hay productos para comprar.")
            else:
                Venta.altaVenta(idCliente, carrito)
                carrito.clear()
        if opcion == 0:
            print("Volviendo al menu principal...")

def altaCliente():  
    """ Dar de alta un nuevo cliente"""
    print("\n--- Registrarse ---")
    clienteNombre= input("Ingrese su nombre nuevo cliente: ")
    clienteEmail= input("Ingrese su Email: ")
    while "@" not in clienteEmail or "." not in clienteEmail:
        print("Correo electrónico no válido. Por favor, ingrese un correo electrónico válido.")
        clienteEmail = input("Ingrese su Email: ")
    clienteTelefono= input("Ingrese su número de contacto: ")
    while not clienteTelefono.isdigit() or len(clienteTelefono) < 7:
        print("Número de teléfono invalido, por favor, vuelve a ingresarlo nuevamente.")
        clienteTelefono= input("Ingrese su número de contacto: ")


    nuevoId= matrizCliente[-1] [0] + 1 if matrizCliente else 1
    nuevoCliente= [nuevoId, clienteNombre, clienteEmail, clienteTelefono, True]
    
    matrizCliente.append(nuevoCliente)
    print(f"Cliente '{clienteNombre}' (ID: {nuevoId}) dado de alta exitosamente.\n")

def bajaCliente(): 
    """ Dar de baja un cliente existente"""
    print("\n--- Baja de cliente ---")
    if not matrizCliente:
        print("No hay clientes para eliminar.")
    else: 
        idCliente = int(input("Ingrese el ID del cliente a dar de baja: "))
        encontrado = False


        for i in range(len(matrizCliente)):
            cliente = matrizCliente[i][1]
            if matrizCliente[i] [0] == idCliente:
                encontrado = True
                if matrizCliente[i][4] == True:
                    matrizCliente[i] [4] = False
                    print(f"Cliente '{cliente}' (ID: {idCliente}) dado de baja exitosamente.")
                else: 
                    print(f"Cliente '{cliente}' (ID: {idCliente}) ya fue dado de baja anteriormente.")
                    condicionAlta = input(f"¿Queres dar de alta al cliente ahora? (si/no): \n Cliente '{cliente}' (ID: {idCliente})")
                    while condicionAlta != "si" and condicionAlta != "no":
                        print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
                        condicionAlta = input("¿Quiere darlo de alta ahora? (si/no): ").strip().lower()
                    
                    if condicionAlta == "si":
                        altaCliente() 
                        break 
        if not encontrado: 
            print(f"No se encontró ningún cliente con ID: {idCliente}. \n")

def modificacionCliente():
    if not matrizCliente:
        print("No hay cliente para modificar.")
    else:
        mostrarListaCliente() 
        idCliente = int(input("Ingrese el ID del cliente para modificar: "))

        for i in range(len(matrizCliente)): 
            if matrizCliente[i][0] == idCliente:
                id, nombre, mail, numero, activo =matrizCliente[i]

                datoModificado = input("Ingrese un nombre: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizCliente[i][1] = datoModificado
                
                datoModificado = input("Ingrese un mail: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizCliente[i][2] = datoModificado
                
                datoModificado = input("Ingrese un numero: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizCliente[i][3] = datoModificado

                print(f"Cliente '{nombre}' (ID: {idCliente}) fue modificado correctamente")
                return
        print("Opción inválida: El ID ingresado no existe.")      

def mostrarListaCliente():
    print(f"{'ID':<5} {'Nombre':<20} {'Email':<30} {'Telefono':<15} {'Activo':<8}")
    print("-" * 80)
    for fila in matrizCliente:
        print(f"{fila[0]:<5} {fila[1]:<20} {fila[2]:<30} {fila[3]:<15} {str(fila[4]):<8}")

def existeCliente(idCliente):
    encontrado = False 
    for i in range(len(matrizCliente)):
        if matrizCliente[i][0] == idCliente:
            encontrado = True
            break

    if not encontrado:
        print("El cliente no existe.")

    return encontrado

def obtenerCliente(idCliente):
    for i in range(len(matrizCliente)):
        if matrizCliente[i] [0] == idCliente:
            return matrizCliente[i]

def agregarAlCarrito():
    carrito = []
    
    while True:
        id_buscar = int(input("Ingrese el ID del producto que desea comprar: "))
        encontrado = False
            
        for producto in Producto.matrizProductos: 
            if producto[0] == id_buscar:
                encontrado = True
                cantidad = int(input(f"¿Cuántos {producto[1]} desea agregar al carrito?: "))
                if cantidad <= producto[3]: 
                    carrito.append([int(Ticket.matrizTicket[-1][0]) + 1, producto[0], cantidad, producto[2]*cantidad, True]) 
                    producto[3] -= cantidad 
                    print(f"{cantidad} unidades de {producto[1]} agregadas al carrito.")
                else:
                    print(f"No hay suficiente stock. Disponible: {producto[3]} unidades.")
                break 
            
        if not encontrado:
            print(f"No se encontró ningún producto con ID: {id_buscar}.")
        
        seleccion = input("Desea seguir agregando? (si/no) ")
        while seleccion.upper().strip() != "SI" and seleccion.upper().strip() != "NO":
            print("Error")
            seleccion = input("Desea seguir agregando? (si/no) ")
        if seleccion.upper().strip() == "NO":
            return carrito

def verCarrito(carrito):
    print("-"*55)  
    print(f'{"Producto":<25}{"Cantidad":<14}{"Precio":<8}')
    print("-"*55)       

    for producto in carrito:
        id, idProducto, cantidad, precio, estado = producto
        producto = Producto.obtenerProducto(idProducto)
        print(f'{producto[1]:<25}{cantidad:<14}{precio:<8}')

    print("-"*55)  

def vaciarCarrito(carrito):
    if not carrito:
        print("El carrito está vacío")
        return

    opcion = input("¿Seguro que quiere vaciar el carrito? (si/no)").lower()
    while opcion != "si" and opcion != "no":
        print("ERROR: Por favor ingrese si/no")
        opcion = input("¿Seguro que quiere vaciar el carrito? (si/no)").lower()

    if opcion == "si":
        print("Carrito vaciado.")
        carrito.clear() 
    else:
        print("Carrito no vaciado")


def buscarYVerCliente():
    print("Hola Mundo")

