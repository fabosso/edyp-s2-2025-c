class SistemaMembresias:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def esta_activo(self, usuario):
        return usuario in self.usuarios
