# Realizar una función que, dada una cadena de caracteres visualice si la cadena
# introducida es una cadena bitónica inversa o no.
#
# Una cadena bitónica inversa es una cadena en la que los caracteres están
# dispuestos en orden decreciente seguido de valores crecientes según el código
# ASCII.

def imprimir_bitonica_inversa(cadena: str):
    if es_bitonica_inversa(cadena):
        print(f'La cadena "{cadena}" es bitónica inversa')
    else:
        print(f'La cadena "{cadena}" no es bitónica inversa')

def es_bitonica_inversa(cadena: str) -> bool:
    # Retorno rápido: cadenas con 0 o 1 carácter son siempre bitónicas.
    if len(cadena) < 2:
        return True

    # 1. Encontramos el índice del carácter mínimo (el "valle") de forma funcional.
    # Usamos enumerate para obtener pares (índice, valor).
    # La función lambda le dice a min() que compare los ítems por su valor (el caracter).
    indice_min, _ = min(enumerate(cadena), key=lambda item: item[1])

    # 2. Dividimos la cadena en el punto mínimo.
    parte_decreciente = cadena[:indice_min + 1]
    parte_creciente = cadena[indice_min:]

    # 3. Creamos pares de elementos adyacentes
    pares_decrecientes = zip(parte_decreciente, parte_decreciente[1:])
    pares_crecientes = zip(parte_creciente, parte_creciente[1:])

    print(list(pares_crecientes))
    print(list(pares_decrecientes))

    # 4. Usamos map para aplicar una función lambda de comparación a cada par
    resultados_decrecientes = map(lambda par: par[0] > par[1], pares_decrecientes)
    resultados_crecientes = map(lambda par: par[0] < par[1], pares_crecientes)

    # 5. `all()` verifica si todos los resultados en los iteradores son True
    es_correcta_decreciente = all(resultados_decrecientes)
    es_correcta_creciente = all(resultados_crecientes)

    # 6. Retornar `True` si se cumplen ambas condiciones
    return es_correcta_creciente and es_correcta_decreciente



def main():
    cadena = "zyxbcde"
    imprimir_bitonica_inversa(cadena)
    # Debería imprimirse:
    # La cadena "zyxbcde" es bitónica inversa
    cadena = "abcdwef"
    imprimir_bitonica_inversa(cadena)
    # Debería imprimirse:
    # La cadena "abcdwef" no es bitónica inversa
    cadena = "86479"
    imprimir_bitonica_inversa(cadena)
    # Debería imprimirse:
    # La cadena "86479" es bitónica inversa


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
