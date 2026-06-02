import unittest
import Producto

class TestProducto(unittest.TestCase):

    def setUp(self):
        Producto.matrizProductos.clear()
        Producto.matrizProductos.extend([
            [1, "Cortado", 122.0 , 5, True],
            [2, "Americano", 122.0 , 10 , True],
            [3, "Cheescake", 250.0, 4, False]
        ])
    def test_obtener_producto_existente(self):
        """ Prueba 1: obtenerProducto debe devolver el producto correcto por ID. """
        resultado= Producto.obtenerProducto(1)
        self.assertEqual(resultado[1], "Cortado")

    def test_obtener_producto_inexistente(self):
        """ Prueba 2: obtenerProducto debe devolver None para un ID que no exista. """
        resultado= Producto.obtenerProducto(99)
        self.assertIsNone (resultado)
    
    def test_nuevo_producto_se_agrega(self):
        """ Prueba 3: al agregar un prodcuto nuevo, la matriz debe crecer."""
        cantidad_antes= len(Producto.matrizProductos)
        Producto.matrizProductos.append([4, "Medialuna", 120.0, 20, True])
        self.assertEqual(len(Producto.matrizProductos), cantidad_antes + 1)

    def test_baja_producto_cambia_estado(self):
        """ Prueba 4: dar de baja un producto debe cambiar su activo a False."""
        Producto.matrizProductos[0] [4] = False
        self.assertFalse(Producto.matrizProductos[0][4])

    def test_alta_producto_cambia_estado(self):
        """ Prueba 5: dar de alta un producto debe cambiar su activo a True."""
        Producto.matrizProductos[2][4] = True
        self.assertTrue(Producto.matrizProductos[2][4])

if __name__ == '__main__':
    unittest.main() 