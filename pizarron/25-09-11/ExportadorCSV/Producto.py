from Exportador import ExportadorObjetos


class Producto:
    def __init__(self, nombre, precio, codigo, stock):
        """
        Inicializa un nuevo producto con los datos proporcionados.
        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            codigo (str): Código identificador del producto.
            stock (int): Cantidad en stock del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        self.stock = stock
        self._proveedor = "Confidencial"  # No se exportará

    def actualizar_stock(self, cantidad):
        """
        Actualiza la cantidad en stock del producto.
        Args:
            cantidad (int): Cantidad a sumar (o restar) al stock actual.
        """
        self.stock += cantidad


class CatalogoProductos:
    def __init__(self):
        """
        Inicializa un catálogo vacío de productos.
        """
        self._productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al catálogo.
        Args:
            producto (Producto): Instancia de Producto a agregar.
        """
        self._productos.append(producto)

    def get_productos(self):
        """
        Devuelve la lista de productos en el catálogo.
        Returns:
            list: Lista de instancias de Producto.
        """
        return self._productos


class ExportadorCatalogo(ExportadorObjetos):
    """Exportador específico para catálogos de productos"""

    def _obtener_objetos(self, catalogo):
        """
        Obtiene la lista de productos de un catálogo.
        Args:
            catalogo (CatalogoProductos): Catálogo de productos.
        Returns:
            list: Lista de productos del catálogo.
        """
        return catalogo.get_productos()


def main():
    """
    Ejemplo de uso: crea un catálogo de productos, agrega productos y exporta los datos a un archivo CSV.
    """
    print("\n=== EJEMPLO 1: Catálogo de Productos ===")
    catalogo = CatalogoProductos()
    catalogo.agregar_producto(
        Producto("Laptop Dell XPS", 1200.00, "LAP001", 15))
    catalogo.agregar_producto(Producto("Mouse Logitech", 25.99, "MOU001", 50))
    catalogo.agregar_producto(
        Producto("Teclado Mecánico", 89.99, "TEC001", 30))

    exportador_productos = ExportadorCatalogo("productos.csv")
    exportador_productos.exportar(catalogo)


if __name__ == "__main__":
    main()
