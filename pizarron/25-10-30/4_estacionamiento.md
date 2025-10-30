# **Sistema de Gestión de Reservas en Estacionamiento Inteligente**

Contexto:<br>
Se desea crear un sistema que gestione las reservas de estacionamiento en un edificio inteligente. El sistema debe registrar vehículos identificados por una matrícula única, administrar el orden en que llegan y salen los vehículos, y mantener un conjunto actualizado de vehículos que tienen privilegios especiales para acceder sin espera.

Requisitos Funcionales:

1. Registrar un vehículo con matrícula y hora de llegada.
2. Permitir asignar un lugar según orden de llegada y liberar el lugar cuando el vehículo sale.
3. Mantener una colección sin duplicados de vehículos con privilegios especiales.
4. Consultar rápidamente si un vehículo tiene privilegios.
5. Reportar el orden actual de vehículos esperando lugar, y lista de privilegiados.

Casos de Prueba:<br>
Caso 1: Registro de 3 vehículos y consulta de orden de llegada<br>
Entrada: registrar A123, B456, C789<br>
Salida esperada: Orden llegada: `[A123, B456, C789]`

Caso 2: Asignar lugar y liberar para vehículo B456, consultar orden restante<br>
Entrada: asignar lugar a A123, liberar lugar de B456<br>
Salida esperada: Orden llegada: `[B456, C789]`

Caso 3: Añadir vehículos privilegiados y consulta de pertenencia<br>
Entrada: añadir A123, C789 a privilegiados, consulta B456<br>
Salida esperada: B456 no tiene privilegios, A123 y C789 sí.

**Sistema de Gestión de Reservas en Estacionamiento Inteligente:**Implica cola para orden de llegada y conjunto para privilegios (aunque no se especifican estructuras exactas al estudiante).Para el sistema de gestión de reservas en estacionamiento inteligente descrito, y considerando las estructuras que los estudiantes han visto, las más eficientes son:

- Lista Secuencial (Array/List):<br>
  Para administrar el orden en que llegan y salen los vehículos, una lista secuencial permite almacenar la secuencia y acceder a los vehículos en orden de llegada de forma sencilla.
- Conjunto (Set):<br>
  Para mantener el conjunto actualizado de vehículos con privilegios especiales sin duplicados, el conjunto es la estructura adecuada, ya que evita automáticamente duplicados y permite operaciones rápidas de membresía (pertenencia).
- Diccionario (Dictionary):<br>
  Para consultar rápidamente si un vehículo tiene privilegios, un diccionario con la matrícula como clave y el estado de privilegio como valor es eficiente para acceso rápido (O(1)).
- Cola (Queue), opcionalmente:<br>
  Para modelar la fila de vehículos esperando su lugar, se puede usar una cola que respeta el orden de llegada y facilita la asignación del próximo lugar disponible.
- Listas enlazadas simples y pilas no son ideales:<br>
  Las listas enlazadas simples tienen acceso lento por índice y pilas no representan el comportamiento FIFO que necesita el orden de llegada.
- Arrays de NumPy no son necesarios:<br>
  Como el manejo es más sobre secuencia y conjuntos de datos no numéricos, NumPy no aporta ventajas en este caso.

En resumen, la combinación recomendada es:

- Lista secuencial para el orden de llegada y gestión de reservas.
- Set para vehículos privilegiados únicos.
- Diccionario para acceso rápido a estado de privilegio.
- Cola para modelo de espera (opcional).
