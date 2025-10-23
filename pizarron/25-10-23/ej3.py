# =============================================================================
# 3. Implementar una función que:
#    - Reciba dos matrices como parámetros
#    - Calcule su producto matricial
#    - Maneje errores de dimensiones incompatibles
#    - Retorne también el determinante si es matriz cuadrada
# =============================================================================
import numpy as np


def multiplicacion_matricial_robusta(A, B):
    """
    Multiplica dos matrices con manejo de errores y cálculo de determinante.

    Parámetros:
    -----------
    A, B : array-like
        Matrices a multiplicar

    Retorna:
    --------
    dict : Diccionario con resultado, determinante (si aplica) y metadatos
    """

    # Convertir a arrays NumPy
    try:
        A = np.asarray(A, dtype=float)
        B = np.asarray(B, dtype=float)
    except Exception as e:
        return {
            "exito": False,
            "error": f"Error al convertir entradas a arrays: {e}",
            "resultado": None,
        }

    # Verificar que son matrices (2D)
    if A.ndim != 2 or B.ndim != 2:
        return {
            "exito": False,
            "error": f"Las entradas deben ser matrices 2D. Dimensiones: A={A.ndim}D, B={B.ndim}D",
            "resultado": None,
        }

    # Verificar compatibilidad de dimensiones para multiplicación
    if A.shape[1] != B.shape[0]:
        return {
            "exito": False,
            "error": f"Dimensiones incompatibles: A{A.shape} × B{B.shape}. A.cols debe = B.rows",
            "resultado": None,
        }

    # Realizar multiplicación
    try:
        producto = A @ B
    except Exception as e:
        return {
            "exito": False,
            "error": f"Error en multiplicación: {e}",
            "resultado": None,
        }

    # Preparar resultado
    resultado = {
        "exito": True,
        "error": None,
        "resultado": producto,
        "shape_A": A.shape,
        "shape_B": B.shape,
        "shape_resultado": producto.shape,
        "determinante_A": None,
        "determinante_B": None,
        "determinante_resultado": None,
    }

    # Calcular determinantes si las matrices son cuadradas
    if A.shape[0] == A.shape[1]:  # A es cuadrada
        try:
            resultado["determinante_A"] = np.linalg.det(A)
        except:
            resultado["determinante_A"] = "Error al calcular"

    if B.shape[0] == B.shape[1]:  # B es cuadrada
        try:
            resultado["determinante_B"] = np.linalg.det(B)
        except:
            resultado["determinante_B"] = "Error al calcular"

    if producto.shape[0] == producto.shape[1]:  # Producto es cuadrado
        try:
            resultado["determinante_resultado"] = np.linalg.det(producto)
        except:
            resultado["determinante_resultado"] = "Error al calcular"

    return resultado


# CASOS DE PRUEBA

print("Caso 1: Multiplicación válida 2x3 × 3x2")
A1 = [[1, 2, 3], [4, 5, 6]]
B1 = [[7, 8], [9, 10], [11, 12]]

resultado1 = multiplicacion_matricial_robusta(A1, B1)
if resultado1["exito"]:
    print("✓ Multiplicación exitosa")
    print(
        f"A{resultado1['shape_A']} × B{resultado1['shape_B']} = C{resultado1['shape_resultado']}"
    )
    print("Resultado:")
    print(resultado1["resultado"])
    print(f"Det(resultado): {resultado1['determinante_resultado']}")
else:
    print("✗ Error:", resultado1["error"])

print("\n" + "-" * 50)
print("Caso 2: Matrices cuadradas 2x2")
A2 = [[1, 2], [3, 4]]
B2 = [[5, 6], [7, 8]]

resultado2 = multiplicacion_matricial_robusta(A2, B2)
if resultado2["exito"]:
    print("✓ Multiplicación exitosa")
    print("Matriz A:")
    print(resultado2["shape_A"], f"Det(A) = {resultado2['determinante_A']:.3f}")
    print("Matriz B:")
    print(resultado2["shape_B"], f"Det(B) = {resultado2['determinante_B']:.3f}")
    print("Resultado A×B:")
    print(resultado2["resultado"])
    print(f"Det(A×B) = {resultado2['determinante_resultado']:.3f}")

    # Verificar propiedad: det(AB) = det(A) × det(B)
    det_producto_teorico = resultado2["determinante_A"] * resultado2["determinante_B"]
    print(f"\nVerificación: det(A)×det(B) = {det_producto_teorico:.3f}")
    print(
        f"¿Coincide? {np.allclose(resultado2['determinante_resultado'], det_producto_teorico)}"
    )
else:
    print("✗ Error:", resultado2["error"])

print("\n" + "-" * 50)
print("Caso 3: Error - Dimensiones incompatibles")
A3 = [[1, 2], [3, 4]]  # 2x2
B3 = [[1, 2, 3]]  # 1x3

resultado3 = multiplicacion_matricial_robusta(A3, B3)
print("✗ Error esperado:", resultado3["error"])

print("\n" + "-" * 50)
print("Caso 4: Error - Entrada no es matriz")
A4 = [1, 2, 3]  # Vector 1D
B4 = [[1], [2], [3]]

resultado4 = multiplicacion_matricial_robusta(A4, B4)
print("✗ Error esperado:", resultado4["error"])

print("\n" + "-" * 50)
print("Caso 5: Matriz identidad")
I = np.eye(3)
A5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

resultado5 = multiplicacion_matricial_robusta(I, A5)
if resultado5["exito"]:
    print("✓ Multiplicación con identidad")
    print("I × A debería ser igual a A:")
    print("Resultado:")
    print(resultado5["resultado"])
    print("Original A:")
    print(np.array(A5))
    print(f"¿Son iguales? {np.allclose(resultado5['resultado'], A5)}")
