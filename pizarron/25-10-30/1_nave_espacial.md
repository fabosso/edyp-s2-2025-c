## **Control de Navegación en Nave Espacial**

Contexto:

Se necesita implementar parte de un sistema de control para una nave espacial que guarda las coordenadas visitadas en orden para poder regresar y rastrear su recorrido. Además, el sistema deberá poder deshacer las últimas maniobras realizadas por el piloto para corregir errores de navegación.

Requisitos Funcionales:

1. Almacenar las coordenadas visitadas en el orden en que fueron recorridas.
2. Permitir obtener la secuencia completa actual de coordenadas.
3. Permitir deshacer la última maniobra retornando a la coordenada previa.
4. Soportar la gestión eficiente de deshacer/repetir maniobras.

**Control de Navegación en Nave Espacial**: Usa listas para recorrido e historial (listas simples) y pilas implícitas (último en procesar).
