from Validador import Validador as V


class Producto:
    def __init__(self, sku: str, precio: str, stock: int):
        self.sku = V.validar_cadena_no_vacia(sku, "SKU")
        self.sku = V.validar_alfanumerico(self.sku, "SKU")
        
        self.precio = V.validar_rango_numerico(precio, 0.01, None, "Precio")
        
        self.stock = V.validar_entero_en_rango(stock, 0, None, "Stock")