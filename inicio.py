import Producto
import Cliente

#print("Inicio de Havanna")

def inicio():
    print("Bienvenido a Havanna")
    opcion = 1
    while opcion != 0:
        print('''\nMenu de Inicio
        1 - Login
        2 - Salir del sistema''')

        opcion = int(input("Ingresa una opción: "))
        if opcion == 1:
            Cliente.menuAutenticacion()
        elif opcion == 2:
            print("Saliendo del sistema... ")
            opcion = 0
if __name__ == "__main__":
    inicio()


