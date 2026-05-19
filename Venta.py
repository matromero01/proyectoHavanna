import Usuario, Ticket, Producto, utilidades
import os

directorio_actual = os.path.dirname(os.path.abspath(__file__))
archivoVenta = os.path.join(directorio_actual, "Archivos", "archivoVenta.txt")

# CODIGO ANSI
RESET = "\33[0m"
VERDE = "\33[32;1m"
ROJO = "\33[31;1m"

MetodosPago = ("efectivo", "tarjeta", "transferencia")

def menuVenta():
    opcion = 1
    while opcion != 0:
        print('''
        --Menu Venta--
        '1 - Modificacion Venta
        '2 - Mostrar Venta
        '3 - Leer venta
        '4 - Baja Venta
        '0 - Volver al menu principal''')

        opcion = utilidades.pedirEntero("Ingresa un numero: ")
        if opcion == 1:
            modificacionVenta()
        elif opcion == 2:
            mostrarVentas()
        elif opcion == 3:
            leerVenta()
        elif opcion == 4:
            bajaVenta()

def cargaVentas():

    if not os.path.exists(archivoVenta):
        return
    
    with open(archivoVenta, "r", encoding="utf-8") as v:
        for linea in v:

            linea = linea.strip()

            if not linea:
                continue

            partes = linea.split(";")

            if len(partes) >= 7:
                id_venta = int(partes[0])
                id_ticket = int(partes[1])
                id_cliente = int(partes[2])
                monto_total = float(partes[3])
                metodo_pago = partes[4].strip('"')
                fecha = partes[5].strip('"')

                estado = partes[6].strip == "True"

                matrizVentas.append([id_venta, id_ticket, id_cliente, monto_total, metodo_pago, fecha, estado])


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

        nuevo_id = listaVentas[-1]["id_venta"] + 1 if listaVentas else 1
        listaVentas.append({"id_venta": nuevo_id, "id_ticket": carrito[0][0], "id_cliente": idCliente, "monto_total": total, "metodo_pago": metodoPago, "fecha": "2025-06-04", "estado": True})
        print(f"{VERDE}Compra realizada correctamente.{RESET}")

        cliente = Usuario.obtenerCliente(idCliente)
        reporte.registrarCompra(cliente, carrito)

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
            return
    
    if not encontrado:
        print("No se encontro la venta indicada.")


def obtenerVentasPorCliente(id_cliente):
    ventasEncontradas = [venta for venta in listaVentas if venta['id_cliente'] == id_cliente]
    return ventasEncontradas


            


            
     
