import Cliente, Ticket, Producto

matrizVenta = [[1, 123, 1, 744.0, True]]


def menuVenta():
    opcion = 1
    while opcion != 0:
        print('''
        --Menu Venta--
        '1 - Alta Venta
        '2 - Baja Venta
        '3 - Modificacion Venta
        '4 - Mostrar Venta
        '5 - Leer Venta
        '0 - Volver al menu principal''')

        opcion = int(input("Ingresa un numero: "))
        if opcion == 1:
            altaVenta()
       # if opcion == 2:
       #     bajaProducto()
       # if opcion == 3:
       #     modificacionProducto()
        if opcion == 4:
            mostrarVentas()
       # if opcion == 5:
       #     mostrarProducto()
        if opcion == 0:
            print("Adios!")     

def altaVenta():
    idCliente = int(input("Ingrese el ID del cliente: "))
    if Cliente.existeCliente(idCliente):
        ticketAuxiliar = Ticket.altaTicket(Ticket.matrizTicket, Producto.matrizProductos)
        total = Ticket.imprimir_ticket(Cliente.obtenerCliente(idCliente), ticketAuxiliar)
        Ticket.agregarTicket(ticketAuxiliar)
    
        matrizVenta.append([matrizVenta[-1][0] + 1, ticketAuxiliar[0][0], idCliente, total, True])

def mostrarVentas():
    for fila in matrizVenta:
        for elemento in fila:
            print(elemento, end=" ")
        print()   
    
    

menuVenta()