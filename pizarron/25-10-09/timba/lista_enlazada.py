from nodo import Nodo
import random

class ListaCircularEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
            return
        # La lista no esta vacia
        self.cola.siguiente = nuevo_nodo
        self.cola = nuevo_nodo
        nuevo_nodo.siguiente = self.cabeza


    def buscar_final(self):
        return self.cola

    def esta_vacia(self):
        return self.cabeza == None

    def eliminar_elemento(self, buscado):
        # Caso 1 - La lista esta vacia
        error = ValueError("Elemento no existe")
        if self.esta_vacia():
            raise error
        # Caso 2 - Es el primero nodo
        if self.cabeza.dato == buscado:
            self.cabeza = self.cabeza.siguiente
            return None
        # Caso 3 - Esta en el medio
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        encontrado = False
        while actual != self.cola and not encontrado:
            if actual.dato == buscado:
                encontrado = True
            else:
                anterior = actual
                actual = actual.siguiente
        if encontrado:
            anterior.siguiente = actual.siguiente
            return None
        # Caso 4 - Es el ultimo
        if actual.dato == buscado:
            anterior.siguiente = self.cabeza
            self.cola = anterior
            return None
        return error

    def obtener_siguiente(self):
        if not self.actual:
            self.actual = self.cabeza
            return self.actual.dato
        self.actual = self.actual.siguiente
        return self.actual.dato

    def longitud(self):
        contador = 0
        if self.esta_vacia():
            return contador
        actual = self.cabeza
        while actual.siguiente != self.cola:
            contador += 1
            actual = actual.siguiente
        return contador




if __name__ == "__main__":

    mi_lista = ListaCircularEnlazada()

    print(f"Longitud lista -> {mi_lista.longitud()}")



    # Agregar todos los números clásicos de la ruleta casino americana
    numeros_colores = [
        ("00", "Verde"),
        ("0", "Verde"),
        ("1", "Rojo"), ("2", "Negro"), ("3", "Rojo"), ("4", "Negro"), ("5", "Rojo"), ("6", "Negro"),
        ("7", "Rojo"), ("8", "Negro"), ("9", "Rojo"), ("10", "Negro"), ("11", "Negro"), ("12", "Rojo"),
        ("13", "Negro"), ("14", "Rojo"), ("15", "Negro"), ("16", "Rojo"), ("17", "Negro"), ("18", "Rojo"),
        ("19", "Rojo"), ("20", "Negro"), ("21", "Rojo"), ("22", "Negro"), ("23", "Rojo"), ("24", "Negro"),
        ("25", "Rojo"), ("26", "Negro"), ("27", "Rojo"), ("28", "Negro"), ("29", "Negro"), ("30", "Rojo"),
        ("31", "Negro"), ("32", "Rojo"), ("33", "Negro"), ("34", "Rojo"), ("35", "Negro"), ("36", "Rojo")
    ]
    for numero, color in numeros_colores:
        mi_lista.agregar(f"{numero} - {color}")

    print(f"Longitud lista -> {mi_lista.longitud()}")

    # La lista gira infinitamente sin importar cuántas veces se llame
    for _ in range(random.randint(1, 1000)):
        print(mi_lista.obtener_siguiente())

    numero = mi_lista.obtener_siguiente()
    print(f"Número ganador: {numero}")


    print("Remuevo el primero")
    mi_lista.eliminar_elemento("00 - Verde")

    print("Remuveo del medio")
    mi_lista.eliminar_elemento("04 - Negro")

    print("Remuevo el ultimo")
    mi_lista.eliminar_elemento("17 - Negro")


    for _ in range(mi_lista.longitud()):
        print(mi_lista.obtener_siguiente())

    numero = mi_lista.obtener_siguiente()
    print(f"Número ganador: {numero}")

    print(f"Longitud lista -> {mi_lista.longitud()}")
