import random

def generar_matriz_notas(num_estudiantes):

    matriz_notas = []
    for i in range(1, num_estudiantes + 1):
        nombre_estudiante = f"Estudiante {i}"
        nota1 = round(random.uniform(1, 10), 1)
        nota2 = round(random.uniform(1, 10), 1)
        nota3 = round(random.uniform(1, 10), 1)
        promedio = round((nota1 + nota2 + nota3) / 3, 1)

        if promedio >= 7:
            estado = "Aprobado"
        elif promedio >= 5:
            estado = "Supletorio"
        else:
            estado = "Reprobado"

        matriz_notas.append([nombre_estudiante, nota1, nota2, nota3, promedio, estado])
    return matriz_notas

def imprimir_matriz(matriz):
    print("------------------------------------------------------------------")
    print("{:<15} {:<8} {:<8} {:<8} {:<10} {:<10}".format("Estudiante", "Nota 1", "Nota 2", "Nota 3", "Promedio", "Estado"))
    print("------------------------------------------------------------------")
    for estudiante in matriz:
        print("{:<15} {:<8} {:<8} {:<8} {:<10} {:<10}".format(*estudiante))
    print("------------------------------------------------------------------")

def contar_estados(matriz):
    aprobados = 0
    supletorios = 0
    reprobados = 0
    for estudiante in matriz:
        if estudiante[5] == "Aprobado":
            aprobados += 1
        elif estudiante[5] == "Supletorio":
            supletorios += 1
        else:
            reprobados += 1
    return {"Aprobados": aprobados, "Supletorios": supletorios, "Reprobados": reprobados}

if __name__ == "__main__":
    try:
        num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
        if num_estudiantes <= 0:
            print("Por favor, ingrese un número de estudiantes válido (mayor que 0).")
        else:
            matriz_generada = generar_matriz_notas(num_estudiantes)
            imprimir_matriz(matriz_generada)
            conteo_estados = contar_estados(matriz_generada)
            print("\nConteo de estados:")
            for estado, cantidad in conteo_estados.items():
                print(f"{estado}: {cantidad}")
    except ValueError:
        print("Error: Por favor, ingrese un número entero para la cantidad de estudiantes.")

