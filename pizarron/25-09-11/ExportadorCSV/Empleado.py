from Exportador import ExportadorObjetos


class Empleado:
    def __init__(self, id_empleado, nombre, cargo, departamento, fecha_ingreso):
        """
        Inicializa un nuevo empleado con los datos proporcionados.
        Args:
            id_empleado (str): Identificador único del empleado.
            nombre (str): Nombre completo del empleado.
            cargo (str): Cargo o puesto del empleado.
            departamento (str): Departamento al que pertenece el empleado.
            fecha_ingreso (str): Fecha de ingreso del empleado a la empresa.
        """
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.cargo = cargo
        self.departamento = departamento
        self.fecha_ingreso = fecha_ingreso
        self._salario = 50000  # Privado, no se exportará
        self.__evaluacion = "Confidencial"  # Muy privado, no se exportará

    def obtener_info_publica(self):
        """
        Devuelve información pública del empleado.
        Returns:
            str: Cadena con el nombre y cargo del empleado.
        """
        return f"{self.nombre} - {self.cargo}"


class RegistroEmpleados:
    def __init__(self, empresa):
        """
        Inicializa un registro de empleados para una empresa.
        Args:
            empresa (str): Nombre de la empresa.
        """
        self.empresa = empresa
        self._empleados = []

    def contratar(self, empleado):
        """
        Agrega un empleado al registro de empleados.
        Args:
            empleado (Empleado): Instancia de la clase Empleado a agregar.
        """
        self._empleados.append(empleado)

    def get_empleados(self):
        """
        Devuelve la lista de empleados registrados.
        Returns:
            list: Lista de instancias de Empleado.
        """
        return self._empleados


class ExportadorEmpleados(ExportadorObjetos):
    """Exportador específico para registros de empleados"""

    def _obtener_objetos(self, registro):
        """
        Obtiene la lista de empleados de un registro.
        Args:
            registro (RegistroEmpleados): Registro de empleados.
        Returns:
            list: Lista de empleados.
        """
        return registro.get_empleados()

    def _extraer_atributos(self, objeto):
        """
        Extrae los atributos públicos del objeto empleado, excluyendo información sensible.
        Args:
            objeto (Empleado): Objeto del cual se extraen los atributos.
        Returns:
            list: Lista de nombres de atributos públicos no sensibles.
        """
        atributos = super()._extraer_atributos(objeto)
        atributos_filtrados = list(
            filter(lambda atr: atr not in ['salario_confidencial', 'numero_seguro_social'], atributos))
        return atributos_filtrados


def main():
    """
    Ejemplo de uso: crea un registro de empleados, contrata empleados y exporta los datos a un archivo CSV.
    """
    print("\n=== EJEMPLO 2: Registro de Empleados ===")
    registro = RegistroEmpleados("Tech Corp")
    registro.contratar(Empleado("E001", "Ana García",
                                "Desarrolladora Senior", "IT", "2023-01-15"))
    registro.contratar(Empleado("E002", "Carlos López",
                                "Diseñador UX", "Diseño", "2023-03-20"))
    registro.contratar(Empleado("E003", "María Rodríguez",
                                "Project Manager", "PMO", "2022-11-10"))

    exportador_empleados = ExportadorEmpleados("empleados.csv")
    exportador_empleados.exportar(registro)


if __name__ == "__main__":
    main()
