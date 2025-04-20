import random
import time

def crear_arreglo(cantidad_de_datos):
    #Tamaño del arrelgo
    tamanio_arreglo = cantidad_de_datos
    if tamanio_arreglo <= 0:
        print("El tamaño debe ser un número entero positivo.")
        return
    # Generar el arreglo de numeros aleatorios
    arreglo_aleatorio = [random.randint(0, 35) for _ in range(tamanio_arreglo)]
    return arreglo_aleatorio

# Metodo de busqueda binaria
def busqueda_binaria(arreglo_ordenado, elemento_a_buscar):
    izquierda, derecha = 0, len(arreglo_ordenado) - 1
    posiciones = []

    while izquierda <= derecha:
        mitad = izquierda + (derecha - izquierda) // 2

        # Si encontramos el objetivo, empezamos a buscar en ambas direcciones
        if arreglo_ordenado[mitad] == elemento_a_buscar:
            # Buscar hacia la izquierda
            indice_izquierda = mitad
            while indice_izquierda >= 0 and arreglo_ordenado[indice_izquierda] == elemento_a_buscar:
                posiciones.append(indice_izquierda)
                indice_izquierda -= 1

            # Buscar hacia la derecha
            indice_derecha = mitad + 1
            while indice_derecha < len(arreglo_ordenado) and arreglo_ordenado[indice_derecha] == elemento_a_buscar:
                posiciones.append(indice_derecha)
                indice_derecha += 1

            break
        elif arreglo_ordenado[mitad] < elemento_a_buscar:
            izquierda = mitad + 1
        else:
            derecha = mitad - 1
    return sorted(posiciones)


def main(cantidad_de_datos=0):
    arreglo_sin_ordenar = crear_arreglo(cantidad_de_datos)
    print("\nArreglo original (sin ordenar):")
    print(arreglo_sin_ordenar)

    '''
    Solicitar el elemento a buscar
    Para fines de automatización se le solicita al sistema que busque un numero aleatorio
    entre el 0 y 100, pero se puede ingresar los datos manualmente con un input
    '''
    elemento_a_buscar = random.randint(0, 35)

    # Ordenar el arreglo para la busqueda binaria
    arreglo_ordenado = sorted(arreglo_sin_ordenar)

    # Imprimir el arreglo ordenado
    print("\nArreglo ordenado:")
    print(arreglo_ordenado)

    #Se mide el tiempo unicamente del algoritmo de busqueda
    inicio = time.time()
    resultados = busqueda_binaria(arreglo_ordenado, elemento_a_buscar)
    fin = time.time()

    #Se imprime los resultados finales
    if resultados:
        print(f"\nEl elemento {elemento_a_buscar} se encuentra en las siguientes posiciones: {resultados}")
    else:
        print(f"\nEl elemento {elemento_a_buscar} no se encuentra en el arreglo.")

    return fin - inicio
if __name__ == "__main__":
    main()