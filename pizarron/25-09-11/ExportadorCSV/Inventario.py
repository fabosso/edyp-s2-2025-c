from Exportador import ExportadorObjetos


class ItemInventario:
    def __init__(self, sku, descripcion, cantidad, ubicacion):
        self.sku = sku
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.ubicacion = ubicacion
        self._costo = 0  # Privado


class Inventario:
    def __init__(self, almacen):
        self.almacen = almacen
        self._items = []

    def agregar_item(self, item):
        """
        Agrega un item al inventario.
        Args:
            item: Instancia de ItemInventario a agregar al inventario.
        """
        self._items.append(item)

    def get_items(self):
        """
        Devuelve la lista de items en el inventario.
        Returns:
            list: Lista de instancias de ItemInventario.
        """
        return self._items


class ExportadorInventario(ExportadorObjetos):
    """Exportador específico para inventarios"""

    def _obtener_objetos(self, inventario):
        """
        Obtiene la lista de items de un inventario.
        Args:
            inventario: Instancia de Inventario.
        Returns:
            list: Lista de items del inventario.
        """
        return inventario.get_items()

    def exportar(self, inventario):
        """
        Exporta el inventario a un archivo CSV y muestra un resumen al final.
        Args:
            inventario: Instancia de Inventario a exportar.
        """
        super().exportar(inventario)
        print(
            f"Total de items en inventario: {len(self._obtener_objetos(inventario))}")

def main():
    """
    Ejemplo de uso: crea un inventario, agrega items y exporta los datos a un archivo CSV.
    """
    print("\n=== EJEMPLO 3: Inventario ===")
    inventario = Inventario("Almacén Principal")
    inventario.agregar_item(ItemInventario(
        "SKU001", "Monitor 24 pulgadas", 25, "A1-B2"))
    inventario.agregar_item(ItemInventario(
        "SKU002", "Cable HDMI 2m", 100, "C3-D4"))
    inventario.agregar_item(ItemInventario("SKU003", "Webcam HD", 40, "E5-F6"))

    exportador_inventario = ExportadorInventario("inventario.csv")
    exportador_inventario.exportar(inventario)

if __name__ == "__main__":
    main()
