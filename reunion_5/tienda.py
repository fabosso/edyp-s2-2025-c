# Clase base Producto
class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

# Clase CD que hereda de Producto
class CD(Producto):
    def __init__(self, id, nombre, precio, artista, genero):
        super().__init__(id, nombre, precio)
        self.artista = artista
        self.genero = genero

    def __str__(self):
        return f"CD: {self.nombre} de {self.artista} - Género: {self.genero} (${self.precio})"

# Clase Tienda que contiene productos
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_por_id(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        return None

    def eliminar_por_id(self, id):
        producto_buscado = self.buscar_por_id(id)
        if producto_buscado != None:
            self.productos.remove(producto_buscado)


tienda = Tienda()

cd1 = CD(1, "Abbey Road", 2500, "The Beatles", "Rock")
cd2 = CD(2, "Thriller", 2700, "Michael Jackson", "Pop")

tienda.agregar_producto(cd1)
tienda.agregar_producto(cd2)

resultado = tienda.buscar_por_id(2)
if resultado:
    print("Producto encontrado:", resultado)
else:
    print("Producto no encontrado")
