# ============================================================
# utilidades.py - Funciones auxiliares reutilizables
# ============================================================

def pedirEntero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese solo numeros enteros")

def pedirDecimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingrese solo numeros.")