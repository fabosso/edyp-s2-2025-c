def funcion_c(n):
    """Función más profunda: solo suma 10 a un número."""
    print("  -> Entrando en funcion_c")
    resultado = n + 10
    print(f"  <- Saliendo de funcion_c, devolviendo: {resultado}")
    return resultado

def funcion_b(x):
    """Función intermedia: multiplica su argumento y llama a funcion_c."""
    print(" -> Entrando en funcion_b")
    valor_para_c = x * 2
    resultado_de_c = funcion_c(valor_para_c)
    resultado_final = resultado_de_c + 5
    print(f" <- Saliendo de funcion_b, devolviendo: {resultado_final}")
    return resultado_final

def funcion_a():
    """Función principal que inicia la cadena de llamadas."""
    print("-> Entrando en funcion_a")
    valor_inicial = 10
    resultado_final = funcion_b(valor_inicial)
    print(f"Resultado final en funcion_a: {resultado_final}")
    print("<- Saliendo de funcion_a")

# --- Punto de entrada del programa ---
print("Iniciando el programa...")
funcion_a()
print("Programa finalizado.")