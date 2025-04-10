from mascota import Mascota

class Gato(Mascota):
    def __init__(self, nombre, esLazarillo):
        super().__init__(nombre)
        self.esSociable = True

    def saludar(self):
        print("miau!")