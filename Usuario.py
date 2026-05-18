import Producto, Venta, Ticket, reporte, utilidades

def login():
    usuarioInput = input("Ingrese el usuario: ").strip().lower()
    for user in obtener_usuarios():
        if user[1].lower() == usuarioInput:
            if user[5] == "True":
                adminMenu()
            else:
                clienteMenu(user[0])
            return
    print("Usuario no encontrado.")

def mostrarClientes():
    print("\nListado de clientes:")
    for user in obtener_usuarios():
        estado = "Activo" if user[4] == "True" else "Inactivo"
        print(f"ID: {user[0]}, Nombre: {user[1]}, Email: {user[2]}, Teléfono: {user[3]}, Estado: {estado}")

def mostrarListaCliente():
    print(f"{'ID':<5} {'Nombre':<20} {'Email':<25} {'Telefono':<15} {'Activo':<8}")
    print("-" * 80)
    for user in obtener_usuarios():
        estado = verificar_Activo(user[4])
        print(f"{user[0]:<5}{user[1]:<20}{user[2]:<28}{user[3]:<15}{estado:<20}")

def altaCliente():
    """Dar de alta un nuevo cliente"""
    print("\n--- Registrarse ---")
    clienteNombre = input("Ingrese su nombre: ")

    clienteEmail = input("Ingrese su Email: ")
    while "@" not in clienteEmail or "." not in clienteEmail:
        print("Correo electrónico no válido.")
        clienteEmail = input("Ingrese su Email: ")

    clienteTelefono = input("Ingrese su número de contacto: ")
    while not clienteTelefono.isdigit() or len(clienteTelefono) < 7:
        print("Número de teléfono inválido.")
        clienteTelefono = input("Ingrese su número de contacto: ")

    try:
        nuevoId = obtener_ultimo_id('Archivos/archivoUsuario.txt') + 1
        with open('Archivos/archivoUsuario.txt', "a", encoding="utf-8") as arch:
            arch.write(f"{nuevoId};{clienteNombre};{clienteEmail};{clienteTelefono};True;False\n")
        print(f"Cliente '{clienteNombre}' (ID: {nuevoId}) dado de alta exitosamente.")
    except OSError as error:
        print("No se puede grabar el archivo:", error)

def bajaCliente():
    """Dar de baja un cliente existente"""
    print("\n--- Baja de cliente ---")
    usuarios = obtener_usuarios()
    if not usuarios:
        print("No hay clientes para dar de baja.")
        return

    mostrarListaCliente()
    idCliente = input("Ingrese el ID del cliente a dar de baja: ").strip()
    encontrado = False

    for user in usuarios:
        if user[0] == idCliente:
            encontrado = True
            if user[4] == "True":
                user[4] = "False"
                guardar_usuarios(usuarios)
                print(f"Cliente '{user[1]}' (ID: {idCliente}) dado de baja exitosamente.")
            else:
                print(f"Cliente '{user[1]}' (ID: {idCliente}) ya estaba dado de baja.")
                condicion = input("¿Querés darlo de alta ahora? (si/no): ").strip().lower()
                if condicion == "si":
                    user[4] = "True"
                    guardar_usuarios(usuarios)
                    print(f"Cliente '{user[1]}' dado de alta exitosamente.")
            return

    if not encontrado:
        print(f"No se encontró ningún cliente con ID: {idCliente}.")

def modificacionCliente():
    usuarios = obtener_usuarios()
    if not usuarios:
        print("No hay clientes para modificar.")
        return

    mostrarListaCliente()
    idCliente = input("Ingrese el ID del cliente a modificar: ").strip()

    for user in usuarios:
        if user[0] == idCliente:
            dato = input("Ingrese un nombre (deje vacío para no modificar): ")
            if dato.strip():
                user[1] = dato

            dato = input("Ingrese un email (deje vacío para no modificar): ")
            if dato.strip():
                user[2] = dato

            dato = input("Ingrese un teléfono (deje vacío para no modificar): ")
            if dato.strip():
                user[3] = dato

            guardar_usuarios(usuarios)
            print(f"Cliente '{user[1]}' (ID: {idCliente}) modificado correctamente.")
            return

    print("No se encontró el ID ingresado.")

def cambiarEstadoCliente():
    usuarios = obtener_usuarios()
    mostrarListaCliente()
    idCliente = input("\nIngrese el ID del cliente a modificar: ").strip()

    for user in usuarios:
        if user[0] == idCliente:
            if user[4] == "True":
                confirmar = input(f"El cliente {user[1]} está activo. ¿Dar de baja? (si/no): ").strip().lower()
                if confirmar == "si":
                    user[4] = "False"
                    guardar_usuarios(usuarios)
                    print(f"Cliente {user[1]} dado de baja.")
                else:
                    print("No se realizaron cambios.")
            else:
                confirmar = input(f"El cliente {user[1]} está inactivo. ¿Dar de alta? (si/no): ").strip().lower()
                if confirmar == "si":
                    user[4] = "True"
                    guardar_usuarios(usuarios)
                    print(f"Cliente {user[1]} dado de alta.")
                else:
                    print("No se realizaron cambios.")
            return

    print("No se encontró el cliente con ese ID.")

def existeCliente(idCliente):
    for user in obtener_usuarios():
        if user[0] == str(idCliente):
            return True
    print("El cliente no existe.")
    return False

def obtenerCliente(idCliente):
    for user in obtener_usuarios():
        if user[0] == str(idCliente):
            return user
    return None

def buscarVentasCliente():
    idCliente = input("Ingrese el ID del cliente: ").strip()
    encontrado = False

    for user in obtener_usuarios():
        if user[0] == idCliente:
            encontrado = True
            ventas = Venta.obtenerVentasPorCliente(int(idCliente))
            for venta in ventas:
                tickets = Ticket.obtenerTickets(venta['id_ticket'])
                print("-"*65)
                print(f'{"ID_Venta:":<5} {venta["id_venta"]} {"ID_Ticket:":>48} {venta["id_ticket"]}')
                print("-"*65)
                print(f'{"Producto":<40}{"Cantidad":<15}{"Subtotal $":<10}')
                for prod in tickets:
                    idTicket, idProducto, cantidad, subtotal, estadoTicket = prod
                    producto = Producto.obtenerProducto(idProducto)
                    print(f"{producto[1]:<43} {cantidad:<15} {subtotal:<10}")
                print("-"*65)
                print(f'Cliente: {user[0]} - {user[1]} {"Total:":>18} {venta["monto_total"]} - {venta["metodo_pago"]}')
                print("-"*65)

    if not encontrado:
        print("No se encontró el cliente indicado.")

def agregarAlCarrito():
    carrito = []
    while True:
        id_buscar = utilidades.pedirEntero("Ingrese el ID del producto que desea comprar: ")
        encontrado = False

        for producto in Producto.matrizProductos:
            if producto[0] == id_buscar:
                encontrado = True
                cantidad = utilidades.pedirEntero(f"¿Cuántos {producto[1]} desea agregar?: ")
                if cantidad <= producto[3]:
                    carrito.append([int(Ticket.matrizTicket[-1][0]) + 1, producto[0], cantidad, producto[2]*cantidad, True])
                    producto[3] -= cantidad
                    print(f"{cantidad} unidades de {producto[1]} agregadas al carrito.")
                else:
                    print(f"No hay suficiente stock. Disponible: {producto[3]} unidades.")
                break

        if not encontrado:
            print(f"No se encontró ningún producto con ese ID.")

        seleccion = input("¿Desea seguir agregando? (si/no): ").strip().upper()
        while seleccion not in ["SI", "NO"]:
            print("Error. Ingrese si o no.")
            seleccion = input("¿Desea seguir agregando? (si/no): ").strip().upper()
        if seleccion == "NO":
            return carrito

def verCarrito(carrito):
    print("-"*55)
    print(f'{"Producto":<25}{"Cantidad":<14}{"Precio":<8}')
    print("-"*55)
    for item in carrito:
        id, idProducto, cantidad, precio, estado = item
        producto = Producto.obtenerProducto(idProducto)
        print(f'{producto[1]:<25}{cantidad:<14}{precio:<8}')
    print("-"*55)

def vaciarCarrito(carrito):
    if not carrito:
        print("El carrito está vacío.")
        return
    opcion = input("¿Seguro que quiere vaciar el carrito? (si/no): ").strip().lower()
    while opcion not in ["si", "no"]:
        print("ERROR: Por favor ingrese si/no.")
        opcion = input("¿Seguro que quiere vaciar el carrito? (si/no): ").strip().lower()
    if opcion == "si":
        for item in carrito:
            for producto in Producto.matrizProductos:
                if producto[0] == item[1]:
                    producto[3] += item[2]
                    break
        carrito.clear()
        print("Carrito vaciado.")
    else:
        print("Carrito no vaciado.")

def gestionarUsuarios():
    opcion = -1
    while opcion != 0:
        print('''\n-- Menú de Usuarios --
        1 - Ver Clientes
        2 - Alta Cliente
        3 - Modificar Cliente
        4 - Activar / Dar de baja cliente
        5 - Buscar Ventas de Clientes
        6 - Dar de baja cliente
        0 - Volver al menú anterior''')
        opcion = utilidades.pedirEntero("Seleccione una opción: ")
        if opcion == 1:
            mostrarListaCliente()
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
    opcion = -1
    while opcion != 0:
        print('''\nMenu Principal
        1 - Gestionar Productos/Stock
        2 - Administrar Usuarios/Clientes
        3 - Gestionar Ventas
        4 - Gestionar Ticket
        5 - Reportes
        0 - Salir del sistema''')
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
            print("Saliendo del sistema...")
        else:
            print("Opción inválida. Intente nuevamente.")

def clienteMenu(idCliente):
    carrito = []
    opcion = -1
    while opcion != 0:
        print('''\nMenu Principal
        1 - Ver Productos
        2 - Agregar al Carrito
        3 - Vaciar Carrito
        4 - Ver Carrito
        5 - Finalizar compra
        0 - Salir del sistema''')
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
        elif opcion == 0:
            print("Volviendo al menú principal...")

def obtener_usuarios():
    usuarios = []
    try:
        with open('Archivos/archivoUsuario.txt', "rt", encoding="utf-8") as arch:
            for linea in arch:
                if linea.strip():
                    datos = linea.strip().split(";")
                    usuarios.append(datos)
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
    return usuarios

def guardar_usuarios(usuarios):
    try:
        with open('Archivos/archivoUsuario.txt', "wt", encoding="utf-8") as arch:
            for user in usuarios:
                arch.write(";".join(user) + "\n")
    except OSError as error:
        print("No se pudo guardar el archivo:", error)

def obtener_ultimo_id(archivo):
    ultimo_id = 0
    try:
        with open(archivo, "rt", encoding="utf-8") as arch:
            for linea in arch:
                datos = linea.strip().split(";")
                if datos[0].isdigit():
                    ultimo_id = int(datos[0])
    except FileNotFoundError:
        pass
    return ultimo_id

def verificar_Activo(activo):
    if activo == "True":
        return "SI"
    else:
        return "NO"