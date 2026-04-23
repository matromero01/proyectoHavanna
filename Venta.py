import Cliente, Ticket, Producto

listaVentas = [
    {"id_venta": 1, "id_ticket": 123, "id_cliente": 1, "monto_total": 744.0, "metodo_pago": "efectivo", "fecha": "2025-06-01", "estado": True},
    {"id_venta": 2, "id_ticket": 124, "id_cliente": 3, "monto_total": 370.0, "metodo_pago": "tarjeta",  "fecha": "2025-06-02", "estado": True},
    {"id_venta": 3, "id_ticket": 125, "id_cliente": 2, "monto_total": 520.0, "metodo_pago": "efectivo", "fecha": "2025-06-02", "estado": True},
    {"id_venta": 4, "id_ticket": 126, "id_cliente": 1, "monto_total": 290.0, "metodo_pago": "transferencia", "fecha": "2025-06-03", "estado": True},
    {"id_venta": 5, "id_ticket": 127, "id_cliente": 4, "monto_total": 180.0, "metodo_pago": "tarjeta",  "fecha": "2025-06-03", "estado": True},
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
        '0 - Volver al menu principal''')

        opcion = int(input("Ingresa un numero: "))
        if opcion == 1:
            altaVenta()
        if opcion == 2:
            bajaVenta()
        if opcion == 3:
            modificacionProducto()
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
            listaVentas.append({"id_venta": nuevo_id, "id_ticket": ticketAuxiliar[0][0], "id_cliente": idCliente, "monto_total": total, "metodo_pago": "pendiente", "fecha": "2025-06-04", "estado": True})
            print("Venta registrada exitosamente.")
    else:
        print("El cliente no existe o está dado de baja.")

def mostrarVentas():
    if not listaVentas:
        print("No hay ventas registradas.")
    else:
        print("-"*70)  
        print(f'{"ID_Venta":<15}{"Ticket":<15}{"Cliente":<16}{"Metodo de Pago":<18}{"Total $":<10}')
        print("-"*70)  
        for venta in listaVentas:
            if venta['estado']:
                  
                print(f"{venta['id_venta']:<15} {venta['id_ticket']:<15} {venta['id_cliente']:<13} {venta['metodo_pago']:<18} {venta['monto_total']:.2f}")


def bajaVenta():
    print("| Baja de la Venta |")
    idVenta = int(input("Ingrese el ID de la venta: "))
    for venta in listaVentas:
        if venta['id_venta'] == idVenta:
            if venta['estado']:
                while True:
                    confirmacion = input(f"Desea confirmar la baja de la venta #{venta['id_venta']}? (si/no) ")

                    if confirmacion.upper().strip() == 'SI':
                        venta['estado'] = False
                        print(f"Confirmacion de la baja. Venta #{venta['id_venta']}!")
                        return
                    elif confirmacion.upper().strip() == 'NO': 
                        print("Saliendo de la baja de venta...")
                        return
                    else:
                        print("Error. Ingrese si o no.")


def modificacionProducto():
    print("| Modificacion de la Venta |")
    
    idVenta = int(input("Ingrese el ID de la venta: "))
    encontrado = False

    for venta in listaVentas:
        if venta['id_venta'] == idVenta:
            encontrado = True
            print(f"Venta encontrada. Metodo de pago actual: {venta['metodo_pago']}")
            
            opcion = 0

            while opcion not in [1, 2, 3]:
                print("\nSeleccione el nuevo metodo de pago:")
                print("1. Efectivo")
                print("2. Tarjeta")
                print("3. Transferencia")

                entrada = input("Seleccione nuevo metodo de pago (1-3): ")
                if entrada.isdigit():
                    opcion = int(entrada)
                    
                    if opcion not in [1, 2, 3]:
                        print("Error: El numero debe ser 1, 2, o 3")
                else:

                    print("Error: Por favor ingrese solo numeros (1-3)")
            
            metodos = {1: "efectivo", 2: "tarjeta", 3: "transferencia"}
            venta['metodo_pago'] = metodos[opcion]
            
            print(f"\nCambio de metodo de pago exitoso a: {venta['metodo_pago']}")
            break 
            
    if not encontrado:
        print("ID incorrecto (No se encontro la venta)")
            


            
     
