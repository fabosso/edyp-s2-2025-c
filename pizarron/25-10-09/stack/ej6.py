class Nodo:
    """
    Clase para representar un nodo en una lista doblemente enlazada.
    """
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def __repr__(self):
        return str(self.dato)

class ListaDoblementeEnlazada:
    """
    Clase para la lista doblemente enlazada.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.tail
            self.tail = nuevo_nodo

    def __repr__(self):
        nodos = []
        nodo_actual = self.head
        while nodo_actual:
            nodos.append(str(nodo_actual.dato))
            nodo_actual = nodo_actual.siguiente
        return " <-> ".join(nodos) if nodos else "Lista vacía"

    def encontrar_sublista_consecutiva_mas_larga(self):
        """
        Encuentra la sublista consecutiva más larga sin usar listas de Python
        como almacenamiento intermedio. Devuelve una nueva ListaDoblementeEnlazada.
        """
        if not self.head:
            return ListaDoblementeEnlazada()

        longitud_maxima = 0
        inicio_sublista_maxima = None # Puntero al nodo inicial de la sublista más larga
        
        nodo_actual = self.head
        while nodo_actual:
            # Inicio de una nueva secuencia potencial
            inicio_secuencia_actual = nodo_actual
            longitud_actual = 1
            
            # Avanzamos para ver hasta dónde llega la secuencia consecutiva
            temp_nodo = nodo_actual
            while temp_nodo.siguiente and temp_nodo.siguiente.dato == temp_nodo.dato + 1:
                longitud_actual += 1
                temp_nodo = temp_nodo.siguiente
            
            # Comparamos la secuencia que acabamos de encontrar con la máxima registrada
            if longitud_actual > longitud_maxima:
                longitud_maxima = longitud_actual
                inicio_sublista_maxima = inicio_secuencia_actual
                
            # Movemos el puntero principal al nodo siguiente al final de la secuencia
            # que acabamos de procesar. Esto es una optimización clave.
            nodo_actual = temp_nodo.siguiente

        # Ahora construimos la lista de resultado a partir de nuestros hallazgos
        lista_resultado = ListaDoblementeEnlazada()
        if inicio_sublista_maxima:
            puntero_resultado = inicio_sublista_maxima
            for _ in range(longitud_maxima):
                lista_resultado.agregar_al_final(puntero_resultado.dato)
                puntero_resultado = puntero_resultado.siguiente
                
        return lista_resultado
    
# Crear una instancia de la lista doblemente enlazada
mi_lista = ListaDoblementeEnlazada()
numeros = [10, 11, 5, 6, 7, 8, 2, 3, 4, 9, 10, 11, 12, 13]
for num in numeros:
    mi_lista.agregar_al_final(num)

print(f"Lista original: {mi_lista}")
# Salida: Lista original: 10 <-> 11 <-> 5 <-> 6 <-> 7 <-> 8 <-> 2 <-> 3 <-> 4 <-> 9 <-> 10 <-> 11 <-> 12 <-> 13

# Encontrar la sublista consecutiva más larga usando el nuevo método
sublista_resultado = mi_lista.encontrar_sublista_consecutiva_mas_larga()

print(f"\nLa sublista consecutiva más larga es: {sublista_resultado}")
# Salida: La sublista consecutiva más larga es: 9 <-> 10 <-> 11 <-> 12 <-> 13

print(f"El tipo del objeto devuelto es: {type(sublista_resultado)}")
# Salida: El tipo del objeto devuelto es: <class '__main__.ListaDoblementeEnlazada'>