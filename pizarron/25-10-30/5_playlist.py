class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion  # en segundos

class Playlist:
    def __init__(self):
        self._canciones = None  # Inicio de lista enlazada (nodo)
        self._actual = None     # Nodo canción actual

    # Métodos a completar:
    def agregar_cancion(self, cancion, posicion=None):
        """Insertar canción en posición dada o final"""

    def eliminar_cancion_actual(self):
        """Eliminar canción activa actual"""

    def siguiente(self):
        """Avanzar a la siguiente canción"""

    def anterior(self):
        """Retroceder a la canción anterior"""

    def mostrar_actual(self):
        """Retorna tupla con datos (título, artista, duración) de canción actual"""
