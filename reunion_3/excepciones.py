# Funcion con nombre
def duplicar(y):
    return int(y) * 2

invalido = True
while invalido:
    try:
        mi_dato = input("Ingrese un numero: ")
        # Aplico la lambda a la variable mi_dato
        doble = (lambda x: int(x)*2)(mi_dato)
        divide = (lambda x: 1/int(x))(mi_dato)
        invalido = False
    except ValueError:
        # Manejo un tipo de error, con cuidado de inicializar la variable afectada
        print("Numero invalido")
        doble = None
        divide = None
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        divide = None
    except Exception as e:
        # Captura cualquier error
        print("Error desconocido")
        print(type(e))

print("El doble es", doble, " y es entero")
print(f"El inverso es {divide} y es real")