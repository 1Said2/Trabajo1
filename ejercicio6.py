import math
import time

def imprimir_matriz_int(matriz):
    # Imprime la matriz con tabulación entre elementos
    for fila in matriz:
        print("\t".join(map(str, fila)))
    print()

def rellenar_matriz(matriz, orden):
    # Calcula el límite máximo de números a rellenar en la matriz
    limite_maximo = (orden * orden + orden) // 2
    contador = 1

    for fila in range(0, orden, 2):
        # Rellena la fila actual de izquierda a derecha
        for columna in range(fila + 1):
            matriz[fila][columna] = contador
            contador += 1

        fila += 1

        # Rellena la siguiente fila de derecha a izquierda si no se ha alcanzado el límite
        if contador < limite_maximo:
            for columna in range(fila, -1, -1):
                matriz[fila][columna] = contador
                contador += 1

def main(tamanio=0):
    # Calcula el orden de la matriz basado en el tamaño
    orden = tamanio // 10

    # Inicializa la matriz con ceros
    matriz = [[0] * orden for _ in range(orden)]

    # Mide el tiempo de ejecución del relleno de la matriz
    inicio = time.time()
    rellenar_matriz(matriz, orden)
    fin = time.time()

    imprimir_matriz_int(matriz)

    return fin - inicio

if __name__ == "__main__":
    main()
