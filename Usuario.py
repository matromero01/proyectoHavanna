import Producto, Venta, Ticket, reporte, utilidades
import json
import os

ARCHIVO_USUARIOS = 'Archivos/archivoUsuario.json'

def obtener_usuarios():
    try:
        with open(ARCHIVO_USUARIOS, "rt", encoding="utf-8") as arch:
            return json.load(arch)
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
        return []
    except json.JSONDecodeError:
        print("Error al leer el archivo de usuarios.")
        return []

def guardar_usuarios(usuarios):
    try:
        with open(ARCHIVO_USUARIOS, "wt", encoding="utf-8") as arch:
            json.dump(usuarios, arch, ensure_ascii=False, indent=4)
    except OSError as error:
        print("No se pudo guardar el archivo:", error)

def obtener_ultimo_id():
    usuarios = obtener_usuarios()
    if not usuarios:
        return 0
    return max(user["id"] for user in usuarios)

def usuarioExiste(usuario):
    usuarioLimpio = usuario.strip().lower().replace(" ", "")
    for user in obtener_usuarios():
        if user["usuario"].strip().lower().replace(" ", "") == usuarioLimpio:
            return True
    return False

def login(intentos=3):
    if intentos == 0:
        print("Demasiados intentos fallidos. Acceso bloqueado.")
        return
    
    usuarioInput = input("Ingrese el usuario: ").strip().lower()
    for user in obtener_usuarios():
        if user["usuario"].lower() == usuarioInput:
            if not user["activo"]:
                print("Usuario dado de baja. Contacte al administrador.")
                return
            if user["esAdmin"]:
                adminMenu()
            else:
                clienteMenu(user["id"])
            return
    
    print(f"Usuario no encontrado. Intentos restantes: {intentos - 1}")
    login(intentos - 1)

def mostrarClientes():
    print("\nListado de clientes:")
    for user in obtener_usuarios():
        estado = "Activo" if user["activo"] else "Inactivo"
        print(f"ID: {user['id']}, Usuario: {user['usuario']}, Nombre: {user['nombre']}, Email: {user['email']}, Teléfono: {user['telefono']}, Estado: {estado}")

def mostrarListaCliente():
    print(f"{'ID':<5} {'Usuario':<15} {'Nombre':<20} {'Email':<27} {'Telefono':<12} {'Activo':<8}")
    print("-" * 95)
    for user in obtener_usuarios():
        estado = "True" if user["activo"] else "False"
        print(f"{user['id']:<5}{user['usuario']:<15}{user['nombre']:<20}{user['email']:<30}{user['telefono']:<15}{estado:<8}")

def altaCliente():
    """Dar de alta un nuevo cliente"""
    print("\n--- Registrarse ---")

    clienteUsuario = input("Ingrese su nombre de usuario: ").strip()

    if usuarioExiste(clienteUsuario):
        usuarios = obtener_usuarios()
        for user in usuarios:
            if user["usuario"].strip().lower().replace(" ", "") == clienteUsuario.strip().lower().replace(" ", ""):
                if not user["activo"]:
                    confirmar = input(f"El usuario '{user['usuario']}' está dado de baja. ¿Querés reactivarlo? (si/no): ").strip().lower()
                    if confirmar == "si":
                        user["activo"] = True
                        guardar_usuarios(usuarios)
                        print(f"Usuario '{user['usuario']}' reactivado exitosamente.")
                    else:
                        print("No se realizaron cambios.")
                else:
                    print(f"Ya existe un usuario activo con el nombre '{clienteUsuario}'.")
                return

    clienteNombre = input("Ingrese su nombre completo: ")

    clienteEmail = input("Ingrese su Email: ")
    while "@" not in clienteEmail or "." not in clienteEmail:
        print("Correo electrónico no válido.")
        clienteEmail = input("Ingrese su Email: ")

    clienteTelefono = input("Ingrese su número de contacto: ")
    while not clienteTelefono.isdigit() or len(clienteTelefono) < 7:
        print("Número de teléfono inválido.")
        clienteTelefono = input("Ingrese su número de contacto: ")

    nuevoUsuario = {
        "id": obtener_ultimo_id() + 1,
        "usuario": clienteUsuario,
        "nombre": clienteNombre,
        "email": clienteEmail,
        "telefono": clienteTelefono,
        "activo": True,
        "esAdmin": False
    }

    usuarios = obtener_usuarios()
    usuarios.append(nuevoUsuario)
    guardar_usuarios(usuarios)
    print(f"Cliente '{clienteNombre}' (ID: {nuevoUsuario['id']}) dado de alta exitosamente.")

def bajaCliente():
    """Dar de baja un cliente existente"""
    print("\n--- Baja de cliente ---")
    usuarios = obtener_usuarios()
    if not usuarios:
        print("No hay clientes para dar de baja.")
        return

    mostrarListaCliente()
    idCliente = utilidades.pedirEntero("Ingrese el ID del cliente a dar de baja: ")
    encontrado = False

    for user in usuarios:
        if user["id"] == idCliente:
            encontrado = True
            if user["activo"]:
                user["activo"] = False
                guardar_usuarios(usuarios)
                print(f"Cliente '{user['nombre']}' (ID: {idCliente}) dado de baja exitosamente.")
            else:
                print(f"Cliente '{user['nombre']}' (ID: {idCliente}) ya estaba dado de baja.")
                condicion = input("¿Querés darlo de alta ahora? (si/no): ").strip().lower()
                if condicion == "si":
                    user["activo"] = True
                    guardar_usuarios(usuarios)
                    print(f"Cliente '{user['nombre']}' dado de alta exitosamente.")
            return

    if not encontrado:
        print(f"No se encontró ningún cliente con ID: {idCliente}.")

def modificacionCliente():
    usuarios = obtener_usuarios()
    if not usuarios:
        print("No hay clientes para modificar.")
        return

    mostrarListaCliente()
    idCliente = utilidades.pedirEntero("Ingrese el ID del cliente a modificar: ")

    for user in usuarios:
        if user["id"] == idCliente:
            dato = input("Ingrese un usuario (deje vacío para no modificar): ").strip()
            if dato:
                if usuarioExiste(dato) and dato.lower() != user["usuario"].lower():
                    print("Ese nombre de usuario ya existe.")
                    return
                user["usuario"] = dato

            dato = input("Ingrese un nombre completo (deje vacío para no modificar): ").strip()
            if dato:
                user["nombre"] = dato

            dato = input("Ingrese un email (deje vacío para no modificar): ").strip()
            if dato:
                user["email"] = dato

            dato = input("Ingrese un teléfono (deje vacío para no modificar): ").strip()
            if dato:
                user["telefono"] = dato

            guardar_usuarios(usuarios)
            print(f"Cliente '{user['nombre']}' (ID: {idCliente}) modificado correctamente.")
            return

    print("No se encontró el ID ingresado.")

def cambiarEstadoCliente():
    usuarios = obtener_usuarios()
    mostrarListaCliente()
    idCliente = utilidades.pedirEntero("\nIngrese el ID del cliente a modificar: ")

    for user in usuarios:
        if user["id"] == idCliente:
            if user["activo"]:
                confirmar = input(f"El cliente {user['nombre']} está activo. ¿Dar de baja? (si/no): ").strip().lower()
                if confirmar == "si":
                    user["activo"] = False
                    guardar_usuarios(usuarios)
                    print(f"Cliente {user['nombre']} dado de baja.")
                else:
                    print("No se realizaron cambios.")
            else:
                confirmar = input(f"El cliente {user['nombre']} está inactivo. ¿Dar de alta? (si/no): ").strip().lower()
                if confirmar == "si":
                    user["activo"] = True
                    guardar_usuarios(usuarios)
                    print(f"Cliente {user['nombre']} dado de alta.")
                else:
                    print("No se realizaron cambios.")
            return

    print("No se encontró el cliente con ese ID.")

def existeCliente(idCliente):
    for user in obtener_usuarios():
        if user["id"] == idCliente:
            return True
    print("El cliente no existe.")
    return False

def obtenerCliente(idCliente):
    for user in obtener_usuarios():
        if user["id"] == idCliente:
            return [user["id"], user["usuario"], user["nombre"], user["email"], user["telefono"], user["activo"], user["esAdmin"]]
    return None 

def buscarVentasCliente():
    idCliente = utilidades.pedirEntero("Ingrese el ID del cliente: ")
    encontrado = False

    for user in obtener_usuarios():
        if user["id"] == idCliente:
            encontrado = True
            ventas = Venta.obtenerVentasPorCliente(idCliente)
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
                print(f'Cliente: {user["id"]} - {user["nombre"]} {"Total:":>18} {venta["monto_total"]} - {venta["metodo_pago"]}')
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
                    carrito.append([Ticket.obtenerUltimoIdTicket() + 1, producto[0], cantidad, (producto[2]*cantidad), True])
                    producto[3] -= cantidad
                    print(f"{cantidad} unidades de {producto[1]} agregadas al carrito.")
                else:
                    print(f"No hay suficiente stock. Disponible: {producto[3]} unidades.")
                break

        if not encontrado:
            print("No se encontró ningún producto con ese ID.")

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
        4 - Buscar Ventas de Clientes
        5 - Dar de baja cliente
        0 - Volver al menú anterior''')
        opcion = utilidades.pedirEntero("Seleccione una opción: ")
        if opcion == 1:
            mostrarListaCliente()
        elif opcion == 2:
            altaCliente()
        elif opcion == 3:
            modificacionCliente()
        elif opcion == 4:
            buscarVentasCliente()
        elif opcion == 5:
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
        0 - Cerrar sesion''')
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
        0 - Cerrar sesion''')
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