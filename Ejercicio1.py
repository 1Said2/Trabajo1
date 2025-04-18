import random
import math

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

# Generar elementos aleatorios y contar los números primos
elementos = 10  
arreglo = [random.randint(1, 100) for _ in range(elementos)]
cantidad_primos = sum(1 for num in arreglo if es_primo(num))

print("Arreglo generado:", arreglo)
print("Cantidad de números primos:", cantidad_primos)
