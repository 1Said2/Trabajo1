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
    filas = len(matriz)
    columnas = len(matriz[0])
    izquierda = 0
    derecha = filas * columnas - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        fila = medio // columnas
        columna = medio % columnas
        valor = matriz[fila][columna]

        if valor == objetivo:
            return fila, columna
        elif valor < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return False

def main():
    try:
        n = int(input("Ingrese el número de filas (n): "))
        m = int(input("Ingrese el número de columnas (m): "))

        matriz = generar_matriz_aleatoria(n, m)
        print("Matriz Generada:")
        plana_ordenada = sorted([elem for fila in matriz for elem in fila])

        columnas = len(matriz[0])
        matriz_ordenada = [plana_ordenada[i:i + columnas] for i in range(0, len(plana_ordenada), columnas)]
        for fila in matriz_ordenada:
            print(*fila,sep="\t")
        objetivo = int(input("Ingrese el número a buscar: "))

        posiciones = encontrar_posiciones_elemento(matriz_ordenada, objetivo)
        if posiciones:
            print(f"El número {objetivo} se encuentra en las posiciones: {posiciones}")
        else:
            print(f"El número {objetivo} no se encuentra en la matriz.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
    main()