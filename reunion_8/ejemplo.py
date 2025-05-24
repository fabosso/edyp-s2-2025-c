import time
# Lista grande
lista_grande = list(range(1000000))
set_grande = set(range(1000000))
# Buscar el último elemento
elemento = 999999
# En lista: O(n) - debe recorrer hasta encontrarlo
inicio = time.time()
elemento in lista_grande
tiempo_lista = time.time() - inicio
# En set: O(1) - va directo a la posición
inicio = time.time()
elemento in set_grande
tiempo_set = time.time() - inicio
print(f"Lista: {tiempo_lista:.6f} segundos")
print(f"Set: {tiempo_set:.6f} segundos")
print(f"El set es {tiempo_lista/tiempo_set:.0f}x más rápido")