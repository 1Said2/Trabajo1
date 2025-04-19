import random

# Función para crear la matriz
def crear_matriz():
    # Solicitar al usuario el número de filas y columnas
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    # Crear la matriz con números aleatorios entre 0 y 100
    matriz = [[random.randint(0, 100) for _ in range(columnas)] for _ in range(filas)]

    return matriz

def ordenar_matriz_por_insercion(matriz):
    # Imprimir la matriz original
    print("\nMatriz original:")
    for fila in matriz:
        print(fila)

    # Solicitar al usuario la fila que desea ordenar (índice basado en 0)
    fila_a_ordenar = int(input("\nIngrese el índice de la fila que desea ordenar (empieza desde 0): "))

    # Verificar que el índice de la fila sea válido
    if 0 <= fila_a_ordenar < len(matriz):
        # Algoritmo de ordenamiento por inserción
        for i in range(1, len(matriz[fila_a_ordenar])):
            clave = matriz[fila_a_ordenar][i]
            j = i - 1
            while j >= 0 and matriz[fila_a_ordenar][j] > clave:
                matriz[fila_a_ordenar][j + 1] = matriz[fila_a_ordenar][j]
                j -= 1
            matriz[fila_a_ordenar][j + 1] = clave

        # Imprimir la fila ordenada
        print(f"\nFila {fila_a_ordenar} ordenada:", matriz[fila_a_ordenar])
        # Imprimir la matriz después del ordenamiento
        print("\nMatriz después de ordenar la fila:")
        for fila in matriz:
            print(fila)

    else:
        print("Índice de fila fuera de rango.")

# Llamar a las funciones
matriz = crear_matriz()

ordenar_matriz_por_insercion(matriz)
