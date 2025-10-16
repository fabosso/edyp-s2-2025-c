# “””
DEMOSTRACIÓN DE EFICIENCIA: SETS vs LISTAS

Comparación con mediciones de tiempo real
“””

import time
import random

# ============================================================================

# 1. BÚSQUEDA DE ELEMENTOS: O(n) vs O(1)

# ============================================================================

def demo_busqueda():
“””
Demuestra la diferencia de velocidad en búsquedas.
Lista: O(n) - debe revisar cada elemento
Set: O(1) - acceso directo mediante hash
“””
print(”=” * 70)
print(“1. BÚSQUEDA DE ELEMENTOS”)
print(”=” * 70)

```
# Crear datos de prueba
tamanios = [1_000, 10_000, 100_000, 500_000]

for tamanio in tamanios:
    # Crear lista y set con los mismos datos
    datos = list(range(tamanio))
    lista = datos.copy()
    conjunto = set(datos)
    
    # Buscar elementos que están al final (peor caso para lista)
    elementos_buscar = [tamanio - 1, tamanio - 100, tamanio - 500]
    
    # Búsqueda en LISTA
    inicio = time.perf_counter()
    for elemento in elementos_buscar:
        _ = elemento in lista
    tiempo_lista = time.perf_counter() - inicio
    
    # Búsqueda en SET
    inicio = time.perf_counter()
    for elemento in elementos_buscar:
        _ = elemento in conjunto
    tiempo_set = time.perf_counter() - inicio
    
    # Calcular cuánto más rápido es el set
    mejora = tiempo_lista / tiempo_set if tiempo_set > 0 else float('inf')
    
    print(f"\n📊 Tamaño: {tamanio:,} elementos")
    print(f"   Lista:    {tiempo_lista*1000:8.4f} ms")
    print(f"   Set:      {tiempo_set*1000:8.4f} ms")
    print(f"   ⚡ Set es {mejora:.0f}x más rápido")
```

# ============================================================================

# 2. ELIMINACIÓN DE DUPLICADOS

# ============================================================================

def demo_duplicados():
“””
Compara la eliminación de duplicados con lista vs set.
“””
print(”\n” + “=” * 70)
print(“2. ELIMINACIÓN DE DUPLICADOS”)
print(”=” * 70)

```
tamanios = [10_000, 50_000, 100_000]

for tamanio in tamanios:
    # Crear lista con muchos duplicados
    datos = [random.randint(0, tamanio // 10) for _ in range(tamanio)]
    
    # Método 1: Con lista (manual)
    inicio = time.perf_counter()
    unicos_lista = []
    for elemento in datos:
        if elemento not in unicos_lista:
            unicos_lista.append(elemento)
    tiempo_lista = time.perf_counter() - inicio
    
    # Método 2: Con set (automático)
    inicio = time.perf_counter()
    unicos_set = list(set(datos))
    tiempo_set = time.perf_counter() - inicio
    
    mejora = tiempo_lista / tiempo_set
    
    print(f"\n📊 Tamaño: {tamanio:,} elementos")
    print(f"   Únicos encontrados: {len(unicos_set):,}")
    print(f"   Lista:    {tiempo_lista*1000:8.2f} ms")
    print(f"   Set:      {tiempo_set*1000:8.2f} ms")
    print(f"   ⚡ Set es {mejora:.0f}x más rápido")
```

# ============================================================================

# 3. INTERSECCIÓN DE CONJUNTOS

# ============================================================================

def demo_interseccion():
“””
Compara encontrar elementos comunes entre dos colecciones.
“””
print(”\n” + “=” * 70)
print(“3. ENCONTRAR ELEMENTOS COMUNES (INTERSECCIÓN)”)
print(”=” * 70)

```
tamanios = [1_000, 5_000, 10_000]

for tamanio in tamanios:
    # Crear dos conjuntos de datos con elementos comunes
    lista1 = list(range(tamanio))
    lista2 = list(range(tamanio // 2, tamanio + tamanio // 2))
    
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    # Método 1: Con listas (doble loop)
    inicio = time.perf_counter()
    comunes_lista = [x for x in lista1 if x in lista2]
    tiempo_lista = time.perf_counter() - inicio
    
    # Método 2: Con sets (operación nativa)
    inicio = time.perf_counter()
    comunes_set = conjunto1.intersection(conjunto2)
    tiempo_set = time.perf_counter() - inicio
    
    mejora = tiempo_lista / tiempo_set
    
    print(f"\n📊 Tamaño: {tamanio:,} elementos cada colección")
    print(f"   Comunes encontrados: {len(comunes_lista):,}")
    print(f"   Lista:    {tiempo_lista*1000:8.2f} ms")
    print(f"   Set:      {tiempo_set*1000:8.2f} ms")
    print(f"   ⚡ Set es {mejora:.0f}x más rápido")
```

# ============================================================================

# 4. CASO PRÁCTICO: SISTEMA DE ESTUDIANTES

# ============================================================================

class Estudiante:
“”“Clase de estudiante con hash eficiente.”””

```
def __init__(self, legajo, nombre, carrera):
    self.legajo = legajo
    self.nombre = nombre
    self.carrera = carrera

def __hash__(self):
    return hash(self.legajo)

def __eq__(self, other):
    if not isinstance(other, Estudiante):
        return False
    return self.legajo == other.legajo

def __repr__(self):
    return f"E{self.legajo}"
```

def demo_caso_practico():
“””
Caso práctico: verificar si estudiantes están inscriptos en una materia.
“””
print(”\n” + “=” * 70)
print(“4. CASO PRÁCTICO: SISTEMA DE ESTUDIANTES”)
print(”=” * 70)

```
# Crear base de estudiantes inscriptos en una materia
cantidad_inscriptos = 50_000
estudiantes_lista = [
    Estudiante(i, f"Estudiante{i}", "Ingeniería")
    for i in range(cantidad_inscriptos)
]
estudiantes_set = set(estudiantes_lista)

# Estudiantes que quieren ingresar al examen (verificar inscripción)
cantidad_verificar = 1_000
a_verificar = [
    Estudiante(random.randint(0, cantidad_inscriptos + 10_000), "", "")
    for _ in range(cantidad_verificar)
]

print(f"\n📚 Estudiantes inscriptos: {cantidad_inscriptos:,}")
print(f"🎓 Estudiantes a verificar: {cantidad_verificar:,}")

# Verificación con LISTA
inicio = time.perf_counter()
autorizados_lista = 0
for estudiante in a_verificar:
    if estudiante in estudiantes_lista:
        autorizados_lista += 1
tiempo_lista = time.perf_counter() - inicio

# Verificación con SET
inicio = time.perf_counter()
autorizados_set = 0
for estudiante in a_verificar:
    if estudiante in estudiantes_set:
        autorizados_set += 1
tiempo_set = time.perf_counter() - inicio

mejora = tiempo_lista / tiempo_set

print(f"\n✅ Autorizados: {autorizados_set}")
print(f"   Lista:    {tiempo_lista*1000:8.2f} ms")
print(f"   Set:      {tiempo_set*1000:8.2f} ms")
print(f"   ⚡ Set es {mejora:.0f}x más rápido")
```

# ============================================================================

# 5. VISUALIZACIÓN DE COMPLEJIDAD

# ============================================================================

def demo_visualizacion_complejidad():
“””
Muestra cómo crece el tiempo con el tamaño de datos.
“””
print(”\n” + “=” * 70)
print(“5. VISUALIZACIÓN: CRECIMIENTO DEL TIEMPO DE BÚSQUEDA”)
print(”=” * 70)

```
tamanios = [1_000, 5_000, 10_000, 50_000, 100_000]
busquedas = 1_000  # Número de búsquedas a realizar

print(f"\nRealizando {busquedas} búsquedas en cada tamaño...\n")
print(f"{'Tamaño':<15} {'Lista (ms)':<15} {'Set (ms)':<15} {'Mejora':<10}")
print("-" * 70)

for tamanio in tamanios:
    datos = list(range(tamanio))
    lista = datos.copy()
    conjunto = set(datos)
    
    # Elementos a buscar (aleatorios)
    elementos = [random.randint(0, tamanio - 1) for _ in range(busquedas)]
    
    # Búsqueda en lista
    inicio = time.perf_counter()
    for elemento in elementos:
        _ = elemento in lista
    tiempo_lista = time.perf_counter() - inicio
    
    # Búsqueda en set
    inicio = time.perf_counter()
    for elemento in elementos:
        _ = elemento in conjunto
    tiempo_set = time.perf_counter() - inicio
    
    mejora = tiempo_lista / tiempo_set
    
    # Crear barra visual
    barra_lista = "█" * int(tiempo_lista * 1000)
    barra_set = "█" * max(1, int(tiempo_set * 1000))
    
    print(f"{tamanio:>10,}     {tiempo_lista*1000:8.2f}       {tiempo_set*1000:8.2f}        {mejora:>6.0f}x")

print("\n💡 OBSERVACIÓN:")
print("   - El tiempo de búsqueda en LISTA crece linealmente (O(n))")
print("   - El tiempo de búsqueda en SET se mantiene constante (O(1))")
```

# ============================================================================

# 6. RESUMEN CON TABLA DE COMPLEJIDADES

# ============================================================================

def mostrar_resumen():
“””
Muestra un resumen de las complejidades.
“””
print(”\n” + “=” * 70)
print(“📊 TABLA DE COMPLEJIDADES”)
print(”=” * 70)

```
print("""
```

╔══════════════════════╦════════════════╦════════════════╗
║     Operación        ║     Lista      ║      Set       ║
╠══════════════════════╬════════════════╬════════════════╣
║ Búsqueda (x in …)  ║    O(n)        ║    O(1) ⚡     ║
║ Agregar elemento     ║    O(1)        ║    O(1) ⚡     ║
║ Eliminar elemento    ║    O(n)        ║    O(1) ⚡     ║
║ Eliminar duplicados  ║    O(n²)       ║    O(n) ⚡     ║
║ Intersección         ║    O(n*m)      ║    O(min(n,m)) ⚡ ║
║ Unión                ║    O(n*m)      ║    O(n+m) ⚡   ║
╚══════════════════════╩════════════════╩════════════════╝

Donde:
n = tamaño de la primera colección
m = tamaño de la segunda colección
⚡ = significativamente más eficiente

💡 CONCLUSIÓN:

- Para búsquedas frecuentes: USA SETS
- Para eliminar duplicados: USA SETS
- Para operaciones de conjuntos (∩, ∪, -): USA SETS
- Para mantener orden: USA LISTAS
- Para acceso por índice: USA LISTAS
  “””)

# ============================================================================

# EJECUTAR TODAS LAS DEMOS

# ============================================================================

def main():
“””
Ejecuta todas las demostraciones.
“””
print(”\n”)
print(“╔” + “═” * 68 + “╗”)
print(“║” + “ “ * 15 + “DEMOSTRACIÓN DE EFICIENCIA: SETS vs LISTAS” + “ “ * 12 + “║”)
print(“╚” + “═” * 68 + “╝”)

```
demo_busqueda()
demo_duplicados()
demo_interseccion()
demo_caso_practico()
demo_visualizacion_complejidad()
mostrar_resumen()

print("\n" + "=" * 70)
print("✅ DEMOSTRACIÓN COMPLETA")
print("=" * 70)
print("\n💡 Consejo: Usa sets cuando necesites búsquedas rápidas y")
print("   no te importe el orden de los elementos.\n")
```

if **name** == “**main**”:
main()