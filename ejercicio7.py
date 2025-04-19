import random
import time
def invertir_matriz(matriz):
    longitud = len(matriz)
    #Tomar los elementos de la diagonal principal como pivote
    for pivote in range(longitud):
        columnas = longitud * 2 - 1
        #Dividir toda la fila para el pivote hasta que este sea 1
        while matriz[pivote][pivote] != 1:
            matriz[pivote][columnas] /= matriz[pivote][pivote]
            columnas -= 1
        #Volver ceros los elementos debajo del pivote
        for filas in range(pivote+1, longitud):
            columnas = longitud * 2 - 1
            while matriz[filas][pivote] != 0:
                matriz[filas][columnas] -= matriz[filas][pivote] * matriz[pivote][columnas]
                columnas -= 1
    #Hacer ceros los elementos encima del pivote
    for pivote in range(longitud-1, -1, -1):
        for filas in range(pivote-1, -1, -1):
            columnas = len(matriz) * 2 - 1
            while matriz[filas][pivote] != 0:
                matriz[filas][columnas] -= matriz[filas][pivote] * matriz[pivote][columnas]
                columnas -= 1
    return matriz

def generar_matriz_aleatoria(cantidad_elementos):
    return [[random.randint(0, 101) for _ in range(cantidad_elementos)] for _ in range(cantidad_elementos)]

def aumentar_matriz(matriz):
    longitud=len(matriz)
    matriz_identidad = [[1 if i == j else 0 for j in range(longitud)] for i in range(longitud)]
    return [fila_A + fila_I for fila_A, fila_I in zip(matriz, matriz_identidad)]

def desaumentar_matriz(matriz_aumentada):
    matriz_desaumentada = []

    for fila in matriz_aumentada:
        mitad = len(fila) // 2
        matriz_desaumentada.append(fila[mitad:])
    return matriz_desaumentada

def main(cantidad_de_datos=0):
    cantidad_de_datos//=10
    matriz = generar_matriz_aleatoria(cantidad_de_datos)
    print("Matriz original")
    for filas in matriz:
        print(*filas,sep="\t")
    #Aumentar la matriz [A|I] para aplciar metodo de Gauss-Jordan
    matriz_aumentada=aumentar_matriz(matriz)
    inicio = time.time()
    matriz_inversa = invertir_matriz(matriz_aumentada)
    fin=time.time()
    #Desaumentar la matriz [I | A⁻¹] para obtener A⁻¹
    matriz_desaumentada = desaumentar_matriz(matriz_inversa)
    print("Matriz invertida")
    for filas in matriz_desaumentada:
        print(*filas,sep="\t")
    return fin - inicio

if __name__ == "__main__":
    main()