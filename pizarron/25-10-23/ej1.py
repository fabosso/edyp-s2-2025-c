# =============================================================================
# 1. Crear una matriz 5x5 con valores aleatorios y:
#    - Encontrar el elemento máximo y su posición
#    - Calcular la suma de cada fila
#    - Normalizar la matriz (media=0, std=1)
# =============================================================================

import numpy as np

# Crear matriz 5x5 con valores aleatorios entre 0 y 100
np.random.seed(42)  # Para reproducibilidad
matriz = np.random.randint(0, 101, (5, 5))

print("Matriz original:")
print(matriz)

# Encontrar elemento máximo y su posición
max_valor = np.max(matriz)
max_pos = np.unravel_index(np.argmax(matriz), matriz.shape)

print(f"\nElemento máximo: {max_valor}")
print(f"Posición (fila, columna): {max_pos}")
print(f"Verificación: matriz[{max_pos[0]}, {max_pos[1]}] = {matriz[max_pos]}")

# Suma de cada fila
suma_filas = np.sum(matriz, axis=1)
print(f"\nSuma por filas: {suma_filas}")

# Verificación manual de la primera fila
print(f"Verificación fila 0: {matriz[0, :]} -> suma = {np.sum(matriz[0, :])}")

# Normalizar matriz (media=0, std=1)
media_original = np.mean(matriz)
std_original = np.std(matriz)

matriz_normalizada = (matriz - media_original) / std_original

print("\nEstadísticas originales:")
print(f"Media: {media_original:.3f}, Std: {std_original:.3f}")

print("\nEstadísticas normalizadas:")
print(f"Media: {np.mean(matriz_normalizada):.10f}")  # Debería ser ~0
print(f"Std: {np.std(matriz_normalizada):.10f}")  # Debería ser ~1

print("\nMatriz normalizada:")
print(matriz_normalizada)
