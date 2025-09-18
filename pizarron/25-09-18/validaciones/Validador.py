from typing import Any, Union


class ValidationError(Exception):
    """Excepción personalizada para errores de validación"""
    pass


class Validador:
    """
    Clase con métodos de clase para validaciones que retornan el valor válido
    o lanzan excepciones específicas
    """

    @classmethod
    def validar_cadena_no_vacia(cls, valor: str, nombre_campo: str = "Campo") -> str:
        """Valida que la cadena no esté vacía. Retorna la cadena limpia si es válida."""
        if not isinstance(valor, str):
            raise ValidationError(
                f"{nombre_campo} debe ser una cadena de texto")

        if not valor or valor.strip() == "":
            raise ValidationError(f"{nombre_campo} no puede estar vacío")

        return valor.strip()

    @classmethod
    def validar_entero(cls, valor: Any, nombre_campo: str = "Campo") -> int:
        """Valida que el valor sea un entero válido. Retorna el entero si es válido."""
        try:
            return int(valor)
        except (ValueError, TypeError):
            raise ValidationError(
                f"{nombre_campo} debe ser un número entero válido. Valor recibido: '{valor}'")

    @classmethod
    def validar_numero(cls, valor: Any, nombre_campo: str = "Campo") -> float:
        """Valida que el valor sea un número válido. Retorna el float si es válido."""
        try:
            return float(valor)
        except (ValueError, TypeError):
            raise ValidationError(
                f"{nombre_campo} debe ser un número válido. Valor recibido: '{valor}'")

    @classmethod
    def validar_longitud(cls, texto: str, min_len: int = 0, max_len: int = None,
                         nombre_campo: str = "Campo") -> str:
        """Valida la longitud del texto. Retorna el texto si es válido."""
        if not isinstance(texto, str):
            raise ValidationError(
                f"{nombre_campo} debe ser una cadena de texto")

        longitud = len(texto)

        if longitud < min_len:
            raise ValidationError(
                f"{nombre_campo} debe tener al menos {min_len} caracteres. Actual: {longitud}")

        if max_len is not None and longitud > max_len:
            raise ValidationError(
                f"{nombre_campo} debe tener máximo {max_len} caracteres. Actual: {longitud}")

        return texto

    @classmethod
    def validar_rango_numerico(cls, valor: Union[int, float, str], min_val: Union[int, float] = None,
                               max_val: Union[int, float] = None, nombre_campo: str = "Campo") -> float:
        """Valida que el número esté en el rango especificado. Retorna el número si es válido."""
        # Primero validar que sea un número
        numero = cls.validar_numero(valor, nombre_campo)

        if min_val is not None and numero < min_val:
            raise ValidationError(
                f"{nombre_campo} debe ser mayor o igual a {min_val}. Valor recibido: {numero}")

        if max_val is not None and numero > max_val:
            raise ValidationError(
                f"{nombre_campo} debe ser menor o igual a {max_val}. Valor recibido: {numero}")

        return numero

    @classmethod
    def validar_solo_letras(cls, texto: str, nombre_campo: str = "Campo") -> str:
        """Valida que el texto contenga solo letras. Retorna el texto si es válido."""
        if not isinstance(texto, str):
            raise ValidationError(
                f"{nombre_campo} debe ser una cadena de texto")

        if not texto.replace(' ', '').isalpha():
            raise ValidationError(
                f"{nombre_campo} debe contener solo letras y espacios. Valor recibido: '{texto}'")

        return texto.strip()

    @classmethod
    def validar_solo_numeros(cls, texto: str, nombre_campo: str = "Campo") -> str:
        """Valida que el texto contenga solo números. Retorna el texto si es válido."""
        if not isinstance(texto, str):
            raise ValidationError(
                f"{nombre_campo} debe ser una cadena de texto")

        if not texto.isdigit():
            raise ValidationError(
                f"{nombre_campo} debe contener solo dígitos. Valor recibido: '{texto}'")

        return texto

    @classmethod
    def validar_alfanumerico(cls, texto: str, nombre_campo: str = "Campo") -> str:
        """Valida que el texto sea alfanumérico. Retorna el texto si es válido."""
        if not isinstance(texto, str):
            raise ValidationError(
                f"{nombre_campo} debe ser una cadena de texto")

        if not texto.isalnum():
            raise ValidationError(
                f"{nombre_campo} debe ser alfanumérico (solo letras y números). Valor recibido: '{texto}'")

        return texto

    @classmethod
    def validar_entero_en_rango(cls, valor: Any, min_val: int = None, max_val: int = None,
                                nombre_campo: str = "Campo") -> int:
        """Valida que sea un entero en el rango especificado. Retorna el entero si es válido."""
        # Primero validar que sea entero
        entero = cls.validar_entero(valor, nombre_campo)

        if min_val is not None and entero < min_val:
            raise ValidationError(
                f"{nombre_campo} debe ser mayor o igual a {min_val}. Valor recibido: {entero}")

        if max_val is not None and entero > max_val:
            raise ValidationError(
                f"{nombre_campo} debe ser menor o igual a {max_val}. Valor recibido: {entero}")

        return entero
