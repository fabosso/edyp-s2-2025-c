import typing

# Definimos un alias de tipo para claridad.
# Cada Medicion será una tupla inmutable de 3 floats.
TipoMedicion = typing.Tuple[float, float, float]


class RegistroSensor:
    """
    Gestiona el almacenamiento y procesamiento de mediciones ambientales.

    Utiliza una lista para almacenar la secuencia de mediciones (Req 2)
    y tuplas para garantizar que cada medición individual sea inmutable (Req 1).
    """

    def __init__(self):
        """
        Inicializa el registro.

        'self.mediciones' es la lista que mantiene el orden temporal.
        """
        # Esta lista almacenará las tuplas de medición
        self.mediciones: typing.List[TipoMedicion] = []

    def agregar_medicion(self, temperatura: float, humedad: float, presion: float):
        """
        Guarda una nueva medición como una tupla inmutable en el registro.
        (Cumple con el Requisito 1)
        """
        # 1. Creamos la tupla. Una vez creada, sus valores (temp, hum, pres)
        #    no pueden ser modificados individualmente.
        medicion_inmutable: TipoMedicion = (temperatura, humedad, presion)

        # 2. Añadimos la tupla inmutable a nuestra lista secuencial.
        self.mediciones.append(medicion_inmutable)
        print(f"[Registro] Medición agregada: {medicion_inmutable}")

    def obtener_serie_temporal(self) -> typing.List[TipoMedicion]:
        """
        Retorna la secuencia completa de mediciones en el orden en que
        fueron agregadas.
        (Cumple con el Requisito 2)
        """
        # Retornamos una copia de la lista para evitar que
        # el consumidor modifique el orden del registro original (aunque no es estrictamente
        # necesario para este ejercicio, es buena práctica).
        return self.mediciones.copy()

    def calcular_promedios(self) -> TipoMedicion:
        """
        Calcula los valores promedio para temperatura, humedad y presión
        sobre todas las mediciones almacenadas.
        (Cumple con el Requisito 3)
        """
        if not self.mediciones:
            # Manejo del caso borde: si no hay mediciones, los promedios son 0.
            return (0.0, 0.0, 0.0)

        # Inicializamos los totales
        total_temp = 0.0
        total_hum = 0.0
        total_pres = 0.0

        # Iteramos sobre la lista de tuplas
        # (temp, hum, pres) desempaqueta la tupla en cada iteración
        for temp, hum, pres in self.mediciones:
            total_temp += temp
            total_hum += hum
            total_pres += pres

        # Calculamos el promedio
        n = len(self.mediciones)
        promedio_temp = total_temp / n
        promedio_hum = total_hum / n
        promedio_pres = total_pres / n

        # Retornamos los promedios también como una tupla
        return (promedio_temp, promedio_hum, promedio_pres)
    

def caso_1():
    mi_sensor = RegistroSensor()

    print("\n--- Agregando Mediciones (Test Case 1) ---")
    mi_sensor.agregar_medicion(22.5, 55.0, 101.3)
    mi_sensor.agregar_medicion(23.0, 54.2, 101.1)
    mi_sensor.agregar_medicion(22.1, 55.8, 101.5)

    print("\n--- Obteniendo Serie Temporal (Test Case 1) ---")
    serie = mi_sensor.obtener_serie_temporal()
    for i, medicion in enumerate(serie):
        print(f"  Medición {i+1}: {medicion}")

def caso_2():
    print("--- Inicializando el Registro del Sensor ---")
    mi_sensor = RegistroSensor()

    mi_sensor.agregar_medicion(22.5, 55.0, 101.3)
    mi_sensor.agregar_medicion(23.0, 54.2, 101.1)
    mi_sensor.agregar_medicion(22.1, 55.8, 101.5)

    print("\n--- Calculando Promedios (Test Case 2) ---")
    promedios = mi_sensor.calcular_promedios()
    print(f"Promedios (Temp, Hum, Pres): {promedios}")

    # Verificación manual (22.5+23.0+22.1)/3 = 22.533 | (55.0+54.2+55.8)/3 = 55.0 | (101.3+101.1+101.5)/3 = 101.3
    print(f"Promedio Temp (Esperado): {(22.5+23.0+22.1)/3:.3f}")
    print(f"Promedio Hum (Esperado):  {(55.0+54.2+55.8)/3:.3f}")
    print(f"Promedio Pres (Esperado): {(101.3+101.1+101.5)/3:.3f}")

def caso_3():
    print("--- Inicializando el Registro del Sensor ---")
    mi_sensor = RegistroSensor()

    mi_sensor.agregar_medicion(22.5, 55.0, 101.3)
    mi_sensor.agregar_medicion(23.0, 54.2, 101.1)
    mi_sensor.agregar_medicion(22.1, 55.8, 101.5)

    print("\n--- Validando Inmutabilidad (Test Case 3) ---")

    try:
        # 1. Obtenemos la primera medición (que es una tupla)
        primera_medicion = mi_sensor.obtener_serie_temporal()[0]
        print(
            f"Intentando modificar la temperatura de la primera medición: {primera_medicion}"
        )

        # 2. Intentamos cambiar el valor de temperatura (índice 0)
        # ESTO DEBE FALLAR porque las tuplas son inmutables.
        primera_medicion[0] = 30.0

    except TypeError as e:
        print("¡ÉXITO! La modificación falló como se esperaba.")
        print(f"Error capturado: {e}")
    except IndexError:
        print("Error: No hay mediciones para probar.")

    print("\n--- Pruebas Finalizadas ---")
