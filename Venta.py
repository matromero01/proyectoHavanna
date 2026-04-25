import Usuario, Ticket, Producto

listaVentas = [
    {"id_venta": 1, "id_ticket": 123, "id_cliente": 1, "monto_total": 744.0, "metodo_pago": "efectivo", "fecha": "2025-06-01", "estado": True},
    {"id_venta": 2, "id_ticket": 124, "id_cliente": 3, "monto_total": 370.0, "metodo_pago": "tarjeta",  "fecha": "2025-06-02", "estado": True},
    {"id_venta": 3, "id_ticket": 125, "id_cliente": 2, "monto_total": 520.0, "metodo_pago": "efectivo", "fecha": "2025-06-02", "estado": True},
    {"id_venta": 4, "id_ticket": 126, "id_cliente": 1, "monto_total": 290.0, "metodo_pago": "transferencia", "fecha": "2025-06-03", "estado": True},
    {"id_venta": 5, "id_ticket": 127, "id_cliente": 4, "monto_total": 180.0, "metodo_pago": "tarjeta",  "fecha": "2025-06-03", "estado": True},
]

# CODIGO ANSI
RESET = "\33[0m"
VERDE = "\33[32;1m"
ROJO = "\33[31;1m"

def menuVenta():
    opcion = 1
    while opcion != 0:
        print('''
        --Menu Venta--
        '1 - Modificacion Venta
        '2 - Mostrar Venta
        '3 - Leer venta
        '0 - Volver al menu principal''')

        opcion = int(input("Ingresa un numero: "))
        if opcion == 1:
            modificacionVenta()
        if opcion == 2:
            mostrarVentas()
        if opcion == 3:
            leerVenta()
        

def altaVenta(idCliente, carrito):  
    if carrito:  
        Ticket.altaTicket(carrito)
        total = Ticket.imprimir_ticket(Usuario.obtenerCliente(idCliente), carrito)
        
        nuevo_id = listaVentas[-1]["id_venta"] + 1 if listaVentas else 1
        listaVentas.append({"id_venta": nuevo_id, "id_ticket": carrito[0][0], "id_cliente": idCliente, "monto_total": total, "metodo_pago": "pendiente", "fecha": "2025-06-04", "estado": True})
        print(f"{VERDE}Compra realizada correctamente.{RESET}")

def mostrarVentas():
    if not listaVentas:
        print("No hay ventas registradas.")
    else:
        print("-"*90)  
        print(f'{"ID_Venta":<15}{"Ticket":<15}{"Cliente":<16}{"Metodo de Pago":<18}{"Total $":<10}')
        print("-"*90)  
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


def modificacionVenta():
    print("| Modificacion de la Venta |")
    print("-"*90)  
    print(f'{"ID_Venta":<15}{"Ticket":<15}{"Cliente":<16}{"Metodo de Pago":<18}{"Total $":<10}')
    print("-"*90)  
    for venta in listaVentas:
        if venta['estado']:              
            print(f"{venta['id_venta']:<15} {venta['id_ticket']:<15} {venta['id_cliente']:<13} {venta['metodo_pago']:<18} {venta['monto_total']:.2f}")

    
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


def leerVenta():
    idVenta = int(input("Ingrese el ID de la venta: "))

    encontrado = False
    for venta in listaVentas:
        if venta['id_venta'] == idVenta: 
            encontrado = True

            cliente = Usuario.obtenerCliente(venta['id_cliente'])
            tickets = Ticket.obtenerTickets(venta['id_ticket'])

            idCliente, nombreCliente, mail, numero, estadoCliente = cliente

            print("-"*65)  
            
            print(f'{"ID_Venta:":<5} {venta['id_venta']} {"ID_Ticket: ":>48} {venta['id_ticket']}')
            
            print("-"*65)

            print(f'{"Producto":<40}{"Cantidad":<15}{"Subtotal $":<10}')

            for prod in tickets:
                idTicket, idProducto, cantidad, subtotal, estadoTicket = prod
                producto = Producto.obtenerProducto(idProducto)
                print(f"{producto[1]:<43} {cantidad:<15} {subtotal:<10}")

            print("-"*65)  

            print(f'{"Cliente: "} {idCliente} - {nombreCliente} {"Total: ":>18} {venta['monto_total']} - {venta['metodo_pago']}')

            print("-"*65)  
            return
    
    if not encontrado:
        print("No se encontro la venta indicada.")


def obtenerVentasPorCliente(id_cliente):
    ventasEncontradas = [venta for venta in listaVentas if venta['id_cliente'] == id_cliente]
    return ventasEncontradas


            


            
     
