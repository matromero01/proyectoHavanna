
matrizCliente = [
    [1,  "Facundo Mello",      "facundomello34@mail.com",   "1124084431", True],
    [2,  "Cristina Kirchner",  "cristinareina@gmail.com",   "1149034410", True],
    [3,  "Juan Perez",         "juanperez@gmail.com",       "1156781234", True],
    [4,  "Maria Lopez",        "marialopez@hotmail.com",    "1167894321", True],
    [5,  "Carlos Gomez",       "carlosgomez@yahoo.com",     "1178905678", False],
    [6,  "Laura Fernandez",    "lauraf@gmail.com",          "1189016789", True],
    [7,  "Diego Martinez",     "diegom@outlook.com",        "1190127890", True],
    [8,  "Ana Rodriguez",      "anar@gmail.com",            "1101238901", False],
]

def menuInicio():
    opcion = 1
    while opcion !=0:
        print('''\nMenu de Inicio
        1 - Login Administrador
        2 - Login Cliente
        3 - Salir del sistema''')

        opcion =int(input("Ingresa una opción: "))
        if opcion == 1:
            loginAdmin()
        if opcion == 2:
            loginCliente()
        if opcion == 3:
            print("Saliendo del sistema... ")

def loginAdmin():
    print("\n--- Login Administrador ---")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")

    if usuario == "admin" and contraseña == "admin123":
        print("Login completado exitosamente. Bienvenido, Administrador!")
        clienteMenu()
    else: 
        print("Usuario o contraseña son incorrectos. Intente nuevamente.")
def loginCliente():
    print("\n--- Login Cliente ---")
    email = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de contacto: ")
    for cliente in matrizCliente:
        if cliente[2] == email and cliente[3] == telefono and cliente[4] == True:
            print(f"Login completado exitosamente. Bienvenido, {cliente[1]}!")
            clienteMenu()
            

    print("Correo electrónico o número de contacto incorrectos, o el cliente está dado de baja. Intente nuevamente.")

    return None 
    '''Use el return None para indicar que la funcion no devuelva ningun valor util en caso de que el login falle, 
    lo que permite al sistema manejar adecuadamente los casos de login fallidos sin causar errores o comportamientos inesperados.'''

def clienteMenu():
    opcion = 1
    while opcion != 0:
        print('''Menu Principal
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
    while "@" not in clienteEmail or "." not in clienteEmail: #Esto es para validar que el correo que ingrese el cliente contenga su formalo valido "@" y un punto, si no, le va a pedir que ingrese un correo valido."
        print("Correo electrónico no válido. Por favor, ingrese un correo electrónico válido.")
        clienteEmail = input("Ingrese su Email: ")
    clienteTelefono= input("Ingrese su número de contacto: ")
    while not clienteTelefono.isdigit() or len(clienteTelefono) < 7:
        print("Número de teléfono invalido, por favor, vuelve a ingresarlo nuevamente.")
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


        for i in range(len(matrizCliente)):
            cliente = matrizCliente[i][1]
            if matrizCliente[i] [0] == idCliente:
                encontrado = True
                if matrizCliente[i][4] == True:
                    matrizCliente[i] [4] = False
                    print(f"Cliente '{cliente}' (ID: {idCliente}) dado de baja exitosamente.")
                else: 
                    print(f"Cliente '{cliente}' (ID: {idCliente}) ya fue dado de baja anteriormente.")
                    condicionAlta = input(f"¿Queres dar de alta al cliente ahora? (si/no): \n Cliente '{cliente}' (ID: {idCliente})")
                    while condicionAlta != "si" and condicionAlta != "no":
                        print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
                        condicionAlta = input("¿Quiere darlo de alta ahora? (si/no): ").strip().lower()
                    
                    if condicionAlta == "si":
                        altaCliente() 
                        break #Agregamos el break para salir del ciclo una vez que se da de alta el cliente nuevamente, evitando asi que el sistema siga preguntando por el mismo cliente dado de baja anteriormente
        if not encontrado: 
            print(f"No se encontró ningún cliente con ID: {idCliente}. \n")

def modificacionCliente():
    if not matrizCliente:
        print("No hay cliente para modificar.")
    else:
        mostrarListaCliente() 
        idCliente = int(input("Ingrese el ID del cliente para modificar: "))

        for i in range(len(matrizCliente)): 
            if matrizCliente[i][0] == idCliente:
                id, nombre, mail, numero, activo =matrizCliente[i]

                datoModificado = input("Ingrese un nombre: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizCliente[i][1] = datoModificado
                
                datoModificado = input("Ingrese un mail: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizCliente[i][2] = datoModificado
                
                datoModificado = input("Ingrese un numero: (Deje vacio si no quiere modificarlo) ")
                if datoModificado.strip() != "":
                    matrizCliente[i][3] = datoModificado

                print(f"Cliente '{nombre}' (ID: {idCliente}) fue modificado correctamente")
                return
        print("Opción inválida: El ID ingresado no existe.")      

def mostrarListaCliente():
    print(f"{'ID':<5} {'Nombre':<20} {'Email':<30} {'Telefono':<15} {'Activo':<8}")
    print("-" * 80)
    for fila in matrizCliente:
        print(f"{fila[0]:<5} {fila[1]:<20} {fila[2]:<30} {fila[3]:<15} {str(fila[4]):<8}")

def existeCliente(idCliente):
    encontrado = False 
    for i in range(len(matrizCliente)):
        if matrizCliente[i][0] == idCliente:
            encontrado = True
            break

    if not encontrado:
        print("El cliente no existe en la matriz.")

    return encontrado

def obtenerCliente(idCliente):
    for i in range(len(matrizCliente)):
        if matrizCliente[i] [0] == idCliente:
            return matrizCliente[i]
