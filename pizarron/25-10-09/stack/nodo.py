# from __future__ import annotations se usa para poder referenciar la clase Nodo
# dentro de sus propios type hints antes de que esté completamente definida.
from __future__ import annotations
from typing import Any, Optional


class Nodo:
    """Representa un nodo individual dentro de una lista doblemente enlazada.

    Cada nodo contiene un dato y dos punteros: uno al nodo siguiente (`sig`)
    y otro al nodo anterior (`ant`).

    Attributes:
        dato (Any): El dato o valor almacenado en el nodo.
        sig (Optional[Nodo]): Referencia al siguiente nodo en la lista,
                              o None si es el último.
        ant (Optional[Nodo]): Referencia al nodo anterior en la lista,
                              o None si es el primero.
    """

    def __init__(self, dato: Any) -> None:
        """Inicializa un nuevo objeto Nodo.

        Args:
            dato (Any): El dato que se almacenará en el nodo.
        """
        self.dato = dato
        self.sig: Optional[Nodo] = None
        self.ant: Optional[Nodo] = None

    def set_sig(self, sig: Optional[Nodo]) -> None:
        """Establece la referencia al nodo siguiente.

        Args:
            sig (Optional[Nodo]): El nodo que será el siguiente a este,
                                  o None para indicar el final de la lista.
        """
        self.sig = sig

    def set_ant(self, ant: Optional[Nodo]) -> None:
        """Establece la referencia al nodo anterior.

        Args:
            ant (Optional[Nodo]): El nodo que será el anterior a este,
                                  o None para indicar el inicio de la lista.
        """
        self.ant = ant

    def get_ant(self) -> Optional[Nodo]:
        """Devuelve el nodo anterior en la lista.

        Returns:
            Optional[Nodo]: El nodo anterior, o `None` si este es el primer nodo.
        """
        return self.ant

    def get_sig(self) -> Optional[Nodo]:
        """Devuelve el nodo siguiente en la lista.

        Returns:
            Optional[Nodo]: El nodo siguiente, o `None` si este es el último nodo.
        """
        return self.sig

    def get_dato(self) -> Any:
        """Devuelve el dato almacenado en el nodo.

        Returns:
            Any: El valor o dato contenido en el nodo.
        """
        return self.dato
