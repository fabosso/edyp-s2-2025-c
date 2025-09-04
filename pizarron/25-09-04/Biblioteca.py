from typing import List, Optional

from Libro import Libro
from Usuario import Usuario


class Biblioteca:
    """Clase que representa la biblioteca y gestiona libros y usuarios"""

    def __init__(self, nombre: str):
        """Constructor de la clase Biblioteca"""
        self.__nombre = nombre
        self.__libros: List['Libro'] = []
        self.__usuarios: List['Usuario'] = []

    # Métodos getter y setter
    def get_nombre(self) -> str:
        """Obtiene el nombre de la biblioteca"""
        return self.__nombre

    def set_nombre(self, nombre: str) -> None:
        """Establece el nombre de la biblioteca"""
        self.__nombre = nombre

    # Métodos de gestión de libros
    def agregar_libro(self, libro: Libro) -> None:
        """Agrega un libro a la biblioteca"""
        # Verificar que no exista un libro con el mismo ISBN
        for libro_existente in self.__libros:
            if libro_existente.get_isbn() == libro.get_isbn():
                print("El libro con este ISBN ya existe en la biblioteca")
                return

        self.__libros.append(libro)

    def eliminar_libro(self, isbn: str) -> None:
        """Elimina un libro de la biblioteca por ISBN"""
        for libro in self.__libros:
            if libro.get_isbn() == isbn:
                if not libro.get_disponible():
                    print("No se puede eliminar: el libro está prestado")
                    return
                self.__libros.remove(libro)
                return

        print("No se encontró un libro con este ISBN")

    def buscar_libro(self, isbn: str) -> Optional[Libro]:
        """Busca un libro en la biblioteca según su ISBN"""
        for libro in self.__libros:
            if libro.get_isbn() == isbn:
                return libro
        return None

    def modificar_informacion_libro(self, isbn: str, titulo: str, autor: str, editorial: str) -> None:
        """Modifica la información de un libro"""
        libro = self.buscar_libro(isbn)

        if not libro:
            print(f"No se encontró un libro con este ISBN: {isbn}")
            return

        libro.set_titulo(titulo)
        libro.set_autor(autor)
        libro.set_editorial(editorial)


    # Métodos de gestión de usuarios
    def agregar_usuario(self, usuario: Usuario) -> None:
        """Agrega un usuario a la biblioteca"""

        # Verificar que no exista un usuario con el mismo DNI
        for usuario_existente in self.__usuarios:
            if usuario_existente.get_dni() == usuario.get_dni():
                print("El usuario con este DNI ya existe en la biblioteca")
                return

        self.__usuarios.append(usuario)

    def eliminar_usuario(self, dni: str) -> None:
        """Elimina un usuario de la biblioteca"""
        for usuario in self.__usuarios:
            if usuario.get_dni() == dni:
                # Verificar que no tenga libros prestados
                if usuario.get_libros_prestados():
                    print("No se puede eliminar: el usuario tiene libros prestados")
                    return

                self.__usuarios.remove(usuario)
                return

        print("No se encontró un usuario con este DNI")


    def buscar_usuario(self, dni: str) -> Optional[Usuario]:
        """Busca un usuario por DNI"""
        for usuario in self.__usuarios:
            if usuario.get_dni() == dni:
                return usuario
        return None

    def modificar_informacion_usuario(self, dni: str, nombre: str) -> None:
        """Modifica la información de un usuario"""
        usuario = self.buscar_usuario(dni)

        if not usuario:
            print(f"No se encontró un usuario con este DNI: {dni}")
            return

        usuario.set_nombre(nombre)

    # Métodos de gestión de préstamos
    def prestar_libro(self, dni_usuario: str, isbn_libro: str) -> None:
        """Gestiona el préstamo de un libro a un usuario"""
        usuario = self.buscar_usuario(dni_usuario)
        if not usuario:
            print("Usuario no encontrado")
            return

        libro = self.buscar_libro(isbn_libro)
        if not libro:
            print("Libro no encontrado")
            return

        try:
            usuario.pedir_libro_prestado(libro)
            print(f"Préstamo exitoso: {libro.get_titulo()} prestado a {usuario.get_nombre()}")
        except ValueError as e:
            print(f"No se pudo realizar el préstamo: {e}")


    def devolver_libro(self, dni_usuario: str, isbn_libro: str) -> None:
        """Gestiona la devolución de un libro"""
        usuario = self.buscar_usuario(dni_usuario)
        if not usuario:
            print("Usuario no encontrado")
            return

        libro = self.buscar_libro(isbn_libro)
        if not libro:
            print("Libro no encontrado")
            return

        try:
            usuario.devolver_libro_prestado(libro)
            print(f"Devolución exitosa: {libro.get_titulo()} devuelto por {usuario.get_nombre()}")
        except ValueError as e:
            print(f"No se pudo realizar la devolución: {e}")


    # Métodos de utilidad
    def listar_libros(self) -> str:
        """Lista todos los libros de la biblioteca"""
        if not self.__libros:
            return "No hay libros en la biblioteca"

        lista = f"\nLibros en {self.__nombre}:\n"
        lista += "=" * 50 + "\n"

        for i, libro in enumerate(self.__libros, 1):
            if libro.get_disponible():
                estado = "📗 Disponible"
            else:
                estado = "📕 Prestado"
            lista += f"{i}. {libro} - {estado}\n"

        return lista

    def listar_usuarios(self) -> str:
        """Lista todos los usuarios de la biblioteca"""
        if not self.__usuarios:
            return "No hay usuarios registrados"

        lista = f"\nUsuarios de {self.__nombre}:\n"
        lista += "=" * 50 + "\n"

        for i, usuario in enumerate(self.__usuarios, 1):
            libros_prestados = len(usuario.get_libros_prestados())
            lista += f"{i}. {usuario} - Libros prestados: {libros_prestados}\n"

        return lista

    def __str__(self) -> str:
        """Representación en cadena de la biblioteca"""
        return f"Biblioteca: {self.__nombre} ({len(self.__libros)} libros, {len(self.__usuarios)} usuarios)"