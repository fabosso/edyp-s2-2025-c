# NumPy Fundamentos para Ingeniería
# Notebook educativo - Conceptos básicos y aplicaciones prácticas

import numpy as np
import matplotlib.pyplot as plt

print("NumPy version:", np.__version__)

# =============================================================================
# 1. CREACIÓN DE ARRAYS - FUNDAMENTOS
# =============================================================================

print("\n" + "=" * 50)
print("1. CREACIÓN DE ARRAYS")
print("=" * 50)

# Arrays básicos
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Array 1D:", arr_1d)
print("Array 2D:\n", arr_2d)
print("Array 3D shape:", arr_3d.shape)

# Funciones de creación útiles
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))
identity = np.eye(3)
random_vals = np.random.random((2, 3))

print("\nZeros 3x4:\n", zeros)
print("\nIdentidad 3x3:\n", identity)

# Rangos y secuencias
range_arr = np.arange(0, 10, 2)  # inicio, fin, paso
linspace_arr = np.linspace(0, 1, 5)  # inicio, fin, cantidad

print("\nArange:", range_arr)
print("Linspace:", linspace_arr)

# =============================================================================
# 2. PROPIEDADES FUNDAMENTALES
# =============================================================================

print("\n" + "=" * 50)
print("2. PROPIEDADES DE ARRAYS")
print("=" * 50)

data = np.random.randint(0, 100, (4, 5))
print("Array ejemplo:\n", data)
print(f"Shape: {data.shape}")
print(f"Dimensiones: {data.ndim}")
print(f"Tamaño total: {data.size}")
print(f"Tipo de datos: {data.dtype}")
print(f"Bytes por elemento: {data.itemsize}")

# =============================================================================
# 3. INDEXING Y SLICING
# =============================================================================

print("\n" + "=" * 50)
print("3. INDEXING Y SLICING")
print("=" * 50)

arr = np.arange(20).reshape(4, 5)
print("Array base:\n", arr)

# Indexing básico
print("\nElemento [1,2]:", arr[1, 2])
print("Primera fila:", arr[0, :])
print("Segunda columna:", arr[:, 1])

# Slicing avanzado
print("\nPrimeras 2 filas, columnas 1-3:\n", arr[:2, 1:4])
print("Cada segunda fila:\n", arr[::2, :])

# Boolean indexing
mask = arr > 10
print("\nElementos > 10:", arr[mask])

# Fancy indexing
indices = [0, 2, 3]
print("Filas seleccionadas [0,2,3]:\n", arr[indices, :])

# =============================================================================
# 4. OPERACIONES MATEMÁTICAS
# =============================================================================

print("\n" + "=" * 50)
print("4. OPERACIONES MATEMÁTICAS")
print("=" * 50)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("a =", a)
print("b =", b)

# Operaciones elemento a elemento
print("\nSuma:", a + b)
print("Multiplicación:", a * b)
print("Potencia:", a**2)

# Operaciones matriciales
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("\nMatriz A:\n", matrix_a)
print("Matriz B:\n", matrix_b)
print("Producto matricial A @ B:\n", matrix_a @ matrix_b)

# Funciones matemáticas universales
x = np.linspace(0, 2 * np.pi, 10)
print("\nSeno de x:", np.sin(x))
print("Exponencial:", np.exp([1, 2, 3]))

# =============================================================================
# 5. ESTADÍSTICAS Y AGREGACIONES
# =============================================================================

print("\n" + "=" * 50)
print("5. ESTADÍSTICAS Y AGREGACIONES")
print("=" * 50)

data = np.random.normal(50, 15, (100,))  # media=50, std=15

print(f"Media: {np.mean(data):.2f}")
print(f"Mediana: {np.median(data):.2f}")
print(f"Desviación estándar: {np.std(data):.2f}")
print(f"Mínimo: {np.min(data):.2f}")
print(f"Máximo: {np.max(data):.2f}")

# Agregaciones por eje
matrix = np.random.randint(1, 10, (3, 4))
print("\nMatriz:\n", matrix)
print("Suma por filas (axis=1):", np.sum(matrix, axis=1))
print("Media por columnas (axis=0):", np.mean(matrix, axis=0))

# =============================================================================
# 6. RESHAPE Y MANIPULACIÓN DE FORMA
# =============================================================================

print("\n" + "=" * 50)
print("6. MANIPULACIÓN DE FORMA")
print("=" * 50)

original = np.arange(12)
print("Original:", original)

# Reshape
reshaped = original.reshape(3, 4)
print("Reshape 3x4:\n", reshaped)

# Flatten
flattened = reshaped.flatten()
print("Flatten:", flattened)

# Transpose
transposed = reshaped.T
print("Transpuesta:\n", transposed)

# Concatenación
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

concat_v = np.vstack([arr1, arr2])  # vertical
concat_h = np.hstack([arr1, arr2])  # horizontal

print("\nConcatenación vertical:\n", concat_v)
print("Concatenación horizontal:\n", concat_h)

# =============================================================================
# 7. BROADCASTING
# =============================================================================

print("\n" + "=" * 50)
print("7. BROADCASTING")
print("=" * 50)

# Broadcasting básico
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10

print("Array original:\n", arr)
print("Array + 10:\n", arr + scalar)

# Broadcasting con arrays
row_vector = np.array([1, 2, 3])
col_vector = np.array([[10], [20]])

print("\nRow vector:", row_vector)
print("Col vector:\n", col_vector)
print("Broadcasting sum:\n", row_vector + col_vector)


# =============================================================================
# 8. EJEMPLO PRÁCTICO: ÁLGEBRA LINEAL
# =============================================================================

print("\n" + "=" * 50)
print("8. EJEMPLO PRÁCTICO: ÁLGEBRA LINEAL")
print("=" * 50)

# Sistema de ecuaciones: Ax = b
# 2x + 3y = 7
# x - y = 1

A = np.array([[2, 3], [1, -1]])
b = np.array([7, 1])

print("Matriz A:\n", A)
print("Vector b:", b)

# Solución usando inversión
x = np.linalg.solve(A, b)
print("Solución x:", x)

# Verificación
# @ es el operador de producto matricial en NumPy
verification = A @ x
print("Verificación A@x:", verification)
print("¿Es igual a b?", np.allclose(verification, b))

# =============================================================================
# 10. TIPS Y MEJORES PRÁCTICAS
# =============================================================================

print("\n" + "=" * 50)
print("10. TIPS Y MEJORES PRÁCTICAS")
print("=" * 50)

# Comparación de performance
import time

# Lista de Python vs NumPy array
python_list = list(range(1000000))
numpy_array = np.arange(1000000)

# Suma con listas
start = time.time()
sum_list = sum(python_list)
time_list = time.time() - start

# Suma con NumPy
start = time.time()
sum_numpy = np.sum(numpy_array)
time_numpy = time.time() - start

print(f"Suma con listas Python: {time_list:.4f} segundos")
print(f"Suma con NumPy: {time_numpy:.4f} segundos")
print(f"NumPy es {time_list/time_numpy:.1f}x más rápido")

# Copia vs vista
original = np.arange(10)
view = original[::2]  # vista
copy = original[::2].copy()  # copia

print("\nOriginal:", original)
original[0] = 999
print("Después de modificar original[0]:")
print("Vista:", view)  # cambia porque es vista
print("Copia:", copy)  # no cambia porque es copia independiente

# =============================================================================
# EJERCICIOS PROPUESTOS
# =============================================================================

print("\n" + "=" * 50)
print("EJERCICIOS PROPUESTOS")
print("=" * 50)

print(
    """
1. Crear una matriz 5x5 con valores aleatorios y:
   - Encontrar el elemento máximo y su posición
   - Calcular la suma de cada fila
   - Normalizar la matriz (media=0, std=1)

2. Simular el lanzamiento de 1000 dados y:
   - Calcular la frecuencia de cada número
   - Graficar el histograma
   - Comparar con distribución uniforme teórica

3. Implementar una función que:
   - Reciba dos matrices como parámetros
   - Calcule su producto matricial
   - Maneje errores de dimensiones incompatibles
   - Retorne también el determinante si es matriz cuadrada
"""
)

print("\n¡Notebook completado! Experimenta con los conceptos y ejercicios.")
