def generar_matriz(longitud):
    array = [[0]*longitud for _ in range(longitud)]
    iterador=1
    for columnas in range(longitud):
        for filas in range(longitud - 1, columnas - 1, -1):
            array[filas][columnas+longitud-1-filas]=iterador
            iterador+=1
    for filas in range(longitud-2,-1,-1):
        for columnas in range(filas+1):
            array[filas-columnas][columnas]=iterador
            iterador+=1
    return array
matriz = generar_matriz(3)
for ñ in matriz:
    print(*ñ,sep="\t")