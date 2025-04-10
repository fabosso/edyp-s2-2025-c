import functools

datos = "1,2,3,4,5,6,7,8,9,10"
print(datos)

# Map: aplica una función a todos los elementos de un iterable (listas, cadeas)
# Filter: aplica una función que retorna verdadero o falso a un iterable,  retornando solo los elementos verdaderos.
# Reduce: Aplica una funcion con dos parametros retornando uno, hasta quedarse con un valor.

"""
Ejemplo
Dado [1, 2, 3, 4]
Aplico reduce con lambda x, y: x + y
[1 + 2, 3, 4]
[3 + 3, 4]
[6 + 4]
10
"""

"""
Escribe un programa en Python que tome una cadena de texto con números enteros separados por comas,
 filtre solo los números pares, y devuelva una nueva cadena con estos números pares separados por 
 comas y espacios
"""

resultado = functools.reduce(
    lambda x, y: x + "," + y,
    map(
        lambda x: str(x),
        filter(lambda x: x % 2 == 0, map(lambda x: int(x), datos.split(","))),
    ),
)


print(resultado)
