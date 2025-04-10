import time
import random

# Crear un array de números aleatorios
numeros = [random.randint(0, 100) for _ in range(100000)]

# Usando while
tiempo_inicio = time.time()
resultado_while = []
i = 0
while i < len(numeros):
    resultado_while.append(numeros[i] * numeros[i])
    i += 1
tiempo_while = time.time() - tiempo_inicio

# Usando for
tiempo_inicio = time.time()
resultado_for = []
for num in numeros:
    resultado_for.append(num * num)
tiempo_for = time.time() - tiempo_inicio

# Usando map
tiempo_inicio = time.time()
resultado_map = list(map(lambda x: x * x, numeros))
tiempo_map = time.time() - tiempo_inicio

# Mostrar resultados
print(f"Tiempo usando while: {tiempo_while:.6f} segundos")
print(f"Tiempo usando for: {tiempo_for:.6f} segundos")
print(f"Tiempo usando map: {tiempo_map:.6f} segundos")

# Determinar el método más rápido
tiempos = {"while": tiempo_while, "for": tiempo_for, "map": tiempo_map}
mas_rapido = min(tiempos, key=tiempos.get)
print(f"\nEl método más rápido es: {mas_rapido}")

# Ejemplo de respuesta
"""
Tiempo usando while: 0.125759 segundos
Tiempo usando for: 0.038795 segundos
Tiempo usando map: 0.029658 segundos

El método más rápido es: map
"""
