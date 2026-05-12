import Producto, Venta, Ticket, utilidades, re

#IdUsuario
matrizUsuario = [
    [1,  "Admin",              "admin@gmail.com",           "12345678",   True, True],
    [2,  "Facundo Mello",      "facundomello34@gmail.com",  "1124084431", True, False],
    [3,  "Lionel Messi",       "messi@gmail.com",           "1122334455", True, False],
    [4,  "Juan Perez",         "juanperez@gmail.com",       "1156781234", True, False],
    [5,  "Maria Lopez",        "marialopez@hotmail.com",    "1167894321", True, False],
    [6,  "Carlos Gomez",       "carlosgomez@yahoo.com",     "1178905678", False, False],
    [7,  "Laura Fernandez",    "lauraf@gmail.com",          "1189016789", True, False],
    [8,  "Diego Martinez",     "diegom@outlook.com",        "1190127890", True, False],
    [9,  "Ana Rodriguez",      "anar@gmail.com",            "1101238901", False, False],
]

def login():
    usuario = input("Ingrese el usuario: ").strip().lower()

    for user in matrizUsuario:
        if user[1].lower() == usuario:
            if user[5]:
                adminMenu()
            else:
                clienteMenu(user[0])
            return        
    print("Usuario no encontrado.")


def mostrarClientes():
    print("\nListado de clientes:")
    for cliente in matrizUsuario:
        estado = "Activo" if cliente[4] else "Inactivo"
        print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}, Teléfono: {cliente[3]}, Estado: {estado}")


def cambiarEstadoCliente():
    mostrarClientes()
    id_cliente = int(input("\nIngrese el ID del cliente a modificar: "))
    for cliente in matrizUsuario:
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
        '1 - Ver Clientes
        '2 - Alta Cliente
        '3 - Modificar Cliente
        '4 - Activar / Dar de baja cliente
        '5 - Buscar Ventas de Clientes
        '6 - Dar de baja cliente
        '0 - Volver al menú anterior''')

        opcion = utilidades.pedirEntero("Seleccione una opción: ")
        if opcion == 1:
            mostrarClientes()
        elif opcion == 2:
            altaCliente()
        elif opcion == 3:
            modificacionCliente()
        elif opcion == 4:
            cambiarEstadoCliente()
        elif opcion == 5:
            buscarVentasCliente()
        elif opcion == 6:
            bajaCliente()
        elif opcion == 0:
            print("Volviendo al menú anterior...")
        else:
            print("Opción inválida. Intente nuevamente.")

def adminMenu():
    import reporte
    opcion = 1
    while opcion != 0:
        print('''Menu Principal
        '1 - Gestionar Productos/Stock
        '2 - Administrar Usuarios/Clientes
        '3 - Gestionar Ventas
        '4 - Gestionar Ticket
        '5 - Reportes
        '0 - Salir del sistema''')

        opcion = utilidades.pedirEntero("Seleccione una opción: ")
        if opcion == 1:
            Producto.productoMenu()
        elif opcion == 2:
            gestionarUsuarios()
        elif opcion == 3:
            Venta.menuVenta()
        elif opcion == 4:
            Ticket.ticketMenu()
        elif opcion == 5:
            reporte.menuReportes()
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

        opcion = utilidades.pedirEntero("Seleccione una opción: ")
        if opcion == 1:
            Producto.mostrarListaProducto(es_cliente="false")
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

PATRON_EMAIL    = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"
PATRON_TELEFONO = r"\d{10,12}"

def altaCliente():
    print("\n--- Registrarse ---")
    clienteNombre = input("Ingrese su nombre: ")

    clienteEmail = input("Ingrese su Email: ")
    while not re.fullmatch(PATRON_EMAIL, clienteEmail):
        print("Correo electrónico no válido. Debe tener formato usuario@dominio.com")
        clienteEmail = input("Ingrese su Email: ")

    clienteTelefono = input("Ingrese su número de contacto: ")
    while not re.fullmatch(PATRON_TELEFONO, clienteTelefono):
        print("Teléfono inválido. Debe tener entre 10 y 12 dígitos.")
        clienteTelefono = input("Ingrese su número de contacto: ")

    nuevoId = matrizCliente[-1][0] + 1 if matrizCliente else 1
    nuevoCliente = [nuevoId, clienteNombre, clienteEmail, clienteTelefono, True]
    matrizCliente.append(nuevoCliente)
    print(f"Cliente '{clienteNombre}' (ID: {nuevoId}) dado de alta exitosamente.")

def bajaCliente(): 
    """ Dar de baja un cliente existente"""
    print("\n--- Baja de cliente ---")
    if not matrizUsuario:
        print("No hay clientes para eliminar.")
    else: 
        idCliente = int(input("Ingrese el ID del cliente a dar de baja: "))
        encontrado = False


        for i in range(len(matrizUsuario)):
            cliente = matrizUsuario[i][1]
            if matrizUsuario[i] [0] == idCliente:
                encontrado = True
                if matrizUsuario[i][4] == True:
                    matrizUsuario[i] [4] = False
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
    if not matrizUsuario:
        print("No hay cliente para modificar.")
    else:
        mostrarListaCliente() 
        idCliente = int(input("Ingrese el ID del cliente para modificar: "))

        for i in range(len(matrizUsuario)): 
            if matrizUsuario[i][0] == idCliente:
                id, nombre, mail, numero, activo =matrizUsuario[i]

                datoModificado = input("Ingrese un nombre: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizUsuario[i][1] = datoModificado
                
                datoModificado = input("Ingrese un mail: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizUsuario[i][2] = datoModificado
                
                datoModificado = input("Ingrese un numero: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizUsuario[i][3] = datoModificado

                print(f"Cliente '{nombre}' (ID: {idCliente}) fue modificado correctamente")
                return
        print("Opción inválida: El ID ingresado no existe.")      

def mostrarListaCliente():
    print(f"{'ID':<5} {'Nombre':<20} {'Email':<30} {'Telefono':<15} {'Activo':<8}")
    print("-" * 80)
    for fila in matrizUsuario:
        print(f"{fila[0]:<5} {fila[1]:<20} {fila[2]:<30} {fila[3]:<15} {str(fila[4]):<8}")

def existeCliente(idCliente):
    encontrado = False
    i = 0
    while i < len(matrizUsuario) and not encontrado:
        if matrizUsuario[i][0] == idCliente:
            encontrado = True
        i += 1
    if not encontrado:
        print("El cliente no existe.")
    return encontrado

def obtenerCliente(idCliente):
    i = 0
    while i < len(matrizUsuario):
        if matrizUsuario[i][0] == idCliente:
            return matrizUsuario[i]
        i += 1

def agregarAlCarrito():
    carrito = []
    
    while True:
        id_buscar = int(input("Ingrese el ID del producto que desea comprar: "))
        encontrado = False

        i = 0
        while i < len(Producto.matrizProductos):
            producto = Producto.matrizProductos[i]
            if producto[0] == id_buscar:
                encontrado = True
                cantidad = int(input(f"¿Cuántos {producto[1]} desea agregar al carrito?: "))
                if cantidad <= producto[3]:
                    carrito.append([int(Ticket.matrizTicket[-1][0]) + 1, producto[0], cantidad, producto[2]*cantidad, True])
                    producto[3] -= cantidad
                    print(f"{cantidad} unidades de {producto[1]} agregadas al carrito")
                else:
                    print (f"No hay suficiente stock. Disponible: {producto[3]} unidades.")
                break
            i += 1
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
        for item in carrito:
            id_producto = item[1]
            cantidad = item[2]
            for producto in Producto.matrizProductos:
                if producto[0] == id_producto:
                    producto[3] += cantidad
                    break
        carrito.clear() 
        print("Carrito vaciado.")
    else:
        print("Carrito no vaciado")


def buscarVentasCliente():
    idCliente = int(input("Ingrese el ID del cliente: "))

    encontrado = False
    for cliente in matrizUsuario:
        if cliente[0] == idCliente: 
            encontrado = True
            ventas = Venta.obtenerVentasPorCliente(idCliente)
            for venta in ventas:
                
                tickets = Ticket.obtenerTickets(venta['id_ticket'])

                idCliente, nombreCliente, mail, numero, estadoCliente = cliente

                print("-"*65)  
            
                print(f'{"ID_Venta:":<5} {venta["id_venta"]} {"ID_Ticket: ":>48} {venta["id_ticket"]}')
            
                print("-"*65)

                print(f'{"Producto":<40}{"Cantidad":<15}{"Subtotal $":<10}')

                for prod in tickets:
                    idTicket, idProducto, cantidad, subtotal, estadoTicket = prod
                    producto = Producto.obtenerProducto(idProducto)
                    print(f"{producto[1]:<43} {cantidad:<15} {subtotal:<10}")

                print("-"*65)  

                print(f'{"Cliente: "} {idCliente} - {nombreCliente} {"Total: ":>18} {venta["monto_total"]} - {venta["metodo_pago"]}')

                print("-"*65) 
    
    if not encontrado:
        print("No se encontro la venta indicada.")
    else :
        return


