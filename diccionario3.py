import math

# Función para generar números Fibonacci hasta cierto valor
def generar_fibonacci(hasta):
    fib = [0, 1]
    while fib[-1] + fib[-2] <= hasta:
        fib.append(fib[-1] + fib[-2])
    return set(fib)

# Función principal
def fibonacci_factoriales(lista1, lista2):
    # Unimos ambas listas
    numeros = set(lista1 + lista2)

    # Generamos Fibonacci hasta el máximo número
    fibs = generar_fibonacci(max(numeros))

    # Creamos diccionario
    resultado = {n: math.factorial(n) for n in numeros if n in fibs}
    return resultado

# Ejemplo de uso
lista1 = [3, 5, 9, 13]
lista2 = [1, 8, 21, 4]

resultado = fibonacci_factoriales(lista1, lista2)
print("Diccionario de Fibonacci y factorial:", resultado)
