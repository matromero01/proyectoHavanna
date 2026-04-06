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
       #     bajaProducto()
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
    numeroTicket = matrizTicket[-1][0] + 1
    while flag:
        Producto.mostrarListaProducto()
        idProducto = int(input("Ingrese el ID del producto que desea comprar: "))
        encontrado = False
        for i in range(len(matrizProductos)): 
            if matrizProductos[i][0] == idProducto:
                encontrado = True
                nombre = matrizProductos[i][1]
                
                cantidad = int(input(f"Ingrese la cantidad de {nombre} que desea llevar: "))

                ticket_auxiliar.append([numeroTicket, idProducto, cantidad, (matrizProductos[i][0] * cantidad), True])
                print("Se agregó correctamente.")
                break

        if not encontrado:
            print("Opción inválida: El ID ingresado no existe.")

        continuar = input("Desea agregar otro producto? (s/n): ")
        if continuar.strip().lower() != "s":
            flag = False
        elif continuar.strip().lower() == "n":   
            flag = True
        else: 
            print("Opción inválida.")

    continuar = input("Desea confirmar el pedido? (s/n): ")
    if continuar.strip().lower() != "s":
        matrizTicket.append(ticket_auxiliar)
        print("Pedido confirmado!")
    elif continuar.strip().lower() == "n":   
        return 
    else: 
        print("Opción inválida.")
        
                

            


