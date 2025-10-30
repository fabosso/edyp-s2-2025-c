# **Optimización de Gestión de Usuarios en Sistema de Membresías**

Contexto:<br>
Actualmente el sistema gestiona usuarios en una lista simple, repitiendo registros y realizando búsquedas lentas para verificar membresías activas. Se debe mejorar el código para evitar duplicados y acelerar consultas.

Tareas:

- Identificar mejoras para eliminar duplicados y mejorar velocidad de consultas.
- Refactorizar con estructuras adecuadas para almacenar usuarios sin duplicados y consultas eficaces.

Casos de Prueba:

- Añadir usuarios repetidos y validar que no se repitan.
- Consultar usuarios activos rápidamente.
- Validar estado tras altas y bajas.
