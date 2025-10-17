"""
RELACIÓN ENTRE SETS Y __hash__
===============================
Explicación completa con ejemplos prácticos
"""

# ============================================================================
# 1. ¿POR QUÉ LOS SETS NECESITAN __hash__?
# ============================================================================

print("=" * 70)
print("1. FUNDAMENTOS: ¿Por qué __hash__?")
print("=" * 70)

"""
Los sets en Python usan una TABLA HASH (hash table) internamente.
Una tabla hash es como un diccionario ultra rápido que permite:
- Búsqueda en O(1) - ¡instantánea!
- Evitar duplicados automáticamente
- Inserción y eliminación rápidas

Para esto, NECESITA calcular un hash de cada elemento.
"""

# Ejemplo: tipos nativos ya son hashables
print("\nTipos nativos hashables:")
print(f"hash(5) = {hash(5)}")
print(f"hash('hola') = {hash('hola')}")
print(f"hash((1, 2, 3)) = {hash((1, 2, 3))}")

# Las listas NO son hashables (son mutables)
try:
    conjunto = {[1, 2, 3]}  # ¡ERROR!
except TypeError as e:
    print(f"\n❌ Error con lista: {e}")

print("\n✅ Los tipos inmutables (int, str, tuple) son hashables por defecto")
print("❌ Los tipos mutables (list, dict, set) NO son hashables")


# ============================================================================
# 2. CLASE SIN __hash__: ¿Qué pasa?
# ============================================================================

print("\n" + "=" * 70)
print("2. CLASE SIN __hash__")
print("=" * 70)


class PersonaSinHash:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Python permite crear el objeto
p1 = PersonaSinHash("Ana", 25)
p2 = PersonaSinHash("Ana", 25)

# Pero cada objeto tiene un hash diferente basado en su dirección en memoria
print(f"\nhash(p1) = {hash(p1)}")
print(f"hash(p2) = {hash(p2)}")
print(f"p1 == p2: {p1 == p2}  # Son objetos diferentes aunque tengan los mismos datos")

# En un set, se tratan como elementos distintos
conjunto = {p1, p2}
print(
    f"len(conjunto) = {len(conjunto)}  # ¡Tiene 2 elementos aunque sean 'la misma' persona!"
)


# ============================================================================
# 3. CLASE CON __hash__ CORRECTO
# ============================================================================

print("\n" + "=" * 70)
print("3. CLASE CON __hash__ Y __eq__ CORRECTOS")
print("=" * 70)


class PersonaConHash:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def __hash__(self):
        """
        Devuelve un número entero que representa al objeto.
        Debe ser inmutable (no cambiar durante la vida del objeto).
        """
        return hash(self.id)  # Usamos el id como identificador único

    def __eq__(self, other):
        """
        Define cuándo dos objetos son iguales.
        REGLA CRUCIAL: Si __hash__ devuelve lo mismo, __eq__ debe dar True
        """
        if not isinstance(other, PersonaConHash):
            return False
        return self.id == other.id

    def __repr__(self):
        return f"Persona({self.id}, '{self.nombre}', {self.edad})"


# Ahora funciona correctamente
p1 = PersonaConHash(1, "Ana", 25)
p2 = PersonaConHash(1, "Ana García", 30)  # Mismo id, pero diferentes datos

print(f"\np1: {p1}")
print(f"p2: {p2}")
print(f"hash(p1) = {hash(p1)}")
print(f"hash(p2) = {hash(p2)}")
print(f"p1 == p2: {p1 == p2}  # ¡True! Porque tienen el mismo id")

conjunto = {p1, p2}
print(f"len(conjunto) = {len(conjunto)}  # Solo 1 elemento (se eliminó el duplicado)")


# ============================================================================
# 4. LA REGLA DE ORO: __hash__ y __eq__ DEBEN SER CONSISTENTES
# ============================================================================

print("\n" + "=" * 70)
print("4. REGLA DE ORO")
print("=" * 70)

print(
    """
⚠️  REGLA CRUCIAL:
   Si dos objetos son iguales (__eq__ da True),
   entonces DEBEN tener el mismo hash (__hash__ debe dar el mismo valor).
   
   Si a == b → entonces hash(a) == hash(b)
   
   (Nota: Lo contrario NO siempre es cierto - objetos con el mismo hash
    pueden ser diferentes. Esto se llama "colisión de hash")
"""
)


# ============================================================================
# 5. EJEMPLO DE HASH MAL IMPLEMENTADO
# ============================================================================

print("\n" + "=" * 70)
print("5. EJEMPLO DE IMPLEMENTACIÓN INCORRECTA")
print("=" * 70)


class PersonaMalHash:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __hash__(self):
        # ❌ MAL: usamos nombre para el hash
        return hash(self.nombre)

    def __eq__(self, other):
        # ❌ MAL: usamos id para la igualdad
        return self.id == other.id

    def __repr__(self):
        return f"Persona({self.id}, '{self.nombre}')"


# Esto rompe la regla de oro
p1 = PersonaMalHash(1, "Ana")
p2 = PersonaMalHash(1, "Carlos")  # Mismo id, diferente nombre

print(f"\np1: {p1}")
print(f"p2: {p2}")
print(f"p1 == p2: {p1 == p2}  # True (mismo id)")
print(f"hash(p1) == hash(p2): {hash(p1) == hash(p2)}  # False (diferente nombre)")
print("❌ ¡Esto VIOLA la regla de oro! Puede causar bugs extraños en sets/dicts")


# ============================================================================
# 6. BUENAS PRÁCTICAS
# ============================================================================

print("\n" + "=" * 70)
print("6. BUENAS PRÁCTICAS")
print("=" * 70)


class ProductoBuenHash:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo  # Inmutable, identificador único
        self.nombre = nombre  # Puede cambiar
        self.precio = precio  # Puede cambiar

    def __hash__(self):
        # ✅ BIEN: Solo usamos atributos inmutables e identificadores únicos
        return hash(self.codigo)

    def __eq__(self, other):
        # ✅ BIEN: Usamos el mismo criterio que __hash__
        if not isinstance(other, ProductoBuenHash):
            return False
        return self.codigo == other.codigo

    def __repr__(self):
        return f"Producto({self.codigo}, '{self.nombre}', ${self.precio})"


# Demostración
prod1 = ProductoBuenHash("P001", "Laptop", 1000)
prod2 = ProductoBuenHash("P001", "Laptop HP", 1200)  # Mismo código, datos diferentes

inventario = {prod1, prod2}
print(f"\n{prod1}")
print(f"{prod2}")
print(f"Productos en inventario: {len(inventario)}")  # Solo 1
print(f"Hash consistente: {hash(prod1) == hash(prod2)}")
print(f"Son iguales: {prod1 == prod2}")


# ============================================================================
# 7. ¿QUÉ PASA INTERNAMENTE EN UN SET?
# ============================================================================

print("\n" + "=" * 70)
print("7. ¿CÓMO FUNCIONA UN SET INTERNAMENTE?")
print("=" * 70)

print(
    """
Cuando haces: conjunto.add(objeto)

1. Python calcula: h = hash(objeto)
2. Usa 'h' para encontrar una posición en la tabla hash
3. Verifica si ya existe un objeto con ese hash en esa posición
4. Si existe, usa __eq__ para verificar si son el mismo objeto
5. Si son iguales (según __eq__), NO lo agrega (evita duplicados)
6. Si son diferentes, lo agrega (colisión de hash)

Esto permite búsquedas en O(1) - ¡instantáneas!
"""
)


# ============================================================================
# 8. EJEMPLO PRÁCTICO: SISTEMA DE ESTUDIANTES
# ============================================================================

print("\n" + "=" * 70)
print("8. EJEMPLO PRÁCTICO: SISTEMA DE ESTUDIANTES")
print("=" * 70)


class Estudiante:
    def __init__(self, legajo, nombre, carrera):
        self.legajo = legajo  # Identificador único inmutable
        self.nombre = nombre
        self.carrera = carrera

    def __hash__(self):
        return hash(self.legajo)

    def __eq__(self, other):
        if not isinstance(other, Estudiante):
            return False
        return self.legajo == other.legajo

    def __repr__(self):
        return f"Estudiante({self.legajo}, '{self.nombre}')"


# Crear estudiantes
e1 = Estudiante(1001, "Ana García", "Ingeniería")
e2 = Estudiante(1002, "Carlos López", "Medicina")
e3 = Estudiante(1001, "Ana García Martinez", "Ingeniería")  # Mismo legajo

# Conjunto de estudiantes inscriptos
inscriptos = {e1, e2, e3}

print(f"\nEstudiantes creados:")
print(f"  {e1}")
print(f"  {e2}")
print(f"  {e3}")

print(f"\nEstudiantes inscriptos: {len(inscriptos)}")  # Solo 2 (e1 y e3 son el mismo)

# Búsqueda ultra rápida
estudiante_buscar = Estudiante(1002, "", "")  # Solo importa el legajo
if estudiante_buscar in inscriptos:
    print(f"✅ El estudiante con legajo 1002 está inscripto")

print("\n" + "=" * 70)
print("RESUMEN")
print("=" * 70)
print(
    """
📌 PUNTOS CLAVE:

1. Los sets usan tablas hash para ser eficientes O(1)
2. __hash__() devuelve un entero que representa al objeto
3. __eq__() define cuándo dos objetos son iguales
4. REGLA DE ORO: Si a == b, entonces hash(a) == hash(b)
5. Usa atributos INMUTABLES e IDENTIFICADORES ÚNICOS en __hash__
6. __hash__ y __eq__ deben usar los MISMOS criterios
7. Objetos mutables (list, dict) no pueden estar en sets

✅ BENEFICIOS:
   - Búsquedas instantáneas
   - Eliminación automática de duplicados
   - Operaciones de conjuntos eficientes (unión, intersección, etc.)
"""
)
