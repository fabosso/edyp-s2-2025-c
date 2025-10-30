class GestionPedidos:
    def __init__(self):
        self.pedidos = []  # Lista simple con diccionarios

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def procesar_pedido_ultimo(self):
        if self.pedidos:
            return self.pedidos.pop()
        return None

    def buscar_pedido(self, id_pedido):
        for p in self.pedidos:
            if p['id'] == id_pedido:
                return p
        return None
