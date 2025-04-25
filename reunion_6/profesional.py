class Profesional:
    registros = []

    def validar_registro(registro):
        if registro in Profesional.registros:
            raise ValueError("Registro invalido ya existe!")
        return registro

    def atender(self, paciente):
        print("{prof} Atendiendo a {paciente}".format(paciente=paciente, prof=self))

    def __init__(self, nombre, registro):
        self.registro = Profesional.validar_registro(registro)
        if nombre:
            self.nombre = nombre

    def __repr__(self):
        return "Dr." + self.nombre

    def __str__(self):
        return self.__repr__()
