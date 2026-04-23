import Producto

# Id_ticket, id_producto, cantidad, subtotal, activo
matrizTicket = matrizTicket = [
    [123, 1, 2, 244.0, True], 
    [123, 2, 4, 500.0, True], 
    [124, 9, 1, 250.0, True], 
    [124, 6, 1, 120.0, True], 
    [125, 3, 2, 300.0, True],  
    [125, 8, 2, 220.0, True], 
    [126, 7, 1, 180.0, True],  
    [126, 8, 1, 110.0, True], 
    [127, 7, 1, 180.0, True]   
]

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
        if opcion == 4:
            mostrarTicket()
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
    matrizTicket.extend(ticket_auxiliar)

def bajaTicket(id_ticket):
    for ticket in matrizTicket:
      if ticket[0] == id_ticket:
          ticket[-1] = False

    
def mostrarTicket():
    if not matrizTicket:
        print("No hay ventas registradas.")
    else:
        print("-"*55)  
        print(f'{"Id_Ticket":<15}{"Id_Producto":<15}{"Cantidad":<16}{"Subtotal $":<10}')
        print("-"*55)  
        for ticket in matrizTicket:
            id_ticket, id_producto, cantidad, subtotal, estado = ticket
            if estado: 
                print(f"{id_ticket:<15} {id_producto:<15} {cantidad:<13} {subtotal:.2f}")