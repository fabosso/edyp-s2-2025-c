import cv2
import numpy as np

def cargar_imagen(ruta='imagen.jpg', alto=1920, ancho=1080):
    """
    Carga una imagen desde un archivo o genera una aleatoria si no existe.
    
    Parámetros:
        ruta (str): Ruta del archivo de imagen
        alto (int): Alto de la imagen generada si no existe el archivo
        ancho (int): Ancho de la imagen generada si no existe el archivo
    
    Retorna:
        numpy.ndarray: Imagen cargada o generada
    """
    imagen = cv2.imread(ruta)
    if imagen is None:
        # np.random.randint: Genera array de enteros aleatorios
        # Parámetros: (min, max, shape, dtype)
        # shape=(alto, ancho, 3) crea una imagen con 3 canales (RGB)
        print(f"No se encontró '{ruta}', generando imagen aleatoria de {alto}x{ancho}")
        imagen = np.random.randint(0, 255, (alto, ancho, 3), dtype=np.uint8)
    else:
        print(f"Imagen cargada: {ruta}")
    
    return imagen