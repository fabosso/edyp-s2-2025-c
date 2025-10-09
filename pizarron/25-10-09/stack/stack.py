from typing import Any, Optional

# Se asume que la clase Nodo documentada anteriormente está en un archivo llamado nodo.py
from nodo import Nodo


class Stack:
    """Implementa una estructura de datos de Pila (Stack) tipo LIFO (Last-In, First-Out).

    Esta implementación utiliza una lista doblemente enlazada de Nodos como
    base de almacenamiento.

    Attributes:
        top (Optional[Nodo]): El nodo que se encuentra en la cima de la pila.
                              Es el último elemento que se añadió.
        length (int): El número actual de elementos en la pila.
    """

    def __init__(self) -> None:
        """Inicializa una pila vacía."""
        self.top: Optional[Nodo] = None
        self.length: int = 0

    def push(self, dato: Any) -> None:
        """Añade un elemento a la cima de la pila.

        Args:
            dato (Any): El dato o valor que se va a añadir a la pila.
        """
        new: Nodo = Nodo(dato)
        if not self.top:
            # Si la pila está vacía, el nuevo nodo es la cima.
            self.top = new
        else:
            # Si ya hay elementos, se enlaza el nuevo nodo con la cima actual.
            self.top.set_sig(new)
            new.set_ant(self.top)
            # El nuevo nodo se convierte en la nueva cima.
            self.top = new
        self.length += 1

    def pop(self) -> Optional[Any]:
        """Elimina y devuelve el elemento en la cima de la pila.

        Returns:
            Optional[Any]: El dato del elemento que estaba en la cima,
                           o None si la pila está vacía.
        """
        if not self.top:
            return None

        dato_a_retornar = self.top.get_dato()

        if self.length == 1:
            # Si solo queda un elemento, la pila queda vacía.
            self.top = None
        else:
            # La nueva cima es el nodo anterior.
            self.top = self.top.get_ant()
            if self.top:
                # Se rompe el enlace hacia el nodo que acabamos de quitar.
                self.top.set_sig(None)

        self.length -= 1
        return dato_a_retornar

    def __len__(self) -> int:
        """Devuelve el número de elementos en la pila.

        Permite usar la función `len()` sobre una instancia de la pila.
        Ejemplo: `len(mi_pila)`

        Returns:
            int: La cantidad de elementos en la pila.
        """
        return self.length

    def __str__(self) -> str:
        """Devuelve una representación en string de la pila.

        Muestra la pila desde la base hasta la cima.
        Ejemplo: "[elemento_base, ..., elemento_cima]"

        Returns:
            str: La representación de la pila como una lista.
        """
        # --- CORRECCIÓN ---
        # La implementación original tenía un error que no imprimía el primer
        # elemento (la base de la pila). Esta versión es más clara y correcta.
        items = []
        aux = self.top
        while aux is not None:
            items.append(str(aux.get_dato()))
            aux = aux.get_ant()
        # Los items se recogen de cima a base, así que los invertimos para mostrarlos
        # desde la base hasta la cima.
        return f"[{', '.join(reversed(items))}]"


def validar_parentesis(expresion: str) -> None:
    """Verifica si una cadena de paréntesis está balanceada.

    Utiliza una Pila para llevar la cuenta de los paréntesis de apertura
    que no han sido cerrados. Imprime en consola si la expresión está
    balanceada o no.

    Args:
        expresion (str): La cadena de caracteres que contiene solo '()'
                         para ser validada.
    """
    pila = Stack()

    for caracter in expresion:
        if caracter == "(":
            pila.push(caracter)
        elif caracter == ")":
            # Si encontramos un ')' pero la pila está vacía, es un error.
            if len(pila) == 0:
                print(f"Expresión '{expresion}': Desbalanceados")
                return
            # Si no está vacía, hacemos pop para balancear un '('.
            pila.pop()

    # Al final, la pila debe estar vacía para que la expresión esté balanceada.
    if len(pila) == 0:
        print(f"Expresión '{expresion}': Balanceados!")
    else:
        print(f"Expresión '{expresion}': Desbalanceados")


# El bloque __name__ == "__main__" permite que este código se ejecute solo
# cuando el archivo se corre como un script principal.
if __name__ == "__main__":
    print("--- Validando Expresiones de Paréntesis ---")
    validar_parentesis("()((()))()")  # Correcto
    validar_parentesis("(()")  # Incorrecto
    validar_parentesis(")()()(")  # Incorrecto
    validar_parentesis(")))))))))))))))")  # Incorrecto
    validar_parentesis("((()))")  # Correcto
    validar_parentesis("()()()")  # Correcto
    validar_parentesis("())")  # Incorrecto
