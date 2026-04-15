import Cliente, Ticket, Producto

listaVentas = [
    {"id_venta": 1, "id_ticket": 123, "id_cliente": 1, "monto_total": 744.0, "metodo_pago": "efectivo", "fecha": "2025-06-01"},
    {"id_venta": 2, "id_ticket": 124, "id_cliente": 3, "monto_total": 370.0, "metodo_pago": "tarjeta",  "fecha": "2025-06-02"},
    {"id_venta": 3, "id_ticket": 125, "id_cliente": 2, "monto_total": 520.0, "metodo_pago": "efectivo", "fecha": "2025-06-02"},
    {"id_venta": 4, "id_ticket": 126, "id_cliente": 1, "monto_total": 290.0, "metodo_pago": "transferencia", "fecha": "2025-06-03"},
    {"id_venta": 5, "id_ticket": 127, "id_cliente": 4, "monto_total": 180.0, "metodo_pago": "tarjeta",  "fecha": "2025-06-03"},
]

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
        if ticketAuxiliar:  # Validar que el ticket se creó correctamente
            total = Ticket.imprimir_ticket(Cliente.obtenerCliente(idCliente), ticketAuxiliar)
            Ticket.agregarTicket(ticketAuxiliar)
        
            nuevo_id = listaVentas[-1]["id_venta"] + 1 if listaVentas else 1
            listaVentas.append({"id_venta": nuevo_id, "id_ticket": ticketAuxiliar[0][0], "id_cliente": idCliente, "monto_total": total, "metodo_pago": "pendiente", "fecha": "2025-06-04"})
            print("Venta registrada exitosamente.")
    else:
        print("El cliente no existe o está dado de baja.")

def mostrarVentas():
    if not listaVentas:
        print("No hay ventas registradas.")
    else:
        for venta in listaVentas:
            print(f"ID Venta: {venta['id_venta']}, Ticket: {venta['id_ticket']}, Cliente: {venta['id_cliente']}, Total: ${venta['monto_total']:.2f}")