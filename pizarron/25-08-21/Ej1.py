# Implemente la funcion "contar_simbolos" que permita contar la cantidad total de
# caracteres alfabéticos, dígitos y caracteres especiales en una cadena y las
# retorne en forma de una lista.
# Reimplemente utilizando funciones lambda y de primera clase y compare las
# soluciones.

def contar_simbolos(cadena: str):
    letras = list(filter(lambda c: c.isalpha(), cadena))
    digitos = list(filter(lambda c: c.isdigit(), cadena))
    especiales = list(filter(lambda c: not (c.isalpha() or c.isdigit()), cadena))

    # Tu implementacion va aqui
    return [len(letras), len(digitos), len(especiales)]


def main():
    resultado = contar_simbolos("Hola Mundo 123!@#")
    print(resultado)  # Debería imprimir [9, 3, 5]


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
