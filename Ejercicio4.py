import random

def generar_matriz_aleatoria(n, m, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]

def busqueda_binaria_fila(fila, objetivo):
    izquierda, derecha = 0, len(fila) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if fila[medio] == objetivo:
            return medio
        elif fila[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def encontrar_posiciones_elemento(matriz, objetivo):
    posiciones = []
    for i, fila in enumerate(matriz):
        # Ordenar la fila para realizar la búsqueda binaria
        fila_ordenada = sorted(fila)
        indice_columna = busqueda_binaria_fila(fila_ordenada, objetivo)
        if indice_columna != -1:
            # Encontrar el índice original en la fila no ordenada
            indice_original = fila.index(fila_ordenada[indice_columna])
            posiciones.append((i, indice_original))
    return posiciones

def main():
    try:
        n = int(input("Ingrese el número de filas (n): "))
        m = int(input("Ingrese el número de columnas (m): "))
        objetivo = int(input("Ingrese el número a buscar: "))

        matriz = generar_matriz_aleatoria(n, m)
        print("Matriz Generada:")
        for fila in matriz:
            print(fila)

        posiciones = encontrar_posiciones_elemento(matriz, objetivo)
        if posiciones:
            print(f"El número {objetivo} se encuentra en las posiciones: {posiciones}")
        else:
            print(f"El número {objetivo} no se encuentra en la matriz.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
    main()