class NaveEspacial:
    def __init__(self):
        self._recorrido = []  # Lista para guardar coordenadas
        self._historial_acciones = []  # Registro de maniobras para deshacer

    def obtener_recorrido(self):
        """
        Devuelve la secuencia de coordenadas visitadas en orden.
        """
        return self._recorrido

    def agregar_coordenada(self, coordenada):
        """
        Añade una nueva coordenada visitada.

        :param coordenada: tupla con (x, y, z)
        """
        pass

    def deshacer_maniobra(self):
        """
        Revierte la última maniobra (agregar_coordenada) y actualiza el recorrido.
        """
        pass


def caso_1():
    nave = NaveEspacial()

    nave.agregar_coordenada((0, 0, 0))
    nave.agregar_coordenada((1, 1, 1))
    nave.agregar_coordenada((2, 2, 2))

    print(nave.obtener_recorrido())  # Salida esperada: [(0,0,0), (1,1,1), (2,2,2)]


def caso_2():
    nave = NaveEspacial()

    nave.agregar_coordenada((0, 0, 0))
    nave.agregar_coordenada((1, 1, 1))
    nave.agregar_coordenada((2, 2, 2))

    nave.deshacer_maniobra()

    print(nave.obtener_recorrido())  # Salida esperada: [(0,0,0), (1,1,1)]


def caso_3():
    nave = NaveEspacial()

    nave.agregar_coordenada((0, 0, 0))
    nave.agregar_coordenada((1, 1, 1))
    nave.agregar_coordenada((2, 2, 2))

    nave.agregar_coordenada((3, 3, 3))
    nave.deshacer_maniobra()
    nave.deshacer_maniobra()
    nave.agregar_coordenada((4, 4, 4))

    print(nave.obtener_recorrido())  # Salida esperada: [(0,0,0), (1,1,1), (4,4,4)]
