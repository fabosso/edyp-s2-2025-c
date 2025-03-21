# Dado una lista de caracteres y sus repeticiones ordenelos de mayor a menor
caracteres = ["a", "b", "c", "d", "e"]
repeticiones = [1, 2, 3, 4, 5]

# Con zip las listas deben ser iguales, o de lo contrario trunca a la longitud de la
# mas corta
lista_final = list(zip(caracteres, repeticiones))

# El parametro key permite customizar el dato que utilizará sort para ordenar
lista_final.sort(key=lambda x: x[1])
lista_final.reverse()

print(lista_final)