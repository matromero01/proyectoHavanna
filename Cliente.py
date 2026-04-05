
matrizCliente = [[1, "Facundo Mello", "facundomello34@mail.com", "1124084431", True],
                  [2, "Cristina Kirchner", "cristinareina@gmail.com", "114903441", True]]

def clienteMenu():
    opcion = 1
    while opcion != 0:
        print('''Menu Cliente
        '1 - Alta Cliente
        '2 - Baja Cliente
        '3 - Modificacion Cliente
        '4 - Mostrar Clientes
        '0 - Volver al menu principal''')

        opcion = int(input("Ingresa un numero: "))
        if opcion == 1:
            altaCliente()
        if opcion == 2:
            bajaCliente()
        if opcion == 3:
            modificacionCliente()
        if opcion == 4:
            mostrarListaCliente()
        if opcion == 0:
            print("Volviendo al menu principal...")
def altaCliente():  #Definimos en el sistema la funcion de alta cliente, en donde vamos a incorporar Nombre,Email,Telefono 
    """ Dar de alta un nuevo cliente"""
    print("\n--- Alta de nuevo cliente ---")
    clienteNombre= input("Ingrese el nombre del nuevo cliente: ")
    clienteEmail= input("Ingrese su Email: ")
    clienteTelefono= input("Ingrese su número de contacto: ")

    #Creamos nuevo cliente con un ID autoincremental, el nombre, email,telefono y el estado activo (True) 
    nuevoId= matrizCliente[-1] [0] + 1 if matrizCliente else 1
    nuevoCliente= [nuevoId, clienteNombre, clienteEmail, clienteTelefono, True]
    
    matrizCliente.append(nuevoCliente)
    print(f"Cliente '{clienteNombre}' (ID: {nuevoId}) dado de alta exitosamente.\n")

def bajaCliente(): #Definimos en el ssitema la funcion de baja cleinte, en donde vamos a incorporar el ID del cliente a eliminar. 
    """ Dar de baja un cliente existente"""
    print("\n--- Baja de cliente ---")
    if not matrizCliente:
        print("No hay clientes para eliminar.")
    else: 
        idCliente = int(input("Ingrese el ID del cliente a dar de baja: "))
        encontrado = False

        cliente = matrizCliente[i][1]

        for i in range(len(matrizCliente)):
            if matrizCliente[i] [0] == idCliente:
                encontrado = True
                if matrizCliente[i][4] == True:
                    matrizCliente[i] [4] = False
                    print(f"Cliente '{cliente}' (ID: {idCliente}) dado de baja exitosamente.")
                else: 
                    print(f"Cliente '{cliente}' (ID: {idCliente}) ya fue dado de baja anteriormente.")
                    condicionAlta = input("¿Queres dar de alta al cliente ahora? (si/no): \n Cliente '{cliente}' (ID: {idCliente})")
                    while condicionAlta != "si" and condicionAlta != "no":
                        print("Opción no válida. Por favor, ingresa 'si' o 'no'.")
                        condicionAlta = input("¿Queres dar de alta al cliente ahora? (si/no): \n Cliente '{cliente}' (ID: {idCliente})")

def modificacionCliente(): 

def mostrarListaCliente(): 