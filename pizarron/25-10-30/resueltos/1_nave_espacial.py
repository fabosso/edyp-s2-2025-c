class NaveEspacial:
    def __init__(self):
        """
        Inicializa la nave.
        _recorrido: Lista que guarda la secuencia de coordenadas (Req 1).
        _historial_acciones: Lista usada como Pila (LIFO) para el
                             mecanismo de deshacer (Req 3 y 4).
        """
        self._recorrido = []  # Lista para guardar coordenadas
        self._historial_acciones = []  # Registro de maniobras para deshacer

    def obtener_recorrido(self):
        """
        Devuelve la secuencia de coordenadas visitadas en orden.
        (Cumple Req 2)
        """
        return self._recorrido

    def agregar_coordenada(self, coordenada):
        """
        Añade una nueva coordenada visitada.
        (Cumple Req 1)

        :param coordenada: tupla con (x, y, z)
        """
        # 1. Agregar coordenada al recorrido (al final de la lista)
        self._recorrido.append(coordenada)

        # 2. Registrar la acción en el historial (apilando).
        #    Guardamos la misma coordenada para saber qué deshacer.
        self._historial_acciones.append(coordenada)

        # Nota: Si tuviéramos una función "rehacer", al agregar una
        # nueva coordenada, deberíamos limpiar el historial de "rehacer".
        # Para este ejercicio, solo apilamos en el historial de "deshacer".

    def deshacer_maniobra(self):
        """
        Revierte la última maniobra (agregar_coordenada) y actualiza el recorrido.
        Utiliza el comportamiento de Pila (LIFO) de las listas.
        (Cumple Req 3)
        """
        # Verificamos si hay algo que deshacer
        if self._historial_acciones:
            # 1. Quitamos la última acción del historial (LIFO - pop)
            accion_deshecha = self._historial_acciones.pop()

            # 2. Quitamos la última coordenada del recorrido (LIFO - pop)
            #    En este caso, sabemos que la acción fue agregar la
            #    última coordenada.
            coordenada_eliminada = self._recorrido.pop()

            print(f"[Nave] Deshaciendo. Coordenada eliminada: {coordenada_eliminada}")

            # (Opcional) Si tuviéramos un stack de "rehacer",
            # aquí apilaríamos la 'coordenada_eliminada' en él.
        else:
            print("[Nave] No hay maniobras para deshacer.")


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
