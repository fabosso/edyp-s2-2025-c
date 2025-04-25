from perro import Perro
from gato import Gato


bobi = Perro("bobi", True)
cati = Gato("Cati", False)

mis_mascotas = []
mis_mascotas.append(bobi)
mis_mascotas.append(cati)
mis_mascotas.append(123)


for mascota in mis_mascotas:
    mascota.saludar()
