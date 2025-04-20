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


    '''
    Para fines de automatización se ordenara una fila aleatoria entre 0 y el número de filas
    que tenga la matriz, pero se puede ingresar un input en la variable para que el usuario
    ingrese la fila a ordenar
    '''
    fila_a_ordenar = random.randint(0, (len(matriz)-1))

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
