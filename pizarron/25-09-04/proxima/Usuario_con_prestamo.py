"""
Clase Usuario para el Sistema de Gestión de Biblioteca
Representa un usuario con su historial de préstamos
"""

from typing import List, Optional
from Libro import Libro
from Prestamo import Prestamo


class Usuario:
    """Clase que representa un usuario de la biblioteca"""

    def __init__(self, nombre: str, dni: str):
        """Constructor de la clase Usuario"""
        self.__nombre = nombre
        self.__dni = dni
        self.__historial_prestamos: List['Prestamo'] = []  # Lista de objetos Prestamo
        self.__libros_prestados: List['Libro'] = []  # Lista de objetos Libro actualmente prestados

    # Métodos getter
    def get_nombre(self) -> str:
        """Obtiene el nombre del usuario"""
        return self.__nombre

    def get_dni(self) -> str:
        """Obtiene el DNI del usuario"""
        return self.__dni

    def get_historial_prestamos(self) -> List[Prestamo]:
        """Obtiene el historial de préstamos (copia de la lista)"""
        return self.__historial_prestamos.copy()

    def get_libros_prestados(self) -> List[Libro]:
        """Obtiene la lista de libros actualmente prestados (copia)"""
        return self.__libros_prestados.copy()

    # Métodos setter
    def set_nombre(self, nombre: str) -> None:
        """Establece el nombre del usuario"""
        self.__nombre = nombre

    def set_dni(self, dni: str) -> None:
        """Establece el DNI del usuario"""
        self.__dni = dni

    # Métodos de funcionalidad
    def pedir_libro_prestado(self, libro: Libro) -> None:
        """Solicita el préstamo de un libro"""
        # Verificar que no tenga ya este libro prestado
        for libro_prestado in self.__libros_prestados:
            if libro_prestado.get_isbn() == libro.get_isbn():
                raise ValueError("El usuario ya tiene este libro prestado.")

        if libro.prestar():
            self.__libros_prestados.append(libro)
            # Crear registro de préstamo
            prestamo = Prestamo(libro.get_titulo(), libro.get_isbn())
            self.__historial_prestamos.append(prestamo)
            return True
        return False

    def devolver_libro_prestado(self, libro: Libro) -> bool:
        """Devuelve un libro prestado"""
        if libro in self.__libros_prestados:
            libro.devolver()
            self.__libros_prestados.remove(libro)

            # Marcar préstamo como devuelto en el historial
            for prestamo in self.__historial_prestamos:
                if prestamo.get_libro_isbn() == libro.get_isbn() and prestamo.is_activo():
                    prestamo.marcar_devuelto()
                    break
            return True
        return False

    def ver_historial_prestamos(self) -> str:
        """Muestra el historial completo de préstamos del usuario"""
        if not self.__historial_prestamos:
            return "No hay historial de préstamos"

        historial = f"\nHistorial de Préstamos - {self.__nombre}:\n"
        historial += "=" * 60 + "\n"

        for i, prestamo in enumerate(self.__historial_prestamos, 1):
            historial += f"{i}. {prestamo}\n"
            historial += f"   Días prestado: {prestamo.dias_prestado()}\n\n"

        return historial

    def ver_libros_prestados(self) -> str:
        """Muestra los libros actualmente prestados"""
        if not self.__libros_prestados:
            return "No tienes libros prestados actualmente"

        libros = f"\nLibros Prestados - {self.__nombre}:\n"
        libros += "=" * 50 + "\n"

        for i, libro in enumerate(self.__libros_prestados, 1):
            # Buscar el préstamo activo correspondiente
            dias_prestado = 0
            for prestamo in self.__historial_prestamos:
                if prestamo.get_libro_isbn() == libro.get_isbn() and prestamo.is_activo():
                    dias_prestado = prestamo.dias_prestado()
                    break

            libros += f"{i}. {libro} - {dias_prestado} días\n"

        return libros

    def __str__(self) -> str:
        """Representación en cadena del usuario"""
        return f"{self.__nombre} (DNI: {self.__dni})"