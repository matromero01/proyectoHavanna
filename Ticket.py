import Producto, Usuario, utilidades

ARCHIVO_TICKET = 'Archivos/archivoTicket.txt'

def ticketMenu():
    opcion = -1
    while opcion != 0:
        print('''
    ----------------------------
            MENU TICKET
        1 - Mostrar Ticket
        2 - Baja Ticket
        0 - Volver al menu principal
    ----------------------------''')

        opcion = utilidades.pedirEntero("Ingresa un numero: ")
        if opcion == 1:
            mostrarTicket()
        elif opcion == 2:
            id_ticket = utilidades.pedirEntero("Ingrese el ID del ticket a dar de baja: ")
            bajaTicket(id_ticket)
        elif opcion == 0:
            print("Adios!")

def altaTicket(carrito):
    tickets = obtener_tickets()
    tickets.extend(carrito)
    guardar_tickets(tickets)

def imprimir_ticket(cliente, carrito):
    total = 0

    print("-"*55)
    print(f"IdTicket --> {carrito[0][0]}")
    print("-"*55)

    print(f'{"PRODUCTO":<15}{"Cantidad":<16}{"Subtotal $":<10}')
    print("-"*55)

    for linea in carrito:
        idTicket, idProducto, cantidad, subtotal, estadoTicket = linea
        producto = Producto.obtenerProducto(idProducto)
        print(f"{producto[1]:<25} {cantidad:<16} {subtotal:<10}")
        total += subtotal

    print("-"*55)
    print(f"Total --> {total}")
    print("-"*55)

    idCliente, nombre, mail, telefono, estadoCliente, *resto = cliente
    print(f"Cliente --> {nombre}")
    print("-"*55)

    return total

def bajaTicket(id_ticket):
    tickets = obtener_tickets()
    encontrado = False
    for ticket in tickets:
        if ticket[0] == id_ticket:
            ticket[4] = False
            encontrado = True
    if encontrado:
        guardar_tickets(tickets)
        print(f"Ticket {id_ticket} dado de baja exitosamente.")
    else:
        print(f"No se encontró el ticket con ID: {id_ticket}.")

def mostrarTicket():
    tickets = obtener_tickets()
    if not tickets:
        print("No hay tickets registrados.")
        return
    print("-"*55)
    print(f'{"Id_Ticket":<15}{"Id_Producto":<15}{"Cantidad":<16}{"Subtotal $":<10}')
    print("-"*55)
    for ticket in tickets:
        id_ticket, id_producto, cantidad, subtotal, estado = ticket
        if estado:
            print(f"{id_ticket:<15} {id_producto:<15} {cantidad:<13} {subtotal:.2f}")

def obtenerTickets(idTicket):
    return [t for t in obtener_tickets() if t[0] == int(idTicket)]

def obtenerUltimoIdTicket():
    tickets = obtener_tickets()
    if not tickets:
        return 0
    return max(t[0] for t in tickets)

def obtener_tickets():
    tickets = []
    try:
        with open(ARCHIVO_TICKET, "rt", encoding="utf-8") as arch:
            for linea in arch:
                if linea.strip():
                    datos = linea.strip().split(";")
                    ticket = [
                        int(datos[0]),    # id_ticket
                        int(datos[1]),    # id_producto
                        int(datos[2]),    # cantidad
                        float(datos[3]),  # subtotal
                        datos[4] == "True" # activo
                    ]
                    tickets.append(ticket)
    except FileNotFoundError:
        pass
    return tickets

def guardar_tickets(tickets):
    try:
        with open(ARCHIVO_TICKET, "wt", encoding="utf-8") as arch:
            for ticket in tickets:
                arch.write(f"{ticket[0]};{ticket[1]};{ticket[2]};{ticket[3]};{ticket[4]}\n")
    except OSError as error:
        print("No se pudo guardar el archivo:", error)