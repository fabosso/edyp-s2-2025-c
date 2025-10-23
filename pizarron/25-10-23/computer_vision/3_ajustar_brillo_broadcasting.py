import cv2
import numpy as np
import time
from utils_imagen import cargar_imagen


def ajuste_brillo():
    """
    Operación 3: Ajuste de brillo usando broadcasting
    Demuestra cómo numpy transmite operaciones con escalares a arrays completos
    """

    # Cargar imagen usando función reutilizable
    imagen = cargar_imagen()

    print(f"\nTamaño de imagen: {imagen.shape}")

    factor_brillo = 1.3
    inicio = time.perf_counter()

    # BROADCASTING: imagen * factor_brillo
    # El escalar 1.3 se "transmite" automáticamente a cada elemento del array
    # Numpy expande conceptualmente 1.3 a un array del mismo tamaño que imagen
    # y luego multiplica elemento por elemento
    #
    # np.clip(array, min, max): limita valores al rango [min, max]
    # Evita que los píxeles excedan 255 o sean menores a 0
    #
    # .astype(np.uint8): convierte el resultado de float64 a uint8 (0-255)
    mas_brillante = np.clip(imagen * factor_brillo, 0, 255).astype(np.uint8)

    tiempo_broadcast = time.perf_counter() - inicio
    print(f"Ajuste de brillo (broadcasting): {tiempo_broadcast*1000:.2f}ms")
    print(f"Factor aplicado: {factor_brillo}\n")

    # Mostrar resultados
    cv2.imshow("Original", imagen)
    cv2.imshow("Mas brillante (1.3x)", mas_brillante)

    print("Presiona cualquier tecla para continuar")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return tiempo_broadcast


if __name__ == "__main__":
    tiempo = ajuste_brillo()
    print(f"\nTiempo de procesamiento: {tiempo*1000:.2f}ms")
