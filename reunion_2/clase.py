class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau, guau!"

    def descripcion(self):
        return f"{self.nombre} es un {self.raza} de {self.edad} años."


# Ejemplo de uso
if __name__ == "__main__":
    mi_perro = Perro("Fido", 3, "Labrador")
    print(mi_perro.descripcion())
    print(mi_perro.ladrar())
