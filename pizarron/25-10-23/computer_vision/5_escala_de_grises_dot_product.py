import cv2
import numpy as np
import time
from utils_imagen import cargar_imagen

def escala_grises_ponderada():
    """
    Operación 5: Combinación ponderada de canales
    Demuestra el uso de producto punto para crear escala de grises personalizada
    """
    
    # Cargar imagen usando función reutilizable
    imagen = cargar_imagen()
    
    print(f"\nTamaño de imagen: {imagen.shape}")
    print("Convirtiendo a escala de grises con pesos personalizados...\n")
    
    inicio = time.perf_counter()
    
    # np.array: crea un array numpy desde una lista Python
    # Estos pesos corresponden a la percepción humana de luminosidad
    pesos = np.array([0.114, 0.587, 0.299])  # Pesos BGR para luminosidad
    
    # np.dot(imagen, pesos): PRODUCTO PUNTO vectorizado
    # Para cada píxel (B, G, R), calcula: B*0.114 + G*0.587 + R*0.299
    # Es equivalente a un loop que multiplica y suma, pero mucho más rápido
    # Resultado: array 2D (alto, ancho) con valores de escala de grises
    escala_grises = np.dot(imagen, pesos).astype(np.uint8)
    
    tiempo_dot = time.perf_counter() - inicio
    print(f"Escala de grises ponderada (producto punto): {tiempo_dot*1000:.2f}ms")
    print(f"Pesos aplicados (RGB): {pesos}\n")
    
    # Comparación con método de OpenCV
    inicio = time.perf_counter()
    grises_cv2 = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    tiempo_cv2 = time.perf_counter() - inicio
    print(f"cv2.cvtColor (método estándar): {tiempo_cv2*1000:.2f}ms\n")
    
    # Mostrar resultados
    cv2.imshow('Original', imagen)
    cv2.imshow('Escala de Grises Personalizada (np.dot)', escala_grises)
    cv2.imshow('Escala de Grises OpenCV (cvtColor)', grises_cv2)
    
    print("Presiona cualquier tecla para continuar")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return {
        'tiempo_numpy': tiempo_dot,
        'tiempo_opencv': tiempo_cv2
    }

if __name__ == "__main__":
    tiempos = escala_grises_ponderada()
    print(f"\nMétricas: {tiempos}")