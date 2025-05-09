class Paciente:
    dnis_pacientes = []

    def validar_dni(dni):
        int(dni)
        return dni

    def __init__(self, dni, nombre):
        if dni in Paciente.dnis_pacientes:
            raise ValueError("El dni ingresado ya existe!")
        self.dni = Paciente.validar_dni(dni)
        Paciente.dnis_pacientes.append(dni)
        if nombre:
            self.nombre = nombre

    def __repr__(self):
        return self.nombre

    def __str__(self):
        return self.__repr__()
