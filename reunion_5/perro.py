from mascota import Mascota


class Perro(Mascota):
    def __init__(self, nombre, esLazarillo):
        super().__init__(nombre)
        self.esLazarillo = True

    def saludar(self):
        print("Guau")
