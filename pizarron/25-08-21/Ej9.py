# Realizar una función que, dada una cadena de caracteres y un número entero `k`,
# reduzca el tamaño de la cadena de acuerdo con las siguientes indicaciones:
# - Debe escoger un grupo de `k` caracteres idénticos consecutivos y 
# - Debe eliminarlos de la cadena
# - Debe repetir esta operación  la cantidad de veces necesarias hasta que ya no sea
# posible hacerlo.

from functools import reduce

# Factory de processors
def crear_processor(k: int):
    def _procesar_char(acumulador: list, char_actual: str):
        # La lógica es idéntica, pero ahora 'k' viene del ámbito superior (closure).
        if acumulador and acumulador[-1][0] == char_actual:
            acumulador[-1][1] += 1
        else:
            acumulador.append([char_actual, 1])

        if acumulador and acumulador[-1][1] == k:
            acumulador.pop()

        return acumulador

    return _procesar_char

def reducir(cadena: str, k: int):
    # Cláusula de guarda
    if k == 1:
        return ""

    # 1. Creamos el procesador específico para nuestro `k`.
    processor = crear_processor(k)

    # 2. Reducimos aplicando el procesador a la cadena.
    # El acumulador es inicialmente una lista vacía, `[]`.
    stack_reducido = reduce(processor, cadena, [])

    # 3. Reconstruimos la cadena a partir del stack reducido.
    # Usamos map con una función lambda para repetir cada caracter su número de veces.
    # Ej: [['a', 2], ['c', 1]] -> ['aa', 'c']
    segmentos = map(lambda item: item[0] * item[1], stack_reducido)

    # 4. Unimos los segmentos para obtener la cadena final.
    return "".join(segmentos)


def main():
    cadena = "deeedbbcccbdaa"
    k = 3

    # Pasos:
    # 1. "deeedbbcccbdaa" -> "ddbbcccbdaa" (se va "eee")
    # 2. "ddbbcccbdaa" -> "ddbbdaa" (se va "ccc")
    # 3. "ddbbdaa" -> "dddaa" (se va "bb")
    # 4. "dddaa" -> "aa" (se va "ddd")
    cadena_reducida = reducir(cadena, k)
    print(cadena_reducida)


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
