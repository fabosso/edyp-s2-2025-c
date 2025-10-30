**Sistema de Atención al Cliente con Prioridades**

**Contexto:**

Un centro de atención telefónica maneja llamadas de clientes que deben ser atendidas en estricto orden de llegada. Cada llamada tiene información que no cambia durante todo el proceso: el número de ticket, nombre del cliente, tipo de consulta y timestamp de cuándo llegó. Esta información debe permanecer intacta y no debe ser modificable una vez creada la llamada.

El sistema tiene varios operadores que toman llamadas de una cola central. Cuando un operador queda libre, debe atender la siguiente llamada que está esperando hace más tiempo. El centro necesita saber en todo momento cuántas llamadas están esperando, cuál es la próxima llamada a atender (sin quitarla de la cola), y poder procesar llamadas de manera ordenada.

Adicionalmente, el sistema debe generar reportes cada hora. Estos reportes contienen datos estadísticos que una vez generados no deben cambiar: el periodo del reporte (hora inicio y fin), cantidad de llamadas atendidas, tiempo promedio de espera, y el operador más activo. Esta información del reporte debe ser inmutable para mantener la integridad de los registros históricos.

**Requisitos Funcionales:**

1. Registrar una nueva llamada entrante en la cola de espera
2. Asignar la siguiente llamada a un operador disponible (respetando orden de llegada)
3. Consultar la próxima llamada sin quitarla de la cola
4. Obtener el número de llamadas esperando
5. Generar un reporte de estadísticas del periodo (datos inmutables)
6. Consultar información de reportes históricos
7. Verificar si hay llamadas en espera

**Restricciones técnicas:**

- Los datos de LlamadaCliente deben almacenarse en una tupla (inmutable)
- Los datos de ReporteHorario deben almacenarse en una tupla (inmutable)
- La cola de llamadas debe procesarse en orden FIFO estricto
- Usar collections.deque o implementación propia para la cola

**Estructuras Esperadas:**

- Cola (Queue):<br>
  Para manejar la cola central de llamadas en orden estricto de llegada, la cola es la estructura natural y eficiente que cumple el principio FIFO (First In, First Out). Permite agregar llamadas al final y atender llamadas desde el frente en orden correcto.
- Tuplas:<br>
  Para guardar cada llamada como una entidad inmutable con número de ticket, nombre, tipo y timestamp. Esto garantiza que los datos de la llamada no cambien una vez creados, manteniendo integridad durante todo el proceso.
- Listas secuenciales o diccionarios:<br>
  Para almacenar los reportes horarios. Dado que los reportes deben ser inmutables, una opción es usar tuplas para cada reporte. Para acceder y consultar reportes históricos, un diccionario con clave como el periodo (hora inicio) facilitaría la búsqueda rápida.
