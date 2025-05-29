---
marp: true
theme: default
paginate: true
backgroundColor: #fff
---

# Estructura de datos y programación
## Reunión 9: NumPy

**Numerical Python - La biblioteca esencial para computación científica**

---

## ¿Qué es NumPy?

- Biblioteca open source de Python para ciencia e ingeniería
- Estructuras de datos multidimensionales eficientes (**ndarray**)
- Gran colección de funciones matemáticas optimizadas
- Base del ecosistema científico de Python

```python
import numpy as np
```

---

## ¿Por qué usar NumPy?

**Listas de Python** vs **Arrays de NumPy**

- **Listas**: Heterogéneas, flexibles, lentas para operaciones masivas
- **Arrays**: Homogéneos, restricciones, pero mucho más eficientes

NumPy brilla cuando:
- Grandes cantidades de datos del mismo tipo
- Operaciones matemáticas intensivas
- Procesamiento en CPU optimizado

---

## Concepto de Array

Un array es una estructura para almacenar datos en forma de grilla:

- **1D**: Lista `[1, 2, 3, 4]`
- **2D**: Tabla/Matriz
- **3D**: Conjunto de tablas apiladas
- **N-D**: Generalización a N dimensiones (**ndarray**)

**Restricciones importantes:**
- Todos los elementos del mismo tipo
- Tamaño fijo una vez creado
- Forma rectangular (no irregular)

---

## Creación Básica de Arrays

```python
# Desde lista
a = np.array([1, 2, 3, 4, 5, 6])

# Array 2D desde listas anidadas
matrix = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12]])

# Funciones de creación
np.zeros(5)        # [0. 0. 0. 0. 0.]
np.ones(3)         # [1. 1. 1.]
np.arange(4)       # [0 1 2 3]
np.linspace(0, 10, 5)  # [0. 2.5 5. 7.5 10.]
```

---

## Atributos Fundamentales

```python
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(a.ndim)    # 2 (dimensiones)
print(a.shape)   # (2, 4) (filas, columnas)
print(a.size)    # 8 (total elementos)
print(a.dtype)   # int64 (tipo de dato)
```

**Terminología importante:**
- **Dimensión/Eje (axis)**: Cada dirección del array
- **Shape**: Tupla con el tamaño en cada dimensión

---

## Indexación y Slicing

```python
data = np.array([1, 2, 3, 4, 5])

# Indexación básica (0-indexed)
data[0]     # 1
data[-1]    # 5

# Slicing
data[1:4]   # [2 3 4]
data[:3]    # [1 2 3]

# Arrays 2D
matrix[1, 3]    # Fila 1, columna 3
matrix[0:2, 0]  # Primeras 2 filas, primera columna
```

---

## Indexación Condicional

```python
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Filtrado por condición
print(a[a < 5])          # [1 2 3 4]
print(a[a >= 5])         # [5 6 7 8 9 10 11 12]

# Múltiples condiciones
print(a[(a > 2) & (a < 11)])  # [3 4 5 6 7 8 9 10]

# Elementos divisibles por 2
print(a[a % 2 == 0])     # [2 4 6 8 10 12]
```

---

## Reshape y Manipulación de Forma

```python
a = np.arange(6)  # [0 1 2 3 4 5]

# Cambiar forma (mismo número de elementos)
b = a.reshape(2, 3)
# [[0 1 2]
#  [3 4 5]]

c = a.reshape(3, 2)
# [[0 1]
#  [2 3]
#  [4 5]]

# Añadir dimensiones
row_vector = a[np.newaxis, :]  # (1, 6)
col_vector = a[:, np.newaxis]  # (6, 1)
```

---

## Operaciones Matemáticas Básicas

```python
data = np.array([1, 2, 3, 4])
ones = np.ones(4, dtype=int)

# Operaciones elemento a elemento
data + ones    # [2 3 4 5]
data - ones    # [0 1 2 3]
data * data    # [1 4 9 16]
data / data    # [1. 1. 1. 1.]

# Agregaciones
data.sum()     # 10
data.mean()    # 2.5
data.max()     # 4
data.std()     # Desviación estándar
```

---

## Broadcasting

NumPy puede operar arrays de diferentes tamaños:

```python
data = np.array([1.0, 2.0])
result = data * 1.6  # [1.6, 3.2]

# Array 2D con escalar
matrix = np.array([[1, 2], [3, 4]])
matrix + 10  # [[11 12], [13 14]]

# Arrays de diferentes formas compatibles
matrix + np.array([10, 20])  # Suma [10, 20] a cada fila
```

**Regla**: Las dimensiones deben ser compatibles (iguales o una de ellas es 1)

---

## Matrices y Operaciones 2D

```python
# Creación de matrices
matrix = np.array([[1, 2], [3, 4], [5, 6]])

# Agregaciones por ejes
matrix.sum()        # 21 (todos los elementos)
matrix.sum(axis=0)  # [9 12] (suma por columnas)
matrix.sum(axis=1)  # [3 7 11] (suma por filas)

# Transposición
matrix.T  # Transpuesta
matrix.transpose()  # Alternativa
```

---

## Números Aleatorios

```python
# Generador de números aleatorios moderno
rng = np.random.default_rng()

# Enteros aleatorios
rng.integers(0, 10, size=5)  # 5 enteros entre 0 y 9

# Flotantes aleatorios
rng.random(3)  # 3 números entre 0 y 1

# Matrices aleatorias
rng.random((2, 3))  # Matriz 2x3 de números aleatorios

# Con semilla para reproducibilidad
rng = np.random.default_rng(seed=42)
```

---

## Elementos Únicos y Conteos

```python
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11])

# Valores únicos
unique_values = np.unique(a)
print(unique_values)  # [11 12 13 14 15 16 17]

# Con índices y conteos
unique_values, indices, counts = np.unique(
    a, return_index=True, return_counts=True)

print(counts)  # [3 2 2 1 1 1 1] (frecuencia de cada único)
```

---

## Guardar y Cargar Arrays

```python
a = np.array([1, 2, 3, 4, 5, 6])

# Formato binario NumPy (.npy)
np.save('mi_array.npy', a)
b = np.load('mi_array.npy')

# Formato texto (.csv, .txt)
np.savetxt('datos.csv', a, delimiter=',')
c = np.loadtxt('datos.csv', delimiter=',')

# Múltiples arrays (.npz)
np.savez('varios_arrays.npz', arr1=a, arr2=b)
loaded = np.load('varios_arrays.npz')
```

---

## Fórmulas Matemáticas - Ejemplo MSE

NumPy permite implementar fórmulas complejas de manera elegante:

```python
def mean_squared_error(predictions, labels):
    return np.mean((predictions - labels) ** 2)

# Ejemplo
y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1.1, 2.2, 2.9, 3.8, 5.2])

error = mean_squared_error(y_pred, y_true)
print(f"MSE: {error:.4f}")
```

La potencia está en que funciona igual para 1 o 1,000,000 de elementos.

---

## Integración con Pandas

```python
import pandas as pd

# Leer CSV con Pandas
df = pd.read_csv('datos.csv')
array_data = df.values  # Convertir a NumPy array

# Seleccionar columnas específicas
selected_data = pd.read_csv('datos.csv', 
                           usecols=['columna1', 'columna2']).values

# Guardar array como CSV via Pandas
df_from_array = pd.DataFrame(my_array)
df_from_array.to_csv('output.csv', index=False)
```

---

## Visualización con Matplotlib

```python
import matplotlib.pyplot as plt

# Plot simple
data = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9])
plt.plot(data)
plt.show()

# Plot con líneas y puntos
x = np.linspace(0, 5, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y, 'purple')  # línea
plt.plot(x, y, 'o')       # puntos
plt.show()
```
![bg right fit vertical](https://numpy.org/doc/stable/_images/matplotlib1.png)
![bg](https://numpy.org/doc/stable/_images/matplotlib2.png)


---

## Mejores Prácticas

1. **Usar funciones NumPy optimizadas** en lugar de loops de Python
2. **Aprovechar broadcasting** para operaciones eficientes
3. **Considerar el uso de memoria**: `ravel()` vs `flatten()`
4. **Documentar el código** con docstrings
5. **Usar el generador moderno** para números aleatorios
6. **Vectorizar operaciones** siempre que sea posible

```python
# ❌ Lento
result = []
for i in range(len(array)):
    result.append(array[i] ** 2)

# ✅ Rápido
result = array ** 2
```

---

## Recursos Adicionales

- **Documentación oficial**: [numpy.org](https://numpy.org)
- **Ayuda integrada**: `help(función)` o `función?` en IPython
- **Código fuente**: `función??` en IPython
- **Ecosistema científico**: SciPy, Pandas, Matplotlib, scikit-learn

```python
# Ayuda rápida
np.array?      # Información básica
np.array??     # Código fuente (si disponible)
help(np.mean)  # Documentación completa
```

---

# ¡Gracias!

**NumPy es la base del ecosistema científico de Python**

- Eficiencia en computación numérica
- Sintaxis clara y expresiva  
- Fundamento para machine learning y análisis de datos

**Próximos pasos**: SciPy, Pandas, Matplotlib, scikit-learn