import Producto, Usuario

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
                
    
def altaTicket(carrito):
    matrizTicket.extend(carrito)
    
    

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
      total+= subtotal
    
    print("-"*55) 
    print(f"Total --> {total}")
    print("-"*55) 
    
    idCliente, nombre, mail, telefono, estadoCliente = cliente
    print(f"Cliente --> {nombre}")
    print("-"*55) 
    
    return total


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


def obtenerTickets(idTicket):
    ticketsConseguidos = []
    for ticket in matrizTicket:
        if ticket[0] == int(idTicket):
            ticketsConseguidos.append(ticket)
    
    return ticketsConseguidos

