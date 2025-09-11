class Libro:
    """Clase que representa un libro en la biblioteca"""

    def __init__(self, titulo: str, autor: str, isbn: str, editorial: str):
        """Constructor de la clase Libro"""
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__editorial = editorial
        self.__disponible = True

    # Métodos getter
    def get_titulo(self) -> str:
        """Obtiene el título del libro"""
        return self.__titulo

    def get_autor(self) -> str:
        """Obtiene el autor del libro"""
        return self.__autor

    def get_isbn(self) -> str:
        """Obtiene el ISBN del libro"""
        return self.__isbn

    def get_editorial(self) -> str:
        """Obtiene la editorial del libro"""
        return self.__editorial

    def get_disponible(self) -> bool:
        """Obtiene la disponibilidad del libro"""
        return self.__disponible

    # Métodos setter
    def set_titulo(self, titulo: str) -> None:
        """Establece el título del libro"""
        self.__titulo = titulo

    def set_autor(self, autor: str) -> None:
        """Establece el autor del libro"""
        self.__autor = autor

    def set_isbn(self, isbn: str) -> None:
        """Establece el ISBN del libro"""
        self.__isbn = isbn

    def set_editorial(self, editorial: str) -> None:
        """Establece la editorial del libro"""
        self.__editorial = editorial

    # Métodos de funcionalidad
    def prestar(self) -> None:
        """Presta el libro si está disponible"""
        if not self.__disponible:
            raise ValueError("El libro no está disponible para préstamo.")

        self.__disponible = False

    def devolver(self) -> None:
        """Devuelve el libro prestado"""
        if self.__disponible:
            raise ValueError("El libro ya está disponible en la biblioteca.")

        self.__disponible = True

    def ver_informacion_libro(self) -> str:
        """Muestra la información completa del libro"""
        if self.__disponible:
            estado = "Disponible"
        else:
            estado = "Prestado"

        return f"""
        Título: {self.__titulo}
        Autor: {self.__autor}
        ISBN: {self.__isbn}
        Editorial: {self.__editorial}
        Estado: {estado}
        """

    def __str__(self) -> str:
        """Representación en cadena del libro"""
        return f"{self.__titulo} - {self.__autor} (ISBN: {self.__isbn})"
