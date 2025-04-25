class Mascota:

    # Atributos de clase
    ids_usados = []
    TIPOS = ["Perro", "Gato", "Tortuga"]  # en mayúscula porque es CONSTANTE

    # Constructor
    def __init__(self, nombre, id, tipo, edad, disponibilidad):
        self.set_nombre(nombre)
        self.set_id(id)
        self.set_tipo(tipo)
        self.set_edad(edad)
        self.set_disponibilidad(disponibilidad)

    # Setters
    def set_nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena")

        if len(nombre.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío")

        if not nombre.strip().isalpha():
            raise ValueError("El nombre debe contener letras únicamente")

        self.nombre = nombre

    def set_id(self, id):
        if not isinstance(id, int):
            raise TypeError("El id debe ser numérico")

        if id < 0:
            raise ValueError("El id debe ser un número positivo")

        if id in Mascota.ids_usados:
            raise ValueError(f"{id} ya existe")

        self.id = id
        Mascota.ids_usados.append(id)

    def set_tipo(self, tipo):
        if not isinstance(tipo, str):
            raise TypeError("El tipo debe ser una cadena")

        if len(tipo.strip()) == 0:
            raise ValueError("El no puede ser vacío")

        if tipo not in Mascota.TIPOS:
            raise ValueError(f"{tipo} no es un tipo válido")

        self.tipo = tipo

    def set_edad(self, edad):
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un entero")

        if edad < 0:
            raise ValueError("La edad debe ser un número positivo")

        if edad > 20:
            raise ValueError("La edad no puede ser mayor a 20")

        self.edad = edad

    def set_disponibilidad(self, disponibilidad):
        if not isinstance(disponibilidad, bool):
            raise TypeError("La disponibilidad debe ser un booleano")

        self.disponibilidad = disponibilidad

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_id(self):
        return self.id

    def get_tipo(self):
        return self.tipo

    def get_edad(self):
        return self.edad

    def get_disponibilidad(self):
        return self.disponibilidad

    # Magic methods

    # Representación user-friendly
    def __str__(self):
        if self.get_disponibilidad():
            return (
                f"{self.nombre} ({self.tipo}), Edad: {self.edad} años, Disponible: Sí"
            )
        return f"{self.nombre} ({self.tipo}), Edad: {self.edad} años, Disponible: No"

    # Representación técnica
    def __repr__(self):
        return f"Mascota(nombre={repr(self.nombre)}, id={self.id}, tipo={repr(self.tipo)}, edad={self.edad}, disponibilidad={self.disponibilidad})"

    # Equals
    def __eq__(self, otra):
        if not isinstance(otra, Mascota):
            return False
        return self.get_tipo() == otra.get_tipo()

    # Delete
    def __del__(self):
        print(f"{self.get_nombre()} fue destruido")
        Mascota.ids_usados.remove(self.id)


if __name__ == "__main__":
    # Crear instancias de Mascota
    mascota1 = Mascota("Max", 101, "Perro", 3, True)
    mascota2 = Mascota("Luna", 102, "Gato", 2, False)
    mascota3 = Mascota("Rex", 103, "Perro", 5, True)

    # Imprimir objetos usando __str__ y __repr__
    print(mascota1)  # Max (Perro), Edad: 3 años, Disponible: Sí
    print(
        repr(mascota2)
    )  # Mascota(nombre='Luna', id=102, tipo='Gato', edad=2, disponibilidad=False)

    # Comparación con __eq__
    print(mascota1 == mascota3)  # True (ambos son "Perro")
    print(mascota1 == mascota2)  # False (uno es "Perro" y el otro "Gato")

    # Listas de mascotas
    lista_mascotas = [mascota1, mascota2, mascota3]
    print(lista_mascotas)  # Se imprimen con __repr__ por estar en una lista

    # Intentamos crear una mascota con un ID repetido
    try:
        mascota4 = Mascota("Bobby", 101, "Tortuga", 4, True)
    except ValueError as e:
        print(f"Error: {e}")  # Error: 101 ya existe
    # Al capturar el error en este punto, el hilo de ejecución no se "corta"

    # Intentamos crear una mascota de un tipo no permitido
    try:
        mascota5 = Mascota("Simba", 110, "León", 3, True)
    except ValueError as e:
        print(f"Error: {e}")  # Error: León no es un tipo válido

    # Eliminar una mascota
    del mascota2  # "Luna fue destruido" y su ID se elimina de ids_usados

    # Verificar que el ID 102 se eliminó correctamente
    try:
        mascota6 = Mascota("Nala", 102, "Gato", 1, True)
        print(f"{mascota6.get_nombre()} creada con ID {mascota6.get_id()}")
    except ValueError as e:
        print(f"Error: {e}")
