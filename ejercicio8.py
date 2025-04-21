import math
import random
import time


def imprimir_matriz(matriz):
    for fila in matriz:
        print("\t".join(fila))
    print()

#Rellenar matriz con letras a traves de sus valores obtenidos del ascii
def rellenar_matriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            matriz[fila][columna] = chr(random.randint(65, 90))

#Generar una palabra o letra al azar para buscar en la sopa de letras
def generar_palabra_random(tamanio_max = 0):
    tamanio_palabra = abs(random.randint(1, tamanio_max))
    palabra = ""
    for letra in range(tamanio_palabra):
        palabra += (chr(random.randint(65, 90)))
    return palabra


def encontrar_palabra(matriz, palabra):
    palabra_en_chars = list(palabra)
    ocurrencias = 0
    filas = len(matriz)
    columnas = len(matriz[0])
    # Definir las 8 direcciones posibles para buscar (diagonal, horizontal, vertical)
    direcciones = [
        (-1, -1),  # Diagonal superior izquierda
        (-1, 0),  # Arriba
        (-1, 1),  # Diagonal superior derecha
        (0, 1),  # Derecha
        (1, 1),  # Diagonal inferior derecha
        (1, 0),  # Abajo
        (1, -1),  # Diagonal inferior izquierda
        (0, -1)  # Izquierda
    ]

    for fila_actual in range(filas):
        for columna_actual in range(columnas):
            # Si el primer carácter coincide, explorar posibles coincidencias
            if matriz[fila_actual][columna_actual] == palabra_en_chars[0]:
                if len(palabra_en_chars) == 1:
                    print(f"({fila_actual},{columna_actual})")
                    ocurrencias += 1
                else:
                    for desplazamiento_horizontal, desplazamiento_vertical in direcciones:
                        posiciones = []
                        encontrado = True
                        fila_buscar, columna_buscar = fila_actual, columna_actual

                        for indice_caracter in range(len(palabra_en_chars)):
                            # Verificar que la posición esté dentro de la matriz y el carácter coincida
                            if 0 <= fila_buscar < filas and 0 <= columna_buscar < columnas and matriz[fila_buscar][columna_buscar] == palabra_en_chars[indice_caracter]:
                                posiciones.append(f"({fila_buscar},{columna_buscar})")
                                # Moverse a la siguiente posición en la dirección actual
                                fila_buscar += desplazamiento_horizontal
                                columna_buscar += desplazamiento_vertical
                            else:
                                # Si no coincide, dejar de buscar en esta dirección
                                encontrado = False
                                break
                        if encontrado:
                            print("Encontrado en posiciones: " + "\t".join(posiciones))
                            ocurrencias += 1

    print(f"La palabra {palabra} se ha encontrado {ocurrencias} veces.")

def main(tamanio = 0):
    filas = int(math.sqrt(tamanio))
    columnas = int(math.sqrt(tamanio))
    print()

    matriz = [['' for _ in range(columnas)] for _ in range(filas)]

    rellenar_matriz(matriz)
    imprimir_matriz(matriz)

    palabra = generar_palabra_random(int(math.sqrt(tamanio))).upper()

    inicio = time.time()
    encontrar_palabra(matriz, palabra)
    fin = time.time()

    return fin - inicio

if __name__ == "__main__":
    main()
