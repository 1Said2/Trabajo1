import math
import random
import time


def imprimir_matriz(matriz):
    for fila in matriz:
        print("\t".join(fila))
    print()


def rellenar_matriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            matriz[fila][columna] = chr(random.randint(65, 90))


def encontrar_palabra_random(tamanio_max = 0):
    tamanio_palabra = abs(random.randint(1, tamanio_max))
    palabra = ""
    for letra in range(tamanio_palabra):
        palabra += (chr(random.randint(65, 90)))
    return palabra


def encontrar_palabra(matriz, palabra):
    palabra_en_chars = list(palabra)
    contador = 0
    filas = len(matriz)
    columnas = len(matriz[0])

    direcciones = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1)
    ]

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == palabra_en_chars[0]:
                if len(palabra_en_chars) == 1:
                    print(f"({i},{j})")
                    contador += 1
                else:
                    for dx, dy in direcciones:
                        posiciones = []
                        encontrado = True
                        x, y = i, j
                        for k in range(len(palabra_en_chars)):
                            if 0 <= x < filas and 0 <= y < columnas and matriz[x][y] == palabra_en_chars[k]:
                                posiciones.append(f"({x},{y})")
                                x += dx
                                y += dy
                            else:
                                encontrado = False
                                break
                        if encontrado:
                            print("Encontrado en posiciones: " + "\t".join(posiciones))
                            contador += 1

    print(f"La palabra {palabra} se ha encontrado {contador} veces.")

def main(tamanio = 0):
    filas = int(math.sqrt(tamanio))
    columnas = int(math.sqrt(tamanio))
    print()

    matriz = [['' for _ in range(columnas)] for _ in range(filas)]

    rellenar_matriz(matriz)
    imprimir_matriz(matriz)

    palabra = encontrar_palabra_random(int(math.sqrt(tamanio))).upper()

    inicio = time.time()
    encontrar_palabra(matriz, palabra)
    fin = time.time()

    return fin - inicio

if __name__ == "__main__":
    main()
