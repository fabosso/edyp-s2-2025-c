# **Registro y Control de Mediciones Inmutables en Sensor Ambiental**

**Contexto:**

Un sensor recolecta mediciones en intervalos fijos que se almacenan con valores de temperatura, humedad y presión. Cada medición es inmutable y debe conservarse sin cambios para análisis. El sistema debe almacenar y retornar múltiples valores por medición para informes.

Requisitos Funcionales:

1. Guardar cada medición como una entidad inmutable con temperatura, humedad y presión.
2. Retornar series temporales de mediciones en secuencia ordenada.
3. Calcular valores promedio para cada variable sobre el conjunto de mediciones almacenadas.

Casos de Prueba:

- Ingresar varias mediciones, solicitar todas.
- Calcular promedios correctos de los valores.
- Validar que no se modifiquen las mediciones almacenadas.

Para solucionar el problema descrito utilizando las estructuras que los estudiantes han visto, las opciones más eficientes son:

- Tuplas: Son ideales para guardar cada medición como una entidad inmutable con sus valores de temperatura, humedad y presión. Siendo inmutables, garantizan que las mediciones no se modifiquen y representan bien un conjunto fijo de valores.
- Listas secuenciales: Para almacenar las mediciones en orden temporal y retornar la serie completa. Las listas permiten añadir mediciones secuencialmente y recorrerlas fácilmente para informes
