# FIXME: EJERCICIOS CON DICCIONARIOS.
# Función para saber si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función principal
def contar_primos(matriz1, matriz2):
    # Unir las dos matrices en una sola lista de números
    todos_los_numeros = [num for fila in matriz1 for num in fila] + [num for fila in matriz2 for num in fila]

    # Crear un diccionario de primos
    primos = {}
    for numero in todos_los_numeros:
        if es_primo(numero):
            primos[numero] = primos.get(numero, 0) + 1

    return primos

# Ejemplo de uso
matriz1 = [
    [2, 4, 5],
    [7, 8, 9]
]

matriz2 = [
    [3, 5, 7],
    [11, 13, 4]
]

resultado = contar_primos(matriz1, matriz2)
print("Primos y sus frecuencias:", resultado)
