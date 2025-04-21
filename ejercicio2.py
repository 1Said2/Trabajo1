import random, time

def main(cantidad_elementos=0):
    arreglo_A = [random.randint(1, 100) for _ in range(cantidad_elementos)]
    arreglo_B = [random.randint(1, 100) for _ in range(cantidad_elementos)]

    elementos_A_y_en_B = []
    inicio = time.time()
    for elemento_A in arreglo_A:
        if elemento_A in arreglo_B and elemento_A not in elementos_A_y_en_B:
            elementos_A_y_en_B.append(elemento_A)
    fin = time.time()
    print("Arreglo A:", arreglo_A)
    print("Arreglo B:", arreglo_B)
    print("Elementos comunes de A y B:", elementos_A_y_en_B)
    return fin - inicio