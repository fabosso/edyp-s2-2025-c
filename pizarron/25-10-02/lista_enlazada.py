from typing import Optional
from nodo import Nodo


class ListaEnlazada:
    def __init__(self):
        self.cabeza: Optional[Nodo] = None

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def agregar_al_inicio(self, nodo: Nodo) -> None:
        if not isinstance(nodo, Nodo):
            raise TypeError("El parámetro recibido no es un Nodo")

        if self.esta_vacia():
            self.cabeza = nodo
            return

        nodo.siguiente = self.cabeza
        self.cabeza = nodo

    def agregar_al_final(self, nodo: Nodo) -> None:
        if not isinstance(nodo, Nodo):
            raise TypeError("El parámetro recibido no es un Nodo")

        if self.esta_vacia():
            self.cabeza = nodo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo

    def mostrar_lista(self) -> None:
        if self.esta_vacia():
            print("La lista está vacía")
            return

        print("Contenido de la lista enlazada:")
        actual = self.cabeza
        valores = []

        # Recorrer la lista hasta que el último sea None
        while actual:
            valores.append(str(actual.dato))
            actual = actual.siguiente

        # Mostrar los valores
        print(" -> ".join(valores))
