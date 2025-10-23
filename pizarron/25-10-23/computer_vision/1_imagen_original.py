import cv2
from utils_imagen import cargar_imagen


def mostrar_imagen():
    """
    Operación 1: Carga y muestra la imagen
    """

    # Cargar imagen usando función reutilizable
    imagen = cargar_imagen()

    # Obtener información de la imagen
    alto, ancho = imagen.shape[:2]
    canales = imagen.shape[2] if len(imagen.shape) == 3 else 1
    tipo_datos = imagen.dtype

    # Imprimir información detallada
    print("\n" + "=" * 50)
    print("INFORMACIÓN DE LA IMAGEN")
    print("=" * 50)
    print(f"Dimensiones (shape):     {imagen.shape}")
    print(f"Alto (filas):            {alto} píxeles")
    print(f"Ancho (columnas):        {ancho} píxeles")
    print(
        f"Canales (colores):       {canales} (RGB)"
        if canales == 3
        else f"Canales: {canales}"
    )
    print(f"Total de píxeles:        {alto * ancho:,}")
    print(f"Total de valores:        {alto * ancho * canales:,}")
    print(f"Tipo de datos:           {tipo_datos}")
    print("Rango de valores:        0-255")
    print(
        f"Tamaño en memoria:       {imagen.nbytes:,} bytes ({imagen.nbytes / (1024**2):.2f} MB)"
    )
    print("=" * 50 + "\n")

    # Mostrar resultados
    cv2.imshow("Original", imagen)

    print("Presiona cualquier tecla para continuar")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    mostrar_imagen()
