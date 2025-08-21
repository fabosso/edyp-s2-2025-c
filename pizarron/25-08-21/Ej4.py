# Realizar una función que dadas dos cadenas de caracteres de igual longitud `n`,
# verifique si existe alguna permutación posible en cualquiera de las cadenas, de
# modo que cada carácter de una cadena sea mayor o igual a cada carácter de la otra
# cadena, en el índice correspondiente. La función debe devolver `True` si es
# posible la permutación en caso contrario devolverá `False`.

def permutacion_posible(cadena1: str, cadena2: str):
    if (len(cadena1) != len(cadena2)):
        return False

    domina = lambda a, b: len(list(filter(lambda par: par[0] >= par[1], zip(sorted(a), sorted(b))))) == len(a)
    return domina(cadena1, cadena2) or domina(cadena2, cadena1)


def main():
    cadena1 = "adb"
    cadena2 = "cda"
    salida = permutacion_posible(cadena1, cadena2)
    print(cadena1, cadena2, salida, sep="\n")
    # Debería imprimirse:
    # "adb"
    # "adc"
    # True
    cadena1 = "gfg"
    cadena2 = "agd"
    salida = permutacion_posible(cadena1, cadena2)
    print(salida)
    # Debería imprimirse:
    # True



# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
