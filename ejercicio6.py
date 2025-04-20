import math


def imprimir_matriz_int(matriz):
    for fila in matriz:
        print("\t".join(map(str, fila)))
    print()


def main(tamanio = 0):
    orden = int(math.sqrt(tamanio))

    matriz = [[0] * orden for _ in range(orden)]

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

    imprimir_matriz_int(matriz)


if __name__ == "__main__":
    main()
