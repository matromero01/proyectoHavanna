import Usuario
import Venta
import Producto
import Ticket
import utilidades

from functools import reduce


#Lambdas directas
calcular_subtotal = lambda precio, cantidad: precio * cantidad
aplicar_descuento = lambda precio: precio * 0.9
calcular_promedio = lambda total, cant: total / cant if cant > 0 else 0
es_venta_activa = lambda venta: venta["estado"] == True

#historialCompras = [
 #   [1, 1, "Facundo Mello", [["Cortado", 2, 244.0], ["Medialunas x3", 1, 120.0]], 364.0],
  #  [2, 3, "Juan Perez",    [["Tostado de jamón", 1, 180.0]], 180.0],
   # [3, 2, "Lionel Messi",  [["Capuccino", 2, 340.0], ["Cheesecake", 1, 250.0]], 590.0],
#]

def verHistorialCompras():
    """Muestra las ultimas 3 compras"""
    ventas_activas = list(filter(es_venta_activa, Venta.obtener_ventas()))

    if not ventas_activas:
        print("No hay compras registradas.")
        return
    
    print("Ultimas 3 compras: ")
    for venta in ventas_activas[-3:]:
        idCompra = venta["id_venta"]
        idCliente = venta["id_cliente"]
        total = venta["monto_total"]

        cliente = Usuario.obtenerCliente(idCliente)
        nombreCliente = cliente[2] if cliente else "Cliente Desconocido"

        print(f"Compra ID: {idCompra}, Cliente: {nombreCliente}(ID:{idCliente}), Total:${total:.2f}")
        print("Productos Comprados:")

        tickets = Ticket.obtenerTickets(venta["id_ticket"])
        for prod in tickets:
            idTicket, idProducto, cantidad, subtotal, estadoTicket = prod
            producto = Producto.obtenerProducto(idProducto)
            nombreProducto = producto[1] if producto else "Producto Eliminado"
            
            print(f" - {nombreProducto}: Cantidad: {cantidad}, Subtotal: {subtotal:.2f}")
        print("-" * 40)


def estadisticasVentas():
    """Muestra estadisticas de ventas: total - promedio - min - max - y % de metodos de pago"""
    ventas_activas = list(filter(es_venta_activa, Venta.obtener_ventas()))

    if not ventas_activas:
        print("No hay ventas registradas.")
        return

    montos = list(map(lambda v: v["monto_total"], ventas_activas))
    montos.sort()
    total    = reduce(lambda x, y: x + y, montos)
    promedio = calcular_promedio(total, len(montos))   # lambda directa
    minimo   = min(montos)
    maximo   = max(montos)

    print("\n===== Estadísticas de ventas =====")
    print(f"  Total de ventas:    {len(ventas_activas)}")
    print(f"  Total recaudado:    ${total:.2f}")
    print(f"  Promedio por venta: ${promedio:.2f}")
    print(f"  Venta mínima:       ${minimo:.2f}")
    print(f"  Venta máxima:       ${maximo:.2f}")

    # ── Porcentajes por método de pago ──────────────────
    print("\n  Ventas por método de pago:")
    metodos_usados = {v["metodo_pago"] for v in ventas_activas}
    metodos_sin_usar = set(Venta.MetodosPago) - metodos_usados
    if metodos_sin_usar:
        print(f"\n  Metodos sin registrar: {metodos_sin_usar}")
    print(f"\n Metodos utilizado: {metodos_usados}")
    for metodo in metodos_usados:
        cantidad  = len([v for v in ventas_activas if v["metodo_pago"] == metodo])
        porcentaje = calcular_promedio(cantidad * 100, len(ventas_activas))
        print(f"    {metodo:<15} {cantidad} ventas  ({porcentaje:.1f}%)")

    print("==================================")

def productoMasVendido():
    """Muestra el producto con mas u. vendidas"""
    conteo = {}
    tickets = Ticket.obtener_tickets()
    if not tickets:
        print("No hay ventas registradas para saber cual es el producto mas vendido")
        return
    
    for ticket in tickets:
        id_producto = ticket[1]
        cantidad = ticket[2]
        estado_ticket = ticket[4]

        if estado_ticket == True:
            if id_producto in conteo:
                conteo[id_producto] += cantidad
            else:
                conteo[id_producto] = cantidad
    
    if not conteo:
        print("No hay ventas activas para calcular")
        return
    
    id_mas_vendido = max(conteo, key=conteo.get)
    producto = Producto.obtenerProducto(id_mas_vendido)

    nombre_producto = producto[1] if producto else "Producto Desconocido"

    print(f"Producto más vendido: {nombre_producto} con {conteo[id_mas_vendido]} unidades vendidas.")
       
def totalRecaudado():
    """Muestra el total recaudado y promedio por venta"""
    ventas_activas = list(filter(es_venta_activa, Venta.obtener_ventas()))
    montos = list(map(lambda v: v["monto_total"], ventas_activas))

    if not montos:
        print("No hay ventas registradas.")
        return

    total = reduce(lambda x, y: x + y, montos)
    promedio = calcular_promedio(total, len(montos))

    print(f"Total recaudado:  ${total:.2f}")
    print(f"Promedio por venta: ${promedio:.2f}")

def clientesRecientes(n=5):
    """Muestra los ultimos N clientes registrados"""
    usuarios = Usuario.obtener_usuarios()
    recientes = usuarios[-n:] 
    print(f"\n--- Últimos {n} clientes registrados ---")
    for user in recientes:
        estado = "Activo" if user["activo"] else "Inactivo"
        nombre_corto = user['nombre'][:15]
        print(f"ID: {user['id']} | {nombre_corto:<15} | {estado}")

def productosMasCaros(n=3):
    """Top N productos mas caros"""
    activos = [p for p in Producto.matrizProductos if p[4]]
    ordenados = sorted(activos, key=lambda p: p[2], reverse=True)
    top = ordenados[:n] 

    print(f"\n--- Top {n} productos más caros ---")
    for i, p in enumerate(top, 1):
        print(f"{i}. {p[1]:<25} ${p[2]:.2f}")

def contarClientes(usuarios, indice=0, activos=0, inactivos=0):
    """Cuenta clientes activos e inactivos de forma recursiva"""
    if indice >= len(usuarios):
        return activos, inactivos
    if usuarios[indice]["activo"]:
        return contarClientes(usuarios, indice + 1, activos + 1, inactivos)
    return contarClientes(usuarios, indice + 1, activos, inactivos + 1)

def calcularTotalCarrito(carrito, indice = 0):
    """Calcula el carrito de forma recursiva"""
    if indice >= len(carrito):
        return 0 
    return carrito[indice][3] + calcularTotalCarrito(carrito, indice + 1)

def reporteClientes():
    """Muestra un resumen del estado de los clientes"""
    usuarios = Usuario.obtener_usuarios()
    activos, inactivos = contarClientes(usuarios)
    print(f"\n--- Estado de clientes ---")
    print(f"Activos:   {activos}")
    print(f"Inactivos: {inactivos}")
    print(f"Total:     {activos + inactivos}")

def menuReportes():
    """Menu de reportes para admin"""
    opcion = 1
    while opcion != 0:
        print('''
    ----------------------------
             MENU REPORTES
        '1 - Ver Historial de Compras
        '2 - Producto mas vendido
        '3 - Total recaudado
        '4 - Estadisticas de Ventas
        '5 - Productos mas caros 
        '6 - Clientes recientes
        '7 - Estadisticas de Clientes
        '0 - Volver al menu principal
    ----------------------------''')

        opcion = utilidades.pedirEntero("Ingresa un numero: ")
        if opcion == 1:
            verHistorialCompras()
        elif opcion == 2:
            productoMasVendido()
        elif opcion == 3:
            totalRecaudado()
        elif opcion == 4:
            estadisticasVentas()
        elif opcion == 5: 
            productosMasCaros()
        elif opcion == 6: 
            clientesRecientes()
        elif opcion == 7:
            reporteClientes()
        elif opcion == 0:
            print("Volviendo al menú principal...")
        else:
            print("Opción Inválida")
