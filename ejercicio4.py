import random
import time

def generar_matriz_aleatoria(num_filas, num_columnas, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(num_columnas)] for _ in range(num_filas)]

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
    for paso, fila in enumerate(matriz):
        # Ordenar la fila para realizar la búsqueda binaria
        fila_ordenada = sorted(fila)
        indice_columna = busqueda_binaria_fila(fila_ordenada, objetivo)

        if indice_columna != -1:
            # Encontrar el índice original en la fila no ordenada
            indice_original = fila.index(fila_ordenada[indice_columna])
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