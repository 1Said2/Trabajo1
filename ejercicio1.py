import random
import math
import time
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True
def main(cantidad_de_datos=0):
    arreglo = [random.randint(1, 100) for _ in range(cantidad_de_datos)]
    inicio = time.time()
    cantidad_primos = sum(1 for num in arreglo if es_primo(num))

    print("Arreglo generado:", *arreglo)
    print("Cantidad de números primos:", cantidad_primos)
    return time.time() - inicio
if __name__ == "__main__":
    main()