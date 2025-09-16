from Validador import Validador as V


class Usuario:
    def __init__(self, nombre: str, edad: int, codigo: str):
        # Las validaciones lanzan excepciones automáticamente si fallan
        self.nombre = V.validar_solo_letras(nombre, "Nombre")
        self.nombre = V.validar_longitud(self.nombre, 2, 50, "Nombre")

        self.edad = V.validar_entero_en_rango(edad, 0, 120, "Edad")

        self.codigo = V.validar_alfanumerico(codigo, "Código")
        self.codigo = V.validar_longitud(self.codigo, 4, 8, "Código")
