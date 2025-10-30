# **Código para Gestión Inadecuada de Pedidos en Tienda Online**

Contexto:

El siguiente código simula la gestión de pedidos donde se añaden y procesan pedidos pero tiene problemas de eficiencia y estructura. El sistema guarda listas simples de pedidos sin control ni acceso rápido para búsqueda y priorización. El código debe ser mejorado usando las estructuras de datos adecuadas para optimizar búsqueda por identificador y control del orden de procesamiento.

Tareas del estudiante:

- Identificar qué estructuras reemplazar para optimizar la búsqueda por id y el orden de procesamiento.
- Refactorizar el código para que la búsqueda sea eficiente y el procesamiento respete orden de llegada o prioridad.
- Mantener integridad y comportamiento correcto luego de los cambios.

Casos de Prueba:<br>
Caso 1: Buscar pedido por id existente y no existente<br>
Entrada: buscar_pedido(101), buscar_pedido(999)<br>
Salida esperada: pedido con id 101, None para 999

Caso 2: Procesar pedidos en orden correcto<br>
Entrada: agregar pedidos 101, 102, procesar dos veces<br>
Salida esperada: primer procesado 102, segundo 101 (último en entrar, primero en salir)

Caso 3: Confirmar que buscar sigue funcionando tras varios procesos y agregados<br>
Entrada: agregar 103, buscar 103<br>
Salida esperada: pedido 103 encontrado

**Código para Gestión Inadecuada de Pedidos en Tienda Online:** Usa lista simple, pero se invita a optimizar con estructuras más adecuadas (diccionarios, colas, pilas).
