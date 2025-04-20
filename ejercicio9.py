import random
import time
from contextlib import nullcontext


# Función para crear la matriz
def crear_matriz(cantidad_de_elementos):
    division = cantidad_de_elementos // 2
    filas = division
    columnas = division + 2 #Se suma dos elementos para mantener la relación de n x m

    # Crear la matriz con números aleatorios entre 0 y 100
    matriz = [[random.randint(0, 100) for _ in range(columnas)] for _ in range(filas)]

    return matriz

def ordenar_matriz_por_insercion(matriz, fila_a_ordenar):
    # Verificar que el índice de la fila sea válido
    if 0 <= fila_a_ordenar < len(matriz):
        # Algoritmo de ordenamiento por inserción
        for indice_actual in range(1, len(matriz[fila_a_ordenar])):
            clave = matriz[fila_a_ordenar][indice_actual]
            indice_de_comparacion = indice_actual - 1
            while indice_de_comparacion >= 0 and matriz[fila_a_ordenar][indice_de_comparacion] > clave:
                matriz[fila_a_ordenar][indice_de_comparacion + 1] = matriz[fila_a_ordenar][indice_de_comparacion]
                indice_de_comparacion -= 1
            matriz[fila_a_ordenar][indice_de_comparacion + 1] = clave
        return matriz
    else:
        return "Índice de fila fuera de los límites de la matriz"


def main(cantidad_de_datos=0):
    matriz_sin_ordenar = crear_matriz(cantidad_de_datos)
    # Imprimir la matriz original
    print("\nMatriz original:")
    for fila in matriz_sin_ordenar:
        print(fila)

    '''
    Para fines de automatización se ordenara una fila aleatoria entre 0 y el número de filas
    que tenga la matriz, pero se puede ingresar un input en la variable para que el usuario
    ingrese la fila a ordenar
    '''
    fila_a_ordenar = random.randint(0, (len(matriz_sin_ordenar)-1))

    # Se mide el tiempo unicamente del algoritmo de ordenamiento
    inicio = time.time()
    matriz_ordenada = ordenar_matriz_por_insercion(matriz_sin_ordenar, fila_a_ordenar)
    fin=time.time()

    # Comprobar si la matriz fue ordenada o no
    if isinstance(matriz_ordenada, str):  # Si el resultado es un mensaje
        print(matriz_ordenada)  # Imprime el mensaje de error
    else:
        # Imprimir la fila ordenada
        print(f"\nFila {fila_a_ordenar} ordenada:", matriz_ordenada[fila_a_ordenar])
        # Imprimir la matriz después del ordenamiento
        print("\nMatriz después de ordenar la fila:")
        for fila in matriz_ordenada:
            print(fila)

    return fin - inicio
if __name__ == "__main__":
    main()
