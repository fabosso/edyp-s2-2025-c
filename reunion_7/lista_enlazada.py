class Nodo:
    """ Clase Nodo para la lista simplemente enlazada """
    def __init__(self, dato):
        self._dato = dato
        self._sig = None

    def set_dato(self, dato):
        self._dato = dato

    def get_dato(self):
        return self._dato

    def get_sig(self):
        return self._sig

    def set_sig(self, sig):
        if not isinstance(sig, Nodo):
            raise TypeError("El siguiente nodo debe ser de tipo Nodo")
        self._sig = sig

    def __repr__(self):
        return str(self._dato)

    def __str__(self):
        return f"Nodo: {self._dato}"


class ListaEnlazada:
    """ Clase ListaEnlazada para la lista simplemente enlazada """
    def __init__(self):
        """ Todos los atributos de la clase son privados"""
        self._cabeza = None
        self._longitud = 0
        self._actual = None

    ##################################################
    ''' Metodos publicos de la clase ListaEnlazada '''
    ##################################################

    def append(self, dato):
        if self._esta_vacia():
            self._set_cabeza(Nodo(dato))
        else:
            aux = self._get_cabeza()
            while aux.get_sig() is not None:
                aux = aux.get_sig()
            aux.set_sig(Nodo(dato))
        self._incrementar_longitud()

    def insert(self, pos, dato):
        self._validar_posicion(pos)
        # Inserto a la cabeza
        if pos == 0:
            aux = self._get_cabeza()
            nuevo = Nodo(dato)
            nuevo.set_sig(aux)
            self._incrementar_longitud()
            return
        # Inserto en el medio
        ant, aux = self._recorrer_lista(pos)
        nuevo = Nodo(dato)
        ant.set_sig(nuevo)
        nuevo.set_sig(aux)
        self._incrementar_longitud()

    def sort(self, reverse=False, key=None):
        """Tarea pendiente: Implementar el metodo sort"""
        raise NotImplementedError("El metodo sort no esta implementado")

    def _swap(self, nodo1, nodo2):
        """Tarea pendiente: Implementar el metodo swap"""
        raise NotImplementedError("El metodo swap no esta implementado")

    def copy(self):
        """Tarea pendiente: Implementar el metodo copy"""
        raise NotImplementedError("El metodo copy no esta implementado")

    def clear(self):
        """Tarea pendiente: Implementar el metodo clear"""
        raise NotImplementedError("El metodo clear no esta implementado")

    def count(self, dato):
        """Tarea pendiente: Implementar el metodo count"""
        raise NotImplementedError("El metodo count no esta implementado")

    def extend(self, lista):
        """Tarea pendiente: Implementar el metodo extend"""
        raise NotImplementedError("El metodo extend no esta implementado")

    def pop(self, pos):
        """Tarea pendiente: Implementar el metodo pop"""
        raise NotImplementedError("El metodo pop no esta implementado")

    def remove(self, dato):
        """Tarea pendiente: Implementar el metodo remove"""
        raise NotImplementedError("El metodo remove no esta implementado")

    def index(self, dato):
        """Tarea pendiente: Implementar el metodo index"""
        raise NotImplementedError("El metodo index no esta implementado")

    ##################################################
    ''' Metodos privados de la clase ListaEnlazada '''
    ##################################################
    def _esta_vacia(self):
        return self._get_cabeza() is None

    def _get_cabeza(self):
        return self._cabeza

    def _set_cabeza(self, cabeza):
        if not isinstance(cabeza, Nodo):
            raise TypeError("La cabeza debe ser de tipo Nodo")
        self._cabeza = cabeza

    def _incrementar_longitud(self):
        self._longitud += 1

    def _decrementar_longitud(self):
        self._longitud -= 1

    def _validar_posicion(self, pos):
        # La posicion excede  la long de la lista
        if pos < 0 or pos >= len(
            self
        ):  # Cambiado de > a >= No puedo asignar a la longitud (emulando la lista de python)
            raise IndexError

    def _eliminar(self, pos):
        self._validar_posicion(pos)
        if pos == len(self):
            raise IndexError
        if pos == 0:
            aux = self._get_cabeza().get_sig()
            self._set_cabeza(aux)
            self._decrementar_longitud()
            return
        ant, aux = self._recorrer_lista(pos)
        ant.set_sig(aux.get_sig())
        self._decrementar_longitud()

    def _recorrer_lista(self, pos):
        self._validar_posicion(pos)
        aux = self._get_cabeza()
        ant = None
        for _ in range(pos):
            ant = aux
            aux = aux.get_sig()
        return ant, aux

    def _obtener_nodo(self, pos):
        _, aux = self._recorrer_lista(pos)
        return aux

    ##################################################
    ''' Metodos magicos  de la clase ListaEnlazada '''
    ##################################################

    def __repr__(self):
        resultado = "["
        aux = self._get_cabeza()
        if not aux:
            return "[]"
        while aux.get_sig() is not None:
            resultado += aux.__repr__()
            resultado += " -> "
            aux = aux.get_sig()
        resultado += aux.__repr__() + "]"
        return resultado

    def __len__(self):
        return self._longitud

    def __getitem__(self, pos):
        return self._obtener_nodo(pos)

    def __setitem__(self, pos, dato):
        aux = self._obtener_nodo(pos)
        aux.set_dato(dato)

    def __iter__(self):
        self._actual = self._get_cabeza()
        return self

    def __next__(self):
        if self._actual is None:
            raise StopIteration
        aux = self._actual
        self._actual = self._actual.get_sig()
        return aux

    def __delitem__(self, pos):
        self._eliminar(pos)


if __name__ == "__main__":
    lista_numeros = ListaEnlazada()
    lista_letras = ListaEnlazada()
    # Agregando elementos a la lista
    lista_numeros.append(1)
    lista_numeros.append(2)
    lista_numeros.append(3)
    lista_numeros.append(4)
    lista_numeros.append(5)
    lista_letras.append("a")
    lista_letras.append("b")
    lista_letras.append("c")
    lista_letras.append("d")
    lista_letras.append("e")
    # Imprimiendo la lista
    print("Listas originales")
    print(lista_numeros)
    print(lista_letras)
    # Eliminando elementos en la lista
    del lista_numeros[0]
    del lista_letras[3]
    del lista_letras[1]
    print("Listas reducidas")
    print(lista_numeros)
    print(lista_letras)
    # Modificando elementos en la lista
    lista_numeros[0] = 10
    lista_letras[0] = "z"
    print("Listas modificadas")
    print(lista_numeros)
    print(lista_letras)
    # Usando el iterador
    print("Iterando la lista")
    for i in lista_numeros:
        print(i)
    print("Iterando la lista")
    for i in lista_letras:
        print(i)
    print("Iterando en lista vacia")
    lista_vacia = ListaEnlazada()
    for i in lista_vacia:
        print(i)
    print("Longitud de la lista")
    print(len(lista_numeros))
    print(len(lista_letras))
    print("Fin del programa")
