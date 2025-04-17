import random
def invertir(matriz):
    m = len(matriz)
    for k in range(m):
        j = m * 2 - 1
        while matriz[k][k] != 1:
            matriz[k][j] /= matriz[k][k]
            j -= 1
        for i in range(k+1, m):
            j = m * 2 - 1
            while matriz[i][k] != 0:
                matriz[i][j] -= matriz[i][k] * matriz[k][j]
                j -= 1
    for k in range(m-1, -1, -1):
        for i in range(k-1, -1, -1):
            j = len(matriz) * 2 - 1
            while matriz[i][k] != 0:
                matriz[i][j] -= matriz[i][k] * matriz[k][j]
                j -= 1
    return matriz
def generar_matriz_aleatoria(n):
    return [[random.randint(0, 101) for _ in range(n)] for _ in range(n)]

def matriz_aumentada(A):
    n=len(A)
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return [fila_A + fila_I for fila_A, fila_I in zip(A, I)]
def desaumentar_matriz(matriz_aumentada):
    A = []
    for fila in matriz_aumentada:
        mitad = len(fila) // 2
        A.append(fila[mitad:])
    return A
def start(n):
    inversa=desaumentar_matriz(invertir(matriz_aumentada([[1,2,3],[0,1,4],[5,6,0]])))
    for i in inversa:
        print(*i,sep="\t")
start(2)
