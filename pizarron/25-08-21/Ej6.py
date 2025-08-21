# Realizar una función que, dada una cadena de caracteres, cuente la cantidad de
# cada uno de los caracteres que se encuentran en la cadena.

def imprimir_contadores(cadena: str):
    # Cadena de ejemplo: "Estructuras de datos"
    s = cadena.lower().replace(" ", "")
    # s -> "estructurasdedatos"

    indices_unicos = filter(lambda i: s.find(s[i]) == i, range(len(s)))
    # Retorna un iterable para que utilizemos luego en el map
    # Este iterable contiene las posiciones de letras "interesantes"
    # en la cadena `estructurasdedatos`, que aparecen por primera vez
    # Son:
    # 0 -> "e"
    # 1 -> "s"
    # 2 -> "t"
    # 3 -> "r"
    # 4 -> "u"
    # 5 -> "c"
    # 9 -> "a"
    # 11 -> "d"
    # 16 -> "o"

    parejas = map(lambda i: (s[i], s.count(s[i])), indices_unicos)
    # Iteramos los indices únicos encontrados a través de la variable iteradora, `i`
    # En `s[i]` tenemos las letras únicas, y las emparejamos con la cantidad de
    # repeticiones de dicha letra, usando el método `count`.
    # Luego, map nos devuelve un iterable con estas tuplas:
    # ("e", 2)
    # ("s", 3)
    # ("t", 3)
    # ("r", 2)
    # ("u", 2)
    # ("c", 1)
    # ("a", 2)
    # ("d", 2)
    # ("o", 1)

    for caracter, cantidad in parejas:
        print(f"{caracter}\t{cantidad}")
    # Finalmente, iteramos `parejas`,
    # desarmamos la tupla en las variables `caracter` y `cantidad`
    # e imprimimos con un tabulado de espacio


def main():
    cadena = "Estructuras de datos"
    imprimir_contadores(cadena)
    # Debería imprimirse:
    # e     2
    # s     3
    # t     3
    # r     2
    # u     2
    # c     1
    # a     2
    # d     2
    # o     1


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
