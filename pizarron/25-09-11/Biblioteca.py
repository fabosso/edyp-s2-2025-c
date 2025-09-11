from typing import Optional, Dict

from Libro import Libro
from Usuario import Usuario


class Biblioteca:
    """
    Clase que representa la biblioteca y gestiona libros y usuarios.

    Args:
        nombre (str): Nombre de la biblioteca
    """

    def __init__(self, nombre: str):
        """
        Constructor de la clase Biblioteca.

        Args:
            nombre (str): Nombre de la biblioteca
        """
        self.__nombre = nombre
        self.__libros: Dict[str, Libro] = {}  # Diccionario {isbn: Libro}
        self.__usuarios: Dict[str, Usuario] = {}  # Diccionario {dni: Usuario}

    # Métodos getter y setter
    def get_nombre(self) -> str:
        """
        Obtiene el nombre de la biblioteca.

        Returns:
            str: Nombre de la biblioteca
        """
        return self.__nombre

    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre de la biblioteca.

        Args:
            nombre (str): Nuevo nombre de la biblioteca
        """
        self.__nombre = nombre

    # Métodos de gestión de libros
    def agregar_libro(self, libro: Libro) -> None:
        """
        Agrega un libro a la biblioteca.

        Args:
            libro (Libro): Libro a agregar
        """
        # Verificar que no exista un libro con el mismo ISBN
        isbn = libro.get_isbn()
        if isbn in self.__libros:
            print("El libro con este ISBN ya existe en la biblioteca")
            return

        self.__libros[isbn] = libro

    def eliminar_libro(self, isbn: str) -> None:
        """
        Elimina un libro de la biblioteca por ISBN.

        Args:
            isbn (str): ISBN del libro a eliminar
        """
        if isbn not in self.__libros:
            print("No se encontró un libro con este ISBN")
            return

        libro = self.__libros[isbn]
        if not libro.get_disponible():
            print("No se puede eliminar: el libro está prestado")
            return

        del self.__libros[isbn]

    def buscar_libro(self, isbn: str) -> Optional[Libro]:
        """
        Busca un libro en la biblioteca según su ISBN.

        Args:
            isbn (str): ISBN del libro a buscar

        Returns:
            Optional[Libro]: Libro encontrado o None si no existe
        """
        return self.__libros.get(isbn)

    def modificar_informacion_libro(self, isbn: str, titulo: str, autor: str, editorial: str) -> None:
        """
        Modifica la información de un libro.

        Args:
            isbn (str): ISBN del libro a modificar
            titulo (str): Nuevo título
            autor (str): Nuevo autor
            editorial (str): Nueva editorial
        """
        libro = self.buscar_libro(isbn)

        if not libro:
            print(f"No se encontró un libro con este ISBN: {isbn}")
            return

        libro.set_titulo(titulo)
        libro.set_autor(autor)
        libro.set_editorial(editorial)

    # Métodos de gestión de usuarios
    def agregar_usuario(self, usuario: Usuario) -> None:
        """
        Agrega un usuario a la biblioteca.

        Args:
            usuario (Usuario): Usuario a agregar
        """

        # Verificar que no exista un usuario con el mismo DNI
        dni = usuario.get_dni()
        if dni in self.__usuarios:
            print("El usuario con este DNI ya existe en la biblioteca")
            return

        self.__usuarios[dni] = usuario

    def eliminar_usuario(self, dni: str) -> None:
        """
        Elimina un usuario de la biblioteca.

        Args:
            dni (str): DNI del usuario a eliminar
        """
        if dni not in self.__usuarios:
            print("No se encontró un usuario con este DNI")
            return

        # Verificar que no tenga libros prestados
        usuario = self.__usuarios[dni]
        if usuario.get_libros_prestados():
            print("No se puede eliminar: el usuario tiene libros prestados")
            return

        del self.__usuarios[dni]

    def buscar_usuario(self, dni: str) -> Optional[Usuario]:
        """
        Busca un usuario por DNI.

        Args:
            dni (str): DNI del usuario a buscar

        Returns:
            Optional[Usuario]: Usuario encontrado o None si no existe
        """
        return self.__usuarios.get(dni)

    def modificar_informacion_usuario(self, dni: str, nombre: str) -> None:
        """
        Modifica la información de un usuario.

        Args:
            dni (str): DNI del usuario a modificar
            nombre (str): Nuevo nombre
        """
        usuario = self.buscar_usuario(dni)

        if not usuario:
            print(f"No se encontró un usuario con este DNI: {dni}")
            return

        usuario.set_nombre(nombre)

    # Métodos de gestión de préstamos
    def prestar_libro(self, dni_usuario: str, isbn_libro: str) -> None:
        """
        Gestiona el préstamo de un libro a un usuario.

        Args:
            dni_usuario (str): DNI del usuario
            isbn_libro (str): ISBN del libro
        """
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
        """
        Gestiona la devolución de un libro.

        Args:
            dni_usuario (str): DNI del usuario
            isbn_libro (str): ISBN del libro
        """
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
        """
        Lista todos los libros de la biblioteca.

        Returns:
            str: Representación de todos los libros
        """
        if not self.__libros:
            return "No hay libros en la biblioteca"

        lista = f"\nLibros en {self.__nombre}:\n"
        lista += "=" * 50 + "\n"

        for i, libro in enumerate(self.__libros.values(), 1):
            if libro.get_disponible():
                estado = "📗 Disponible"
            else:
                estado = "📕 Prestado"
            lista += f"{i}. {libro} - {estado}\n"

        return lista

    def listar_usuarios(self) -> str:
        """
        Lista todos los usuarios de la biblioteca.

        Returns:
            str: Representación de todos los usuarios
        """
        if not self.__usuarios:
            return "No hay usuarios registrados"

        lista = f"\nUsuarios de {self.__nombre}:\n"
        lista += "=" * 50 + "\n"

        for i, usuario in enumerate(self.__usuarios.values(), 1):
            libros_prestados = len(usuario.get_libros_prestados())
            lista += f"{i}. {usuario} - Libros prestados: {libros_prestados}\n"

        return lista

    def __str__(self) -> str:
        """
        Representación en cadena de la biblioteca.

        Returns:
            str: Representación de la biblioteca
        """
        return f"Biblioteca: {self.__nombre} ({len(self.__libros)} libros, {len(self.__usuarios)} usuarios)"