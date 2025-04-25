class Turno:
    def __init__(self, profesional, paciente, dia, hora):
        # Valido que cada objeto sea instancia de la clase correspondiente
        self.profesional = profesional
        self.paciente = paciente
        self.dia = dia
        self.hora = hora

    def __repr__(self):
        return "Turno de {} a {} el dia {} a las {}".format(
            self.paciente, self.profesional, self.dia, self.hora
        )

    def __str__(self):
        return self.__repr__()
