import math
import time


def imprimir_matriz_int(matriz):
    for fila in matriz:
        print("\t".join(map(str, fila)))
    print()


def rellenar_matriz(matriz, orden):
    limite_maximo = (orden * orden + orden) // 2
    contador = 1

    for fila in range(0, orden, 2):
        for columna in range(fila + 1):
            matriz[fila][columna] = contador
            contador += 1

        fila += 1

        if contador < limite_maximo:
            for columna in range(fila, -1, -1):
                matriz[fila][columna] = contador
                contador += 1


def main(tamanio = 0):
    orden = tamanio//10

    matriz = [[0] * orden for _ in range(orden)]

    inicio = time.time()
    rellenar_matriz(matriz, orden)
    fin = time.time()

    imprimir_matriz_int(matriz)

    return fin - inicio


if __name__ == "__main__":
    main()
