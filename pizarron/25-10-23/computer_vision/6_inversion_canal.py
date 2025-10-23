import cv2
import numpy as np
import time
from utils_imagen import cargar_imagen


def inversion_canal():
    """
    Operación 6: Inversión de canal con numpy
    Demuestra la velocidad de operaciones vectorizadas vs loops
    """

    # Cargar imagen usando función reutilizable
    imagen = cargar_imagen()
    alto, ancho = imagen.shape[:2]

    # cv2.split: separa los 3 canales de la imagen en 3 arrays numpy independientes
    azul, verde, rojo = cv2.split(imagen)

    print(f"\nTamaño de imagen: {imagen.shape}")
    print(f"Procesando {alto * ancho * 3:,} píxeles\n")

    # === Inversión con numpy (vectorizado) ===
    inicio = time.perf_counter()

    # OPERACIÓN VECTORIZADA: 255 - rojo
    # Numpy aplica la resta a CADA elemento del array simultáneamente
    # No hay loops explícitos, el operador '-' está sobrecargado para arrays
    rojo_invertido = 255 - rojo

    tiempo_numpy = time.perf_counter() - inicio
    print(f"Inversión con numpy: {tiempo_numpy*1000:.2f}ms")

    # === Inversión con loops (sobre subset) ===
    subconjunto = rojo[:100, :100].copy()
    inicio = time.perf_counter()

    # LOOP TRADICIONAL: procesa pixel por pixel secuencialmente
    for i in range(subconjunto.shape[0]):
        for j in range(subconjunto.shape[1]):
            subconjunto[i, j] = 255 - subconjunto[i, j]

    tiempo_loop = time.perf_counter() - inicio

    # Extrapolar a imagen completa
    ratio_pixeles = (alto * ancho) / (100 * 100)
    tiempo_loop_estimado = tiempo_loop * ratio_pixeles
    print(f"Inversión con loops (extrapolado): {tiempo_loop_estimado*1000:.2f}ms")
    print(f"Aceleración: {tiempo_loop_estimado/tiempo_numpy:.0f}x\n")

    # Mostrar resultados
    cv2.imshow("Rojo Invertido", cv2.merge([azul, verde, rojo_invertido]))

    print("Presiona cualquier tecla para continuar")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return {
        "tiempo_numpy": tiempo_numpy,
        "tiempo_loop": tiempo_loop_estimado,
        "aceleracion": tiempo_loop_estimado / tiempo_numpy,
    }


if __name__ == "__main__":
    metricas = inversion_canal()
    print(f"\nMétricas: {metricas}")
