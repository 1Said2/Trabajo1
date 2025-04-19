import time
def generar_matriz(dimension):
    array = [[0] * dimension for _ in range(dimension)]
    iterador=1
    for columnas in range(dimension):
        for filas in range(dimension - 1, columnas - 1, -1):
            array[filas][columnas + dimension - 1 - filas]=iterador
            iterador+=1
    for filas in range(dimension - 2, -1, -1):
        for columnas in range(filas+1):
            array[filas-columnas][columnas]=iterador
            iterador+=1
    return array
def main(dimension=0):
    inicio=time.time()
    matriz=generar_matriz(dimension)
    fin=time.time()
    for fila in matriz:
        print(*fila,sep="\t")
    return fin-inicio
if __name__ == "__main__":
    main()