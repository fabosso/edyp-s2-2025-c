from Biblioteca import Biblioteca
from Libro import Libro
from Usuario import Usuario


# Ejemplo de uso del sistema
def ejemplo_uso():
    """Función de ejemplo para demostrar el uso del sistema"""

    # Crear biblioteca
    biblioteca = Biblioteca("Biblioteca Central")

    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-84-376-0494-7", "Sudamericana")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-84-376-0495-4", "Planeta")
    libro3 = Libro("1984", "George Orwell", "978-84-376-0496-1", "Debolsillo")

    # Crear usuarios
    usuario1 = Usuario("Ana García", "12345678A")
    usuario2 = Usuario("Carlos López", "87654321B")

    # Agregar libros y usuarios a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    biblioteca.agregar_usuario(usuario1)
    biblioteca.agregar_usuario(usuario2)

    # Demostrar funcionalidades
    print(biblioteca)
    print(biblioteca.listar_libros())
    print(biblioteca.listar_usuarios())

    # Realizar préstamos
    print("\n--- Realizando préstamos ---")
    biblioteca.prestar_libro("12345678A", "978-84-376-0494-7")
    biblioteca.prestar_libro("87654321B", "978-84-376-0495-4")

    print("\nLibros después de los préstamos:")
    print(biblioteca.listar_libros())

    print("\nLibros prestados a Ana García:")
    print(usuario1.ver_libros_prestados())

    # Devolver un libro
    print("\n--- Devolviendo libro ---")
    biblioteca.devolver_libro("12345678A", "978-84-376-0494-7")

    # print("\nHistorial de Ana García:")
    # print(usuario1.ver_historial_prestamos())


if __name__ == "__main__":
    ejemplo_uso()