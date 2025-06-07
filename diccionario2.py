# Función para generar números Fibonacci hasta un máximo
def generar_fibonacci(hasta):
    fib = [0, 1]
    while fib[-1] + fib[-2] <= hasta:
        fib.append(fib[-1] + fib[-2])
    return set(fib)  # Usamos set para búsqueda rápida

# Función principal
def vecinos_fibonacci(lista):
    if not lista:
        return {}

    fib_set = generar_fibonacci(max(lista))
    resultado = {}

    for i in range(len(lista)):
        actual = lista[i]
        if actual in fib_set:
            anterior = lista[i - 1] if i > 0 else None
            siguiente = lista[i + 1] if i < len(lista) - 1 else None
            resultado[actual] = (anterior, siguiente)

    return resultado

# Ejemplo de uso
lista = [4, 1, 3, 8, 5, 2, 13, 21, 7]
resultado = vecinos_fibonacci(lista)
print("Diccionario de Fibonacci con vecinos:", resultado)
