# utilidades.py - Funciones auxiliares reutilizables

def pedirEntero(mensaje):
    """Pide un entero al usuario y lo repite si no es valido"""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese solo numeros enteros")

def pedirDecimal(mensaje):
    """Pide un numero decimal al usuario y lo repite si no es valido"""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingrese solo numeros.")
