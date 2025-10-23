# =============================================================================
# 2. Simular el lanzamiento de 1000 dados y:
#    - Calcular la frecuencia de cada número
#    - Graficar el histograma
#    - Comparar con distribución uniforme teórica
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
dados = np.random.randint(1, 7, 1000)

print(f"Primeros 20 lanzamientos: {dados[:20]}")

# Calcular frecuencias
valores_unicos, frecuencias = np.unique(dados, return_counts=True)

print("\nFrecuencias observadas:")
for valor, freq in zip(valores_unicos, frecuencias):
    porcentaje = (freq / 1000) * 100
    print(f"Cara {valor}: {freq} veces ({porcentaje:.1f}%)")

# Frecuencia teórica (distribución uniforme)
freq_teorica = 1000 / 6  # 166.67 aproximadamente

print(f"\nFrecuencia teórica esperada: {freq_teorica:.2f} por cada cara")

# Test Chi-cuadrado simple
chi2 = np.sum((frecuencias - freq_teorica) ** 2 / freq_teorica)
print(f"Estadístico Chi-cuadrado: {chi2:.3f}")

# Crear histograma
plt.figure(figsize=(10, 6))

# Subplot 1: Histograma observado
plt.subplot(1, 2, 1)
plt.bar(valores_unicos, frecuencias, alpha=0.7, color="skyblue", edgecolor="black")
plt.axhline(
    y=freq_teorica, color="red", linestyle="--", label=f"Teórico ({freq_teorica:.1f})"
)
plt.xlabel("Cara del dado")
plt.ylabel("Frecuencia")
plt.title("Frecuencias Observadas vs Teóricas")
plt.legend()
plt.grid(True, alpha=0.3)

# Subplot 2: Diferencias
plt.subplot(1, 2, 2)
diferencias = frecuencias - freq_teorica
colores = ["red" if d < 0 else "green" for d in diferencias]
plt.bar(valores_unicos, diferencias, color=colores, alpha=0.7, edgecolor="black")
plt.axhline(y=0, color="black", linestyle="-", linewidth=0.8)
plt.xlabel("Cara del dado")
plt.ylabel("Diferencia (Observado - Teórico)")
plt.title("Desviaciones de la Distribución Uniforme")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Análisis estadístico adicional
print("\nAnálisis estadístico:")
print(f"Media observada: {np.mean(dados):.3f} (teórica: 3.5)")
print(f"Desviación estándar: {np.std(dados):.3f}")
print(f"Máxima desviación de frecuencia: {np.max(np.abs(diferencias)):.1f}")
