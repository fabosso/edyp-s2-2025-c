from datetime import datetime


class LlamadaCliente:
    """Representa una llamada de cliente (datos inmutables)"""

    def __init__(self, ticket, nombre_cliente, tipo_consulta, timestamp):
        # TODO: Implementar usando una estructura inmutable para estos datos
        # que no deberían cambiar una vez creada la llamada
        pass

    def __str__(self):
        return f"Ticket {self.ticket} - {self.nombre_cliente} ({self.tipo_consulta})"


class ReporteHorario:
    """Representa un reporte de estadísticas (datos inmutables una vez creado)"""

    def __init__(
        self,
        hora_inicio,
        hora_fin,
        llamadas_atendidas,
        tiempo_promedio_espera,
        operador_destacado,
    ):
        # TODO: Implementar usando una estructura que garantice
        # que estos datos no puedan ser modificados después de crear el reporte
        pass

    def __str__(self):
        return (
            f"Reporte {self.hora_inicio}-{self.hora_fin}: "
            f"{self.llamadas_atendidas} llamadas, "
            f"Promedio espera: {self.tiempo_promedio_espera}min, "
            f"Operador destacado: {self.operador_destacado}"
        )


class SistemaAtencionCliente:
    """Sistema de gestión de llamadas del centro de atención"""

    def __init__(self):
        # TODO: Inicializar estructura para mantener llamadas en orden de llegada
        # TODO: Inicializar estructura para almacenar reportes históricos
        pass

    def registrar_llamada(self, ticket, nombre_cliente, tipo_consulta):
        """
        Registra una nueva llamada entrante.
        La llamada debe entrar a una cola de espera para ser atendida
        en orden de llegada (primera en llegar, primera en ser atendida).

        Args:
            ticket (str): Número de ticket único
            nombre_cliente (str): Nombre del cliente
            tipo_consulta (str): Tipo de consulta (técnica, ventas, reclamo)
        """
        # TODO: Implementar
        # La estructura debe garantizar orden FIFO
        pass

    def atender_siguiente(self, operador):
        """
        Asigna la siguiente llamada en espera a un operador.
        Debe respetar estrictamente el orden de llegada.

        Args:
            operador (str): Nombre del operador que atenderá

        Returns:
            LlamadaCliente: La llamada asignada, o None si no hay llamadas
        """
        # TODO: Implementar
        # Debe quitar la llamada más antigua de la cola
        pass

    def ver_siguiente(self):
        """
        Consulta cuál es la próxima llamada sin quitarla de la cola.
        Útil para que los operadores sepan qué tipo de llamada viene.

        Returns:
            LlamadaCliente: La próxima llamada, o None si no hay llamadas
        """
        # TODO: Implementar
        pass

    def llamadas_en_espera(self):
        """
        Retorna la cantidad de llamadas esperando ser atendidas.

        Returns:
            int: Número de llamadas en cola
        """
        # TODO: Implementar
        pass

    def generar_reporte(
        self,
        hora_inicio,
        hora_fin,
        llamadas_atendidas,
        tiempo_promedio,
        operador_destacado,
    ):
        """
        Genera un reporte horario con estadísticas.
        Los datos del reporte no deben poder modificarse después de crearlo.

        Returns:
            ReporteHorario: El reporte generado
        """
        # TODO: Implementar
        # Usar estructura inmutable para los datos del reporte
        reporte = ReporteHorario(
            hora_inicio,
            hora_fin,
            llamadas_atendidas,
            tiempo_promedio,
            operador_destacado,
        )
        # TODO: Almacenar el reporte en el historial
        return reporte

    def obtener_reportes(self):
        """
        Retorna todos los reportes históricos generados.

        Returns:
            list: Lista de reportes
        """
        # TODO: Implementar
        pass


def caso_1():
    sistema = SistemaAtencionCliente()
    sistema.registrar_llamada("T001", "Juan Pérez", "técnica")
    sistema.registrar_llamada("T002", "María García", "ventas")
    sistema.registrar_llamada("T003", "Carlos López", "reclamo")

    print(sistema.llamadas_en_espera())  # Salida esperada: 3

    llamada1 = sistema.atender_siguiente("Operador1")
    print(llamada1.ticket)  # Salida esperada: T001
    print(llamada1.nombre_cliente)  # Salida esperada: Juan Pérez

    llamada2 = sistema.atender_siguiente("Operador2")
    print(llamada2.ticket)  # Salida esperada: T002

    print(sistema.llamadas_en_espera())  # Salida esperada: 1

def caso_2():
    sistema = SistemaAtencionCliente()
    sistema.registrar_llamada("T001", "Ana Ruiz", "consulta")
    sistema.registrar_llamada("T002", "Luis Mora", "técnica")

    proxima = sistema.ver_siguiente()
    print(proxima.ticket)  # Salida esperada: T001
    print(sistema.llamadas_en_espera())  # Salida esperada: 2 (no se quitó de la cola)

    atendida = sistema.atender_siguiente("Operador1")
    print(atendida.ticket)  # Salida esperada: T001
    print(sistema.llamadas_en_espera())  # Salida esperada: 1

def caso_3():
    sistema = SistemaAtencionCliente()

    # Generar reporte
    reporte1 = sistema.generar_reporte("09:00", "10:00", 25, 3.5, "Operador1")
    reporte2 = sistema.generar_reporte("10:00", "11:00", 30, 2.8, "Operador2")

    # Intentar modificar datos del reporte debería fallar o no tener efecto
    # (dependiendo de la implementación con tuplas)
    print(reporte1)  # Salida esperada: Reporte 09:00-10:00: 25 llamadas, Promedio espera: 3.5min, Operador destacado: Operador1

    reportes = sistema.obtener_reportes()
    print(len(reportes))  # Salida esperada: 2
    print(reportes[0].llamadas_atendidas)  # Salida esperada: 25

def caso_4():
    sistema = SistemaAtencionCliente()
    print(sistema.llamadas_en_espera())  # Salida esperada: 0
    llamada = sistema.atender_siguiente("Operador1")
    print(llamada)  # Salida esperada: None
    proxima = sistema.ver_siguiente()
    print(proxima)  # Salida esperada: None
