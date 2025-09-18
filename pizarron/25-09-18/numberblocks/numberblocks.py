# solo para los type hints, no es necesario.
from __future__ import annotations
from typing import Any, Dict, List


class ValidationError(Exception):
    """Excepción personalizada para errores de validación"""
    pass


class Validador:
    @classmethod
    def validar_entero(cls, valor: Any, nombre_campo: str = "Campo") -> int:
        """Valida que el valor sea un entero válido. Retorna el entero si es válido."""
        if type(valor) != int:
            raise ValidationError(
                f"{nombre_campo} debe ser un número entero válido. Valor recibido: '{valor}'")

        return int(valor)

    @classmethod
    def validar_positivo(cls, valor: Any, nombre_campo: str = "Campo") -> int:
        """Valida que el valor sea un entero positivo válido. Retorna el positivo si es válido."""
        try:
            cls.validar_entero(valor, nombre_campo)
            if valor < 0:
                raise ValidationError(
                    f"{nombre_campo} debe ser un número positivo. Valor recibido: '{valor}'")
            return int(valor)
        except ValidationError:
            raise ValidationError(
                f"{nombre_campo} debe ser un número positivo. Valor recibido: '{valor}'")

    @classmethod
    def validar_negativo(cls, valor: Any, nombre_campo: str = "Campo") -> int:
        """Valida que el valor sea un entero negativo válido. Retorna el negativo si es válido."""
        try:
            cls.validar_entero(valor, nombre_campo)
            if valor >= 0:
                raise ValidationError(
                    f"{nombre_campo} debe ser un número negativo. Valor recibido: '{valor}'")
            return int(valor)
        except ValidationError:
            raise ValidationError(
                f"{nombre_campo} debe ser un número negativo. Valor recibido: '{valor}'")


class Numberblock:
    # Atributos de clase = globales para TODOS los Numberblock
    colores: List[str] = ["violeta", "rojo", "naranja", "amarillo", "verde"]
    characters: Dict[int, List[Numberblock]] = {}

    def __init__(self, valor: int, color: str, personalidad: list):
        self.valor = Validador.validar_positivo(valor, nombre_campo="Valor NB")
        self.color = self.validar_color(color)
        self.atributos = self.validar_personalidad(personalidad)

        # Agregamos numberblock al diccionario
        self.registrar_nb(self)

    def validar_color(self, color: str) -> str:
        if color not in Numberblock.colores:
            raise ValueError("Color inválido.")

        # Todo validado:
        return color

    def validar_personalidad(self, personalidad: list) -> list:
        if type(personalidad) != list:
            raise ValueError("Personalidad debe tener al menos un atributo")
        if not personalidad:
            raise ValueError("Personalidad debe tener al menos un atributo")

        # Todo validado:
        return personalidad


    def registrar_nb(self, nb: Numberblock):
        if not isinstance(nb, Numberblock):
            raise TypeError(
                "Error en registrar_nb: el nb pasado por parámetro no es de tipo Numberblock")

        if nb.valor not in self.characters:
            # creo una nueva lista vacía
            self.characters[nb.valor] = []

        # agrego a la lista el objeto Numberblock
        self.characters[nb.valor].append(nb)

    def es_perfecto(self) -> bool:
        raiz_cuadrada = self.valor ** 0.5

        # Retorna True si la raiz cuadrada del valor es un número entero
        return raiz_cuadrada == int(raiz_cuadrada)

    def __repr__(self) -> str:
        presentacion = f"Soy el número {self.valor}, soy {self.color}."
        if self.es_perfecto():
            presentacion += " Soy un cuadrado perfecto."

        return presentacion

    def replicar(self) -> Numberblock:
        return Numberblock(self.valor, self.color, self.atributos)

    def __eq__(self, other: Numberblock):
        "Método necesario para establecer la igualdad de las réplicas"
        print(self.__dict__)
        return self.__dict__ == other.__dict__

    def combinar_con(self, other: Numberblock) -> Numberblock:
        if not isinstance(other, Numberblock):
            raise TypeError(f'No se puede combinar. Tipo "{type(other)}" inválido')

        suma = self.valor + other.valor

        if suma not in Numberblock.characters:
            # construyo un numberblock nuevo
            resultado = Numberblock(suma, self.color, other.atributos)
        else:
            # reutilizo el primer valor de los Numberblocks existentes con ese numero
            resultado = Numberblock.characters[suma][0]
            # lo registro en el diccionario:
            self.registrar_nb(resultado)

        return resultado

    def personalidad(self):
        for attr in self.atributos:
            print(attr)

    @classmethod
    def personajes(cls):
        personajes_ordenados = dict(sorted(cls.characters.items()))

        for valor in personajes_ordenados:
            replicas_nb = personajes_ordenados[valor]
            nb_original = replicas_nb[0]
            print(f"#{valor}: '{nb_original}' - Réplicas: {len(replicas_nb)}")


class Rebelblock(Numberblock):
    def __init__(self, valor: int, color: str, personalidad: list):
        self.valor = Validador.validar_negativo(valor, nombre_campo="Valor RB")
        if self.valor in self.characters:
            raise ValueError("Este Rebelblock ya existe")
        self.color = self.validar_color(color)
        self.atributos = self.validar_personalidad(personalidad)

        super().registrar_nb(self)

    def validar_color(self, color: str) -> str:
        if color in Rebelblock.colores:
            raise ValueError("Color inválido.")

        # Todo validado:
        return color

    def replicar(self) -> None:
        print("No me replico, no insistas.")

    def combinar_con(self, other) -> None:
        print("No quiero combinarme!")

    def __repr__(self):
        return f"Soy {self.valor}, y me jacto de ser negativo."


def prueba_1():
    nb_1 = Numberblock(1, "rojo", ["lindo", "amable"])
    nb_1_rep = nb_1.replicar()

    print(nb_1 == nb_1_rep)

    Numberblock.personajes()


def prueba_2():
    nb_invalido = Numberblock(1.14, "rojo", ["lindo", "amable"])

def prueba_3():
    nb_3 = Numberblock(3, "amarillo", ["curioso", "entusiasta"])
    nb_4 = Numberblock(4, "verde", ["amable", "bueno"])

    nb_7 = nb_3.combinar_con(nb_4)

    Numberblock.personajes()

    nb_7.personalidad()

def prueba_4():
    rb_invalido = Rebelblock(1, "violeta", ["maquiavelico"])

def prueba_5():
    rebelblock = Rebelblock(-1, "negro", ["triste"])
    rebelblock.replicar()

    Rebelblock.personajes()

if __name__ == "__main__":
    prueba_5()