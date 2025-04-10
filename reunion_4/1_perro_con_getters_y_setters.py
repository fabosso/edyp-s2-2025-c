class Perro:
    # Constructor
    def __init__(self, nombre_constructor, edad_constructor, raza_constructor):
        self.set_nombre(nombre_constructor)
        self.set_edad(edad_constructor)
        self.set_raza(raza_constructor)

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_raza(self):
        return self.raza

    # Setters
    def set_nombre(self, nombre_nuevo):
        self.nombre = nombre_nuevo

    def set_edad(self, edad_nueva):
        self.edad = edad_nueva

    def set_raza(self, raza_nueva):
        self.raza = raza_nueva

    # Métodos
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau, guau!"

    def descripcion(self):
        return f"{self.nombre} es un {self.raza} de {self.edad} años."

# Ejemplo de uso
if __name__ == "__main__":
    mi_perro = Perro("Fido", 3, "Labrador")
    print(mi_perro.descripcion())
    print(mi_perro.ladrar())

    try:
        mi_otro_perro = Perro("Rex", -2, "Pastor Alemán")
    except:
        print("El perro no fue construido")