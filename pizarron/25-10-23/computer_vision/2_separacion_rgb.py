import cv2
import numpy as np
from utils_imagen import cargar_imagen

def visualizar_canales():
    """
    Operación 2: Crear visualizaciones RGB
    Demuestra indexación avanzada para aislar canales individuales
    """
    
    # Cargar imagen usando función reutilizable
    imagen = cargar_imagen()
    
    print(f"\nTamaño de imagen: {imagen.shape}")
    print("Separando canales RGB...\n")
    
    # cv2.split: separa los 3 canales de la imagen en 3 arrays numpy independientes
    azul, verde, rojo = cv2.split(imagen)
    
    # np.zeros_like(imagen): crea un array de ceros con la misma forma y tipo que imagen
    # Esto genera una imagen negra (todos los píxeles en 0)
    solo_rojo = np.zeros_like(imagen)
    
    # INDEXACIÓN AVANZADA: solo_rojo[:, :, 2]
    # [:, :, 2] significa: todas las filas, todas las columnas, canal 2 (rojo en RGB)
    # Asignar 'rojo' a este slice copia todos los valores del canal rojo
    # Los canales 0 y 1 quedan en 0 (negro)
    solo_rojo[:, :, 2] = rojo
    
    # Solo canal verde (canal índice 1)
    solo_verde = np.zeros_like(imagen)
    solo_verde[:, :, 1] = verde
    
    # Solo canal azul (canal índice 0)
    solo_azul = np.zeros_like(imagen)
    solo_azul[:, :, 0] = azul
    
    # Mostrar resultados
    cv2.imshow('Canal Rojo', solo_rojo)
    cv2.imshow('Canal Verde', solo_verde)
    cv2.imshow('Canal Azul', solo_azul)
    
    print("Presiona cualquier tecla para continuar")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    visualizar_canales()