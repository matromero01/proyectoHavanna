import Producto

# Id_ticket, id_producto, cantidad, subtotal, activo
matrizTicket = [[123, 1, 2, 244.0, True],
                [123, 2, 4, 500.0, True]] 

def ticketMenu():
    opcion = 1
    while opcion != 0:
        print('''
        --Menu Ticket--
        '1 - Alta Ticket
        '2 - Baja Ticket
        '3 - Modificacion Ticket
        '4 - Mostrar Ticket
        '5 - Leer Ticket
        '0 - Volver al menu principal''')

        opcion = int(input("Ingresa un numero: "))
        if opcion == 1:
            altaTicket()
       # if opcion == 2:
       # if opcion == 3:
       #     modificacionProducto()
       # if opcion == 4:
       #     mostrarListaProducto()
       # if opcion == 5:
       #     mostrarProducto()
        if opcion == 0:
            print("Adios!")
                
    
def altaTicket(matrizTicket, matrizProductos):
    ticket_auxiliar = []
    flag = True
    numeroTicket = int(matrizTicket[-1][0]) + 1
    while flag:
        print()
        Producto.mostrarListaProducto()
        print()
        idProducto = int(input("Ingrese el ID del producto que desea comprar: "))
        encontrado = False
        for i in range(len(matrizProductos)): 
            if matrizProductos[i][0] == idProducto:
                encontrado = True
                nombre = matrizProductos[i][1]
                
                cantidad = int(input(f"Ingrese la cantidad de {nombre} que desea llevar: "))

                ticket_auxiliar.append([numeroTicket, idProducto, cantidad, (matrizProductos[i][2] * cantidad), True])
                print("Se agregó correctamente.")
                break

        if not encontrado:
            print("Opción inválida: El ID ingresado no existe.")
        
        continuar = ""
        while continuar.strip().lower() != "s" and continuar.strip().lower() != "n":
            continuar = input("Desea agregar otro producto? (s/n): ")
            if continuar.strip().lower() == "s":
                flag = True
            elif continuar.strip().lower() == "n":   
                flag = False
            else: 
                print("Opción inválida.")
    
    continuar = ""
    while continuar.strip().lower() != "s" and continuar.strip().lower() != "n":
        continuar = input("Desea confirmar el pedido? (s/n): ")
        if continuar.strip().lower() == "s":
            return ticket_auxiliar
        elif continuar.strip().lower() == "n":   
            return 
        else: 
            print("Opción inválida.")

def imprimir_ticket(cliente, ticket_auxiliar):
    total = 0
    print(f"IdTicket --> {ticket_auxiliar[0][0]}")
    print("|    Producto    |    Cantidad    |    Subtotal    |")
    
    for linea in ticket_auxiliar:
      idTicket, idProducto, cantidad, subtotal, estadoTicket = linea
      print(f"|       {idProducto}       |       {cantidad}       |       {subtotal}       |")
      total+= subtotal
    
    print(f"Total --> {total}")
    
    idCliente, nombre, mail, telefono, estadoCliente = cliente
    print(f"Cliente --> {nombre}")

    return total

def agregarTicket(ticket_auxiliar):
    matrizTicket.append(ticket_auxiliar)
    
    