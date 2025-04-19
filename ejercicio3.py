import random
import time


def generar_arreglo_y_busqueda(cantidad_de_datos):
        # Tamano del arreglo
        tamanio_arreglo = cantidad_de_datos
        if tamanio_arreglo <= 0:
            print("El tamaño debe ser un número entero positivo.")
            return

        # Generar el arreglo de numeros aleatorios
        arreglo_aleatorio = [random.randint(0, 100) for _ in range(tamanio_arreglo)]

        print("\nArreglo original (sin ordenar):")
        print(arreglo_aleatorio)

        # Solicitar el elemento a buscar
        elemento_a_buscar = random.randint(0,100)

        # Ordenar el arreglo para la busqueda binaria
        arreglo_ordenado = sorted(arreglo_aleatorio)

        # Imprimir el arreglo ordenado
        print("\nArreglo ordenado:")
        print(arreglo_ordenado)

        # Aplicamos la búsqueda binaria
        resultados = busqueda_binaria(arreglo_ordenado, elemento_a_buscar)

        if resultados:
            print(f"\nEl elemento {elemento_a_buscar} se encuentra en las siguientes posiciones: {resultados}")
        else:
            print(f"\nEl elemento {elemento_a_buscar} no se encuentra en el arreglo.")

# Aplicamos la busqueda binaria
def busqueda_binaria(arreglo_ordenado, elemento_a_buscar):
    izquierda, derecha = 0, len(arreglo_ordenado) - 1
    posiciones = []

    while izquierda <= derecha:
        mitad = izquierda + (derecha - izquierda) // 2

        # Si encontramos el objetivo, empezamos a buscar en ambas direcciones
        if arreglo_ordenado[mitad] == elemento_a_buscar:
            # Buscar hacia la izquierda
            i = mitad
            while i >= 0 and arreglo_ordenado[i] == elemento_a_buscar:
                posiciones.append(i)
                i -= 1

            # Buscar hacia la derecha
            i = mitad + 1
            while i < len(arreglo_ordenado) and arreglo_ordenado[i] == elemento_a_buscar:
                posiciones.append(i)
                i += 1

            break
        elif arreglo_ordenado[mitad] < elemento_a_buscar:
            izquierda = mitad + 1
        else:
            derecha = mitad - 1
    return sorted(posiciones)

# Ejecutar la funcion principal
def main(cantidad_de_datos=0):
    inicio = time.time()
    generar_arreglo_y_busqueda(cantidad_de_datos)
    fin=time.time()
    return fin - inicio
if __name__ == "__main__":
    main()