import random

# Generar dos arreglos A y B con números aleatorios positivos
numelementos = 10  
A = [random.randint(1, 100) for _ in range(numelementos)]
B = [random.randint(1, 100) for _ in range(numelementos)]

elementos_A_y_en_B = []
for elemento_A in A:
    if elemento_A in B and elemento_A not in elementos_A_y_en_B:
        elementos_A_y_en_B.append(elemento_A)

print("Arreglo A:", A)
print("Arreglo B:", B)
print("Elementos de A que están en B:", elementos_A_y_en_B)
