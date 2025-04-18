import random

# Generar dos arreglos A y B con números aleatorios positivos
numelementos = 10  
A = [random.randint(1, 100) for _ in range(numelementos)]
B = [random.randint(1, 100) for _ in range(numelementos)]

# Encontrar los elementos de A que están en B y los de B que están en A
elementos_A_en_B = set(A) & set(B)
elementos_B_en_A = set(B) & set(A)


print("Arreglo A:", A)
print("Arreglo B:", B)
print("Elementos de A que están en B:", list(elementos_A_en_B))
print("Elementos de B que están en A:", list(elementos_B_en_A))

