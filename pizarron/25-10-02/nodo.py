from typing import Optional


class Nodo:
    def __init__(self, dato):
        self.dato: int = dato
        self.siguiente: Optional[Nodo] = None
