import Usuario, Ticket, Producto, utilidades

ARCHIVO_VENTA = 'Archivos/archivoVenta.txt'

# CODIGO ANSI
RESET = "\33[0m"
VERDE = "\33[32;1m"
ROJO = "\33[31;1m"

MetodosPago = ("efectivo", "tarjeta", "transferencia")

def obtener_ventas():
    ventas = []
    try:
        with open(ARCHIVO_VENTA, "rt", encoding="utf-8") as arch:
            for linea in arch:
                if linea.strip():
                    datos = linea.strip().split(";")
                    venta = {
                        "id_venta":   int(datos[0]),
                        "id_ticket":  int(datos[1]),
                        "id_cliente": int(datos[2]),
                        "monto_total": float(datos[3]),
                        "metodo_pago": datos[4],
                        "fecha":       datos[5],
                        "estado":      datos[6] == "True"
                    }
                    ventas.append(venta)
    except FileNotFoundError:
        pass
    return ventas

def guardar_ventas(ventas):
    try:
        with open(ARCHIVO_VENTA, "wt", encoding="utf-8") as arch:
            for venta in ventas:
                arch.write(f"{venta['id_venta']};{venta['id_ticket']};{venta['id_cliente']};{venta['monto_total']};{venta['metodo_pago']};{venta['fecha']};{venta['estado']}\n")
    except OSError as error:
        print("No se pudo guardar el archivo:", error)

def obtener_ultimo_id():
    ventas = obtener_ventas()
    if not ventas:
        return 0
    return max(v["id_venta"] for v in ventas)

def menuVenta():
    opcion = -1
    while opcion != 0:
        print('''
        --Menu Venta--
        1 - Modificacion Venta
        2 - Mostrar Venta
        3 - Leer venta
        4 - Baja Venta
        0 - Volver al menu principal''')

        opcion = utilidades.pedirEntero("Ingresa un numero: ")
        if opcion == 1:
            modificacionVenta()
        elif opcion == 2:
            mostrarVentas()
        elif opcion == 3:
            leerVenta()
        elif opcion == 4:
            bajaVenta()

def altaVenta(idCliente, carrito):
    import reporte
    if carrito:
        Ticket.altaTicket(carrito)
        total = Ticket.imprimir_ticket(Usuario.obtenerCliente(idCliente), carrito)

        print("Seleccione metodo de pago:")
        for i, metodo in enumerate(MetodosPago):
            print(f"{i+1}. {metodo.capitalize()}")
        opcionPago = utilidades.pedirEntero("Ingrese opcion: ")
        while opcionPago not in [1, 2, 3]:
            print("Opcion invalida")
            opcionPago = utilidades.pedirEntero("Ingrese opcion: ")
        metodoPago = MetodosPago[opcionPago - 1]

        nuevo_id = obtener_ultimo_id() + 1
        nueva_venta = {
            "id_venta":    nuevo_id,
            "id_ticket":   carrito[0][0],
            "id_cliente":  idCliente,
            "monto_total": total,
            "metodo_pago": metodoPago,
            "fecha":       "2026-04-06",
            "estado":      True
        }
        ventas = obtener_ventas()
        ventas.append(nueva_venta)
        guardar_ventas(ventas)
        print(f"{VERDE}Compra realizada correctamente.{RESET}")

        cliente = Usuario.obtenerCliente(idCliente)
        reporte.registrarCompra(cliente, carrito)

def mostrarVentas():
    ventas = obtener_ventas()
    if not ventas:
        print("No hay ventas registradas.")
        return
    print("-"*90)
    print(f'{"ID_Venta":<15}{"Ticket":<15}{"Cliente":<16}{"Metodo de Pago":<18}{"Total $":<10}')
    print("-"*90)
    for venta in ventas:
        if venta['estado']:
            print(f"{venta['id_venta']:<15} {venta['id_ticket']:<15} {venta['id_cliente']:<13} {venta['metodo_pago']:<18} {venta['monto_total']:.2f}")

def bajaVenta():
    print("| Baja de la Venta |")
    ventas = obtener_ventas()
    idVenta = utilidades.pedirEntero("Ingrese el ID de la venta: ")

    for venta in ventas:
        if venta['id_venta'] == idVenta:
            if venta['estado']:
                while True:
                    confirmacion = input(f"Desea confirmar la baja de la venta #{venta['id_venta']}? (si/no) ").upper().strip()
                    if confirmacion == 'SI':
                        venta['estado'] = False
                        guardar_ventas(ventas)
                        print(f"Confirmacion de la baja. Venta #{venta['id_venta']}!")
                        return
                    elif confirmacion == 'NO':
                        print("Saliendo de la baja de venta...")
                        return
                    else:
                        print("Error. Ingrese si o no.")
            else:
                print(f"La venta #{idVenta} ya estaba dada de baja.")
                return

    print("No se encontró la venta indicada.")

def modificacionVenta():
    print("| Modificacion de la Venta |")
    ventas = obtener_ventas()
    print("-"*90)
    print(f'{"ID_Venta":<15}{"Ticket":<15}{"Cliente":<16}{"Metodo de Pago":<18}{"Total $":<10}')
    print("-"*90)
    for venta in ventas:
        if venta['estado']:
            print(f"{venta['id_venta']:<15} {venta['id_ticket']:<15} {venta['id_cliente']:<13} {venta['metodo_pago']:<18} {venta['monto_total']:.2f}")

    idVenta = utilidades.pedirEntero("Ingrese el ID de la venta: ")
    encontrado = False

    for venta in ventas:
        if venta['id_venta'] == idVenta:
            encontrado = True
            print(f"Venta encontrada. Metodo de pago actual: {venta['metodo_pago']}")

            opcion = 0
            while opcion not in [1, 2, 3]:
                print("\nSeleccione el nuevo metodo de pago:")
                for i, metodo in enumerate(MetodosPago):
                    print(f"{i+1}. {metodo.capitalize()}")
                entrada = input("Seleccione nuevo metodo de pago (1-3): ")
                if entrada.isdigit():
                    opcion = int(entrada)
                    if opcion not in [1, 2, 3]:
                        print("Error: El numero debe ser 1, 2, o 3")
                else:
                    print("Error: Por favor ingrese solo numeros (1-3)")

            venta['metodo_pago'] = MetodosPago[opcion - 1]
            guardar_ventas(ventas)
            print(f"\nCambio de metodo de pago exitoso a: {venta['metodo_pago']}")
            break

    if not encontrado:
        print("ID incorrecto (No se encontro la venta)")

def leerVenta():
    ventas = obtener_ventas()
    idVenta = utilidades.pedirEntero("Ingrese el ID de la venta: ")

    for venta in ventas:
        if venta['id_venta'] == idVenta:
            cliente = Usuario.obtenerCliente(venta['id_cliente'])
            tickets = Ticket.obtenerTickets(venta['id_ticket'])

            nombreCliente = cliente[2] if isinstance(cliente, list) else cliente["nombre"]
            idCliente = cliente[0] if isinstance(cliente, list) else cliente["id"]

            print("-"*65)
            print(f'{"ID_Venta:":<5} {venta["id_venta"]} {"ID_Ticket:":>48} {venta["id_ticket"]}')
            print("-"*65)
            print(f'{"Producto":<40}{"Cantidad":<15}{"Subtotal $":<10}')

            for prod in tickets:
                idTicket, idProducto, cantidad, subtotal, estadoTicket = prod
                producto = Producto.obtenerProducto(idProducto)
                print(f"{producto[1]:<43} {cantidad:<15} {subtotal:<10}")

            print("-"*65)
            print(f'{"Cliente:"} {idCliente} - {nombreCliente} {"Total:":>18} {venta["monto_total"]} - {venta["metodo_pago"]}')
            print("-"*65)
            return

    print("No se encontro la venta indicada.")

def obtenerVentasPorCliente(id_cliente):
    return [v for v in obtener_ventas() if v['id_cliente'] == id_cliente]