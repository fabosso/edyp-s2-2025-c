"""
Clase Prestamo para el Sistema de Gestión de Biblioteca
Representa un préstamo de libro con fechas y estado
"""

from datetime import datetime
from typing import Optional


class Prestamo:
    """Clase que representa un préstamo de libro"""

    def __init__(self, libro_titulo: str, libro_isbn: str):
        """Constructor de la clase Prestamo"""
        self.__libro_titulo = libro_titulo
        self.__libro_isbn = libro_isbn
        self.__fecha_prestamo = datetime.now()
        self.__fecha_devolucion = None
        self.__activo = True

    # Métodos getter
    def get_libro_titulo(self) -> str:
        """Obtiene el título del libro prestado"""
        return self.__libro_titulo

    def get_libro_isbn(self) -> str:
        """Obtiene el ISBN del libro prestado"""
        return self.__libro_isbn

    def get_fecha_prestamo(self) -> datetime:
        """Obtiene la fecha de préstamo"""
        return self.__fecha_prestamo

    def get_fecha_devolucion(self) -> Optional[datetime]:
        """Obtiene la fecha de devolución (None si no se ha devuelto)"""
        return self.__fecha_devolucion

    def is_activo(self) -> bool:
        """Verifica si el préstamo está activo (no devuelto)"""
        return self.__activo

    # Métodos de funcionalidad
    def marcar_devuelto(self) -> bool:
        """Marca el préstamo como devuelto"""
        if self.__activo:
            self.__fecha_devolucion = datetime.now()
            self.__activo = False
            return True
        return False

    def dias_prestado(self) -> int:
        """Calcula los días que ha estado prestado el libro"""
        if self.__activo:
            return (datetime.now() - self.__fecha_prestamo).days
        else:
            return (self.__fecha_devolucion - self.__fecha_prestamo).days

    def get_info_prestamo(self) -> str:
        """Obtiene información completa del préstamo"""
        fecha_prestamo = self.__fecha_prestamo.strftime("%d/%m/%Y %H:%M")

        if self.__activo:
            estado = "ACTIVO"
            fecha_devolucion = "No devuelto"
            dias = self.dias_prestado()
        else:
            estado = "DEVUELTO"
            fecha_devolucion = self.__fecha_devolucion.strftime("%d/%m/%Y %H:%M")
            dias = self.dias_prestado()

        return f"""
        Libro: {self.__libro_titulo} (ISBN: {self.__libro_isbn})
        Fecha préstamo: {fecha_prestamo}
        Fecha devolución: {fecha_devolucion}
        Estado: {estado}
        Días prestado: {dias}
        """

    def __str__(self) -> str:
        """Representación en cadena del préstamo"""
        estado = "ACTIVO" if self.__activo else "DEVUELTO"
        fecha_prestamo = self.__fecha_prestamo.strftime("%d/%m/%Y")
        return f"{self.__libro_titulo} - {fecha_prestamo} ({estado})"