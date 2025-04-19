import random
import time

def generar_matriz_aleatoria(num_filas, num_columnas, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(num_columnas)] for _ in range(num_filas)]


def busqueda_binaria_fila(fila, objetivo):
    indices = []
    izquierda, derecha = 0, len(fila) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if fila[medio] == objetivo:
            # Buscar hacia la izquierda y derecha para encontrar todas las ocurrencias
            i = medio
            while i >= 0 and fila[i] == objetivo:
                indices.append(i)
                i -= 1
            i = medio + 1
            while i < len(fila) and fila[i] == objetivo:
                indices.append(i)
                i += 1
            break
        elif fila[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return sorted(indices)


def encontrar_posiciones_elemento(matriz, objetivo):
    posiciones = []
    for paso, fila in enumerate(matriz):
        # Ordenar la fila para realizar la búsqueda binaria
        fila_ordenada = sorted((valor, idx) for idx, valor in enumerate(fila))
        valores_ordenados = [valor for valor, _ in fila_ordenada]
        indices_columnas = busqueda_binaria_fila(valores_ordenados, objetivo)

        for indice_columna in indices_columnas:
            # Encontrar el índice original en la fila no ordenada
            _, indice_original = fila_ordenada[indice_columna]
            posiciones.append((paso, indice_original))

    return posiciones


def main(cantidad_de_datos=0):
    try:
        objetivo = int(input("Ingrese el número a buscar: "))

        matriz = generar_matriz_aleatoria(cantidad_de_datos, cantidad_de_datos)
        print("Matriz Generada:")
        for fila in matriz:
            print(fila)
        
        inicio = time.time()
        
        posiciones = encontrar_posiciones_elemento(matriz, objetivo)
        if posiciones:
            print(f"El número {objetivo} se encuentra en las posiciones: {posiciones}")
        else:
            print(f"El número {objetivo} no se encuentra en la matriz.")
            
        return time.time() - inicio
    
    except ValueError:
        print("Entrada inválida. Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
    main()