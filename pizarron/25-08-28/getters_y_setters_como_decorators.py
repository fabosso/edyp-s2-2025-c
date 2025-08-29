class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Usamos _ para indicar que es "privado"
        self._edad = edad

    # PROPERTY para 'nombre' (getter)
    @property
    def nombre(self):
        """Devuelve el nombre de la persona"""
        return self._nombre.title()  # Siempre devuelve con formato Title Case

    # SETTER para 'nombre'
    @nombre.setter
    def nombre(self, valor):
        """Establece el nombre con validación"""
        if not isinstance(valor, str):
            raise TypeError("El nombre debe ser una cadena")
        if len(valor.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    # PROPERTY para 'edad' (getter)
    @property
    def edad(self):
        """Devuelve la edad de la persona"""
        return self._edad

    # SETTER para 'edad'
    @edad.setter
    def edad(self, valor):
        """Establece la edad con validación"""
        if not isinstance(valor, (int, float)):
            raise TypeError("La edad debe ser un número")
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        if valor > 150:
            raise ValueError("La edad no puede ser mayor a 150")
        self._edad = int(valor)

    # PROPERTY calculada (solo getter, no setter)
    @property
    def es_mayor_de_edad(self):
        """Calcula si es mayor de edad (solo lectura)"""
        return self._edad >= 18

    @property
    def categoria_edad(self):
        """Devuelve la categoría según la edad"""
        if self._edad < 13:
            return "Niño"
        elif self._edad < 18:
            return "Adolescente"
        elif self._edad < 65:
            return "Adulto"
        else:
            return "Adulto Mayor"


# PROBANDO LA CLASE CON PROPIEDADES
# ----------------------------------
print("Creando persona válida:")
persona = Persona("ana garcía", 28)
print(f"Nombre: {persona.nombre}")  # Se formatea automáticamente
print(f"Edad: {persona.edad}")
print(f"Es mayor de edad: {persona.es_mayor_de_edad}")
print(f"Categoría: {persona.categoria_edad}")
print()

print("Modificando valores válidos:")
persona.nombre = "  carlos ruiz  "  # Se limpia automáticamente
persona.edad = 16
print(f"Nuevo nombre: {persona.nombre}")
print(f"Nueva edad: {persona.edad}")
print(f"Es mayor de edad: {persona.es_mayor_de_edad}")
print(f"Categoría: {persona.categoria_edad}")
print()