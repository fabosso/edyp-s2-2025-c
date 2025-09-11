import csv

class Exportador:
    """Clase base para todos los exportadores"""

    def __init__(self, nombre_archivo):
        """
        Inicializa el exportador con el nombre del archivo de salida.
        Args:
            nombre_archivo (str): Nombre del archivo donde se exportarán los datos.
        """
        self.nombre_archivo = nombre_archivo

    def exportar(self, datos):
        """
        Método base para exportar datos. Debe ser implementado por las subclases.
        Args:
            datos: Datos a exportar.
        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        raise NotImplementedError(
            "Las subclases deben implementar el método exportar()")

    def _escribir_csv(self, lista_datos):
        """
        Escribe una lista de listas en un archivo CSV.
        Args:
            lista_datos (list): Lista de listas con los datos a exportar.
        Raises:
            IOError: Si ocurre un error al escribir el archivo.
        """
        try:
            with open(self.nombre_archivo, "w", newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(lista_datos)
        except IOError:
            print(f"Error al exportar archivo: {self.nombre_archivo}")
            raise IOError

class ExportadorSimple(Exportador):
    """Exportador para datos que ya están en formato lista de listas"""

    def exportar(self, lista_datos):
        """
        Exporta una lista de listas a un archivo CSV.
        Args:
            lista_datos (list): Lista de listas con los datos a exportar.
        """
        if not lista_datos:
            print("No hay datos para exportar")
            return

        self._escribir_csv(lista_datos)
        print(f"Datos exportados exitosamente a {self.nombre_archivo}")

class ExportadorObjetos(Exportador):
    """Clase base para exportadores que trabajan con colecciones de objetos"""

    def __init__(self, nombre_archivo):
        """
        Inicializa el exportador de objetos con el nombre del archivo de salida.
        Args:
            nombre_archivo (str): Nombre del archivo donde se exportarán los datos.
        """
        super().__init__(nombre_archivo)

    def _extraer_atributos(self, objeto):
        """
        Extrae los atributos públicos de un objeto.
        Args:
            objeto: Objeto del cual se extraerán los atributos.
        Returns:
            list: Lista de nombres de atributos públicos.
        """
        atributos = []
        for atributo in dir(objeto):
            if not callable(getattr(objeto, atributo)) and not atributo.startswith("_"):
                atributos.append(atributo)
        return atributos

    def _extraer_valores(self, objeto, atributos):
        """
        Extrae los valores de los atributos especificados de un objeto.
        Args:
            objeto: Objeto del cual se extraerán los valores.
            atributos (list): Lista de nombres de atributos a extraer.
        Returns:
            list: Lista de valores correspondientes a los atributos.
        """
        valores = []
        for atributo in atributos:
            valores.append(getattr(objeto, atributo))
        return valores

    def exportar(self, coleccion):
        """
        Exporta una colección de objetos a un archivo CSV.
        Args:
            coleccion: Colección de objetos a exportar.
        """
        objetos = self._obtener_objetos(coleccion)

        if not objetos:
            print("No hay objetos para exportar")
            return

        datos = []
        atributos_header = self._extraer_atributos(objetos[0])

        # Agregar encabezado
        datos.append(atributos_header)

        # Agregar datos de cada objeto
        for objeto in objetos:
            valores = self._extraer_valores(objeto, atributos_header)
            datos.append(valores)

        self._escribir_csv(datos)
        print(
            f"{self.__class__.__name__}: Exportados {len(objetos)} registros a {self.nombre_archivo}")

    def _obtener_objetos(self, coleccion):
        """
        Método para obtener la lista de objetos de la colección.
        Args:
            coleccion: Colección de la cual se obtendrán los objetos.
        Returns:
            list: Lista de objetos extraídos de la colección.
        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        raise NotImplementedError(
            "Las subclases deben implementar _obtener_objetos()")
