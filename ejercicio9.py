import random
import time

# Función para crear la matriz
def crear_matriz(cantidad_de_elementos):
    division = cantidad_de_elementos // 2
    filas = division
    columnas = division + 2

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

# Ejecutar la funcion principal
def main(cantidad_de_datos=0):
    inicio = time.time()
    ordenar_matriz_por_insercion(crear_matriz(cantidad_de_datos))
    fin=time.time()
    return fin - inicio
if __name__ == "__main__":
    main()
