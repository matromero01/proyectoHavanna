import Producto
import Usuario
import reporte

#print("Inicio de Havanna")

def inicio():
    print("Bienvenido a Havanna")
    opcion = 1
    while opcion != 0:
        print('''\nMenu de Inicio
        1 - Login
        0 - Salir del sistema''')

        opcion = int(input("Ingresa una opción: "))
        if opcion == 1:
            Usuario.menuAutenticacion()
        elif opcion == 0:
            print("Saliendo del sistema... ")
if __name__ == "__main__":
    inicio()
