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

historialCompras = [
    [1, 1, "Facundo Mello", [["Cortado", 2, 244.0], ["Medialunas x3", 1, 120.0]], 364.0],
    [2, 3, "Juan Perez",    [["Tostado de jamón", 1, 180.0]], 180.0],
    [3, 2, "Lionel Messi",  [["Capuccino", 2, 340.0], ["Cheesecake", 1, 250.0]], 590.0],
]

def registrarCompra(cliente, carrito):
    ''' Guarda la compra finalizada en el historial de compras. '''
    if not carrito:
        print("El carrito está vacío. No se puede registrar la compra.")
        return
    idCompra = len(historialCompras) + 1
    idCliente = cliente[0]
    nombreCliente = cliente[1]
    productosComprados= []
    total = 0
    for item in carrito:
        if len(item) == 4:
            idProducto, nombre, precio, cantidad = item
            subtotal = precio * cantidad
        else:
            idProducto, nombre, precio, cantidad = item[0], item[1], item[2], item[3]
            subtotal = precio * cantidad
        productosComprados.append([nombre, cantidad, subtotal])
        total += subtotal
    historialCompras.append([idCompra, idCliente, nombreCliente, productosComprados, total])
    print(f"Compra registrada exitosamente para el cliente {nombreCliente}. Total: ${total:.2f}")

def estadisticasVentas():
    ventas_activas = list(filter(es_venta_activa, Venta.listaVentas))

    if not ventas_activas:
        print("No hay ventas registradas.")
        return

    montos = list(map(lambda v: v["monto_total"], ventas_activas))
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
    print(f"\n Metodos utilizado: {metodos_usados}")
    for metodo in metodos_usados:
        cantidad  = len([v for v in ventas_activas if v["metodo_pago"] == metodo])
        porcentaje = calcular_promedio(cantidad * 100, len(ventas_activas))
        print(f"    {metodo:<15} {cantidad} ventas  ({porcentaje:.1f}%)")

    print("==================================")

def productoMasVendido():

    conteo = {}
    
    for ticket in Ticket.matrizTicket:
        id_producto = ticket[1]
        cantidad = ticket[2]
        if id_producto in conteo:
            conteo[id_producto] += cantidad
        else:
            conteo[id_producto] = cantidad
    
    id_mas_vendido = max(conteo, key=conteo.get)
    producto = Producto.obtenerProducto(id_mas_vendido)
    
    print(f"Producto más vendido: {producto[1]} con {conteo[id_mas_vendido]} unidades vendidas.")

def totalRecaudado():
    ventas_activas = list(filter(es_venta_activa, Venta.listaVentas))
    montos = list(map(lambda v: v["monto_total"], ventas_activas))

    if not montos:
        print("No hay ventas registradas.")
        return

    total = reduce(lambda x, y: x + y, montos)
    promedio = calcular_promedio(total, len(montos))

    print(f"Total recaudado:  ${total:.2f}")
    print(f"Promedio por venta: ${promedio:.2f}")

def menuReportes():
    opcion = 1
    while opcion != 0:
        print('''
        --Menu Reportes--
        '1 - Ver Historial de Compras
        '2 - Producto mas vendido
        '3 - Total recaudado
        '4 - Estadisticas de Ventas
        '0 - Volver al menu principal''')

        opcion = utilidades.pedirEntero("Ingresa un numero: ")
        if opcion == 1:
            if not historialCompras:
                print("No hay compras registradas.")
            else:
                print("Ultimas 3 compras: ")
                for compra in historialCompras[-3:]:
                    idCompra, idCliente, nombreCliente, productosComprados, total = compra
                    print(f"Compra ID: {idCompra}, Cliente: {nombreCliente} (ID: {idCliente}), Total: ${total:.2f}")
                    print("Productos Comprados:")
                    for producto in productosComprados:
                        nombre, cantidad, subtotal = producto
                        print(f" - {nombre}: Cantidad: {cantidad}, Subtotal: ${subtotal:.2f}")
                    print("-" * 40)
        elif opcion == 2:
            productoMasVendido()
        elif opcion == 3:
            totalRecaudado()
        elif opcion == 4:
            estadisticasVentas()
        elif opcion == 0:
            print("Volviendo al menú principal...")
        else:
            print("Opción Inválida")
