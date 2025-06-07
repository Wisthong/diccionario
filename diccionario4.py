def diccionario_pares_por_fila(matriz):
    resultado = {}
    for i, fila in enumerate(matriz):
        pares = [num for num in fila if num % 2 == 0]
        resultado[i] = pares
    return resultado


# Ejemplo de uso
matriz = [[1, 2, 3, 4], [5, 7, 6, 8, 18], [9, 10, 11, 13, 14], [15, 16, 17]]


def mayor_par_y_su_clave(diccionario):
    mayor = None
    clave_mayor = None

    for clave, lista in diccionario.items():
        for num in lista:
            if (mayor is None) or (num > mayor):
                mayor = num
                clave_mayor = clave

    return mayor, clave_mayor


resultado = diccionario_pares_por_fila(matriz)
print("Diccionario de pares por fila:", resultado)

mayor, clave = mayor_par_y_su_clave(resultado)
print(f"El mayor número par es {mayor} y se encuentra en la clave {clave}")
