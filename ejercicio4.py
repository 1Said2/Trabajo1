import random
import time

def generar_matriz_aleatoria(num_filas, num_columnas, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(num_columnas)] for _ in range(num_filas)]


def busqueda_matriz_ordenada(matriz, objetivo):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultados = []

    # Búsqueda binaria para encontrar cualquier aparición
    izquierda, derecha = 0, filas * columnas - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        fila = medio // columnas
        columna = medio % columnas
        if matriz[fila][columna] == objetivo:
            while fila < filas and matriz[fila][columna] == objetivo:
                resultados.append([fila, columna])
                columna = (columna + 1) % columnas
                if columna == 0:
                    fila += 1
            fila, columna = resultados[0][0], resultados[0][1]
            columna = (columna - 1) % columnas
            if columna == columnas - 1:
                fila -= 1
            while fila >= 0 and matriz[fila][columna] == objetivo:
                resultados.append([fila, columna])
                columna = (columna - 1) % columnas
                if columna == columnas - 1:
                    fila -= 1
            return sorted(resultados)
        if matriz[fila][columna] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1


def main(cantidad_de_datos=0):
    try:

        matriz = generar_matriz_aleatoria(cantidad_de_datos, cantidad_de_datos)
        lista_ordenada = sorted([num for fila in matriz for num in fila])
        filas = len(matriz)
        columnas = len(matriz[0])
        matriz_ordenada = [lista_ordenada[i * columnas: (i + 1) * columnas] for i in range(filas)]
        print("Matriz Generada:")
        for fila in matriz_ordenada:
            print(fila)
        objetivo = random.randint(0, 100)
        inicio = time.time()
        
        posiciones = busqueda_matriz_ordenada(matriz_ordenada, objetivo)

        fin = time.time()
        if posiciones:
            print(f"El número {objetivo} se encuentra en las posiciones: {posiciones}")
        else:
            print(f"El número {objetivo} no se encuentra en la matriz.")
            
        return fin - inicio
    
    except ValueError:
        print("Entrada inválida. Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
    main()