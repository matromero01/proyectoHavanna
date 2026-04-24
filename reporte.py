import Cliente
import Venta
import Producto
import Ticket
from functools import reduce

historialCompras = []

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

def totalRecaudado():
    # filter - solo ventas activas
    ventas_activas = list(filter(lambda v: v["estado"] == True, Venta.listaVentas))
    
    # map - extrae solo los montos
    montos = list(map(lambda v: v["monto_total"], ventas_activas))
    
    if not montos:
        print("No hay ventas registradas.")
        return
    
    # reduce - suma todos los montos
    total = reduce(lambda x, y: x + y, montos)
    
    print(f"Total recaudado: ${total:.2f}")

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

def menuReportes():
    opcion = 1
    while opcion != 0:
        print('''
        --Menu Reportes--
        '1 - Ver Historial de Compras
        '2 - Producto mas vendido
        '3 - Total recaudado
        '0 - Volver al menu principal''')

        opcion = int(input("Ingresa un numero: "))
        if opcion == 1:
            if not historialCompras:
                print("No hay compras registradas.")
            else:
                for compra in historialCompras:
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
        elif opcion == 0:
            print("Volviendo al menú principal...")
        else:
            print("Opción Inválida")
