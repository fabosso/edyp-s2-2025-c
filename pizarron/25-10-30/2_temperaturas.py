import typing

# Definimos un alias de tipo para claridad.
# Cada Medicion será una tupla inmutable de 3 floats.
TipoMedicion = typing.Tuple[float, float, float]


class RegistroSensor:
    def __init__(self):
        pass

    def agregar_medicion(self, temperatura: float, humedad: float, presion: float):
        pass

    def obtener_serie_temporal(self) -> typing.List[TipoMedicion]:
        pass

    def calcular_promedios(self) -> TipoMedicion:
        pass

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
