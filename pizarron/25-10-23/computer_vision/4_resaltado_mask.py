import cv2
import numpy as np
import time
from utils_imagen import cargar_imagen


def mascara_booleana():
    """
    Operación 4: Máscara booleana - aislar píxeles brillantes
    Demuestra indexación booleana y operaciones condicionales vectorizadas
    """

    # Cargar imagen usando función reutilizable
    imagen = cargar_imagen()

    print(f"\nTamaño de imagen: {imagen.shape}")
    print("Aplicando máscara booleana para aislar píxeles brillantes...\n")

    inicio = time.perf_counter()

    # COMPARACIÓN VECTORIZADA: imagen > 200
    # Retorna un array booleano de la misma forma que imagen
    # True donde el píxel es > 200, False en caso contrario
    #
    # .all(axis=2): verifica si TODOS los canales son True a lo largo del axis 2 (canales)
    # axis=2 reduce las dimensiones de (alto, ancho, 3) a (alto, ancho)
    # Resultado: array 2D booleano donde True indica que R, G y B son todos > 200
    mascara_brillante = (imagen > 200).all(axis=2)

    resaltado = imagen.copy()

    # INDEXACIÓN BOOLEANA: resaltado[~mascara_brillante]
    # ~ es el operador NOT bit a bit, invierte la máscara booleana
    # Esta indexación selecciona SOLO los píxeles donde mascara_brillante es False
    # Luego aplica // 3 (división entera) solo a esos píxeles
    # Es como un "if" vectorizado sin escribir loops
    resaltado[~mascara_brillante] = resaltado[~mascara_brillante] // 3

    tiempo_mascara = time.perf_counter() - inicio
    print(f"Operación con máscara booleana: {tiempo_mascara*1000:.2f}ms")

    # Contar píxeles brillantes
    num_brillantes = np.sum(mascara_brillante)
    total_pixeles = mascara_brillante.size
    porcentaje = (num_brillantes / total_pixeles) * 100
    print(f"Píxeles brillantes (RGB > 200): {num_brillantes:,} ({porcentaje:.2f}%)\n")

    # Crear visualización de la máscara
    # Convertir booleano a imagen (True=255, False=0)
    visualizacion_mascara = (mascara_brillante * 255).astype(np.uint8)

    # Mostrar resultados
    cv2.imshow("Original", imagen)
    cv2.imshow("Mascara (blanco=brillante)", visualizacion_mascara)
    cv2.imshow("Areas brillantes resaltadas", resaltado)

    print("Presiona cualquier tecla para continuar")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return tiempo_mascara


if __name__ == "__main__":
    tiempo = mascara_booleana()
    print(f"\nTiempo de procesamiento: {tiempo*1000:.2f}ms")
