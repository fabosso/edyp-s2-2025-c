"""
Clase Usuario para el Sistema de Gestión de Biblioteca
Representa un usuario
"""

from typing import List
from Libro import Libro


class Usuario:
    """Clase que representa un usuario de la biblioteca"""

    def __init__(self, nombre: str, dni: str):
        """Constructor de la clase Usuario"""
        self.__nombre = nombre
        self.__dni = dni
        self.__libros_prestados: List['Libro'] = []  # Lista de objetos Libro actualmente prestados

    # Métodos getter
    def get_nombre(self) -> str:
        """Obtiene el nombre del usuario"""
        return self.__nombre

    def get_dni(self) -> str:
        """Obtiene el DNI del usuario"""
        return self.__dni

    def get_libros_prestados(self) -> List[Libro]:
        """Obtiene la lista de libros actualmente prestados (copia)"""
        return self.__libros_prestados.copy()

    # Métodos setter
    def set_nombre(self, nombre: str) -> None:
        """Establece el nombre del usuario"""
        self.__nombre = nombre

    # Métodos de funcionalidad
    def pedir_libro_prestado(self, libro: Libro) -> None:
        """Solicita el préstamo de un libro"""
        # Verificar que no tenga ya este libro prestado
        for libro_prestado in self.__libros_prestados:
            if libro_prestado.get_isbn() == libro.get_isbn():
                raise ValueError("El usuario ya tiene este libro prestado.")

        # Intentar prestar el libro
        try:
            libro.prestar()
            self.__libros_prestados.append(libro)
        except ValueError as e:
            raise ValueError(f"No se pudo prestar el libro: {e}")

    def devolver_libro_prestado(self, libro: Libro) -> None:
        """Devuelve un libro prestado"""
        if libro not in self.__libros_prestados:
            raise ValueError("El usuario no tiene este libro prestado.")

        # Intentar devolver el libro
        try:
            libro.devolver()
            self.__libros_prestados.remove(libro)
        except ValueError as e:
            raise ValueError(f"No se pudo devolver el libro: {e}")

    def ver_libros_prestados(self) -> str:
        """Muestra los libros actualmente prestados"""
        if not self.__libros_prestados:
            return "No tienes libros prestados actualmente"

        libros = f"\nLibros Prestados - {self.__nombre}:\n"
        libros += "=" * 50 + "\n"

        for libro in self.__libros_prestados:
            libros += f"{libro}\n"
            libros += "-" * 50 + "\n"

        return libros

    def __str__(self) -> str:
        """Representación en cadena del usuario"""
        return f"{self.__nombre} (DNI: {self.__dni})"