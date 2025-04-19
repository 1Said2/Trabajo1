'''
Integrantes:
Said Cotacachi
Daniel Carranco
Diego Montesdeoca
Gisella Salgado
Kevin Arteaga
'''''

import importlib
import matplotlib.pyplot as plt
from tabulate import tabulate

def ejecutar_ejercicio(numero_ejercicio, parametro):
    try:
        modulo = importlib.import_module(f"ejercicio{numero_ejercicio}")
        tiempo = modulo.main(parametro)
        return float(tiempo)
    except ImportError:
        print(f"\n❌ Error: Archivo 'ejercicio{numero_ejercicio}.py' no encontrado.")
        return None
    except Exception as e:
        print(f"\n❌ Error en ejercicio{numero_ejercicio}.py: {str(e)}")
        return None

def mostrar_menu():
    print("\n" + "=" * 30)
    print("  MENÚ DE EJERCICIOS")
    print("=" * 30)
    for i in range(1, 11):
        print(f"  {i}. Ejercicio {i}")
    print("  0. Salir")

def generar_reporte(ejercicio, tiempos):
    print("\n📊 RESULTADOS:")
    tabla = [[param, f"{tiempo:.6f}s"] for param, tiempo in zip(range(1, 11), tiempos)]
    print(tabulate(tabla, headers=["Iteraciones", "Tiempo (s)"], tablefmt="grid"))

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, 11), tiempos, 'o-', color='blue', label=f"Ejercicio {ejercicio}")
    plt.title(f"⏱️ Tiempos de Ejecución (Ejercicio {ejercicio})")
    plt.xlabel("Iteraciones")
    plt.ylabel("Tiempo (segundos)")
    plt.xticks(range(1, 11))
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\n👉 Seleccione un ejercicio (0-10): ").strip()

        if opcion == "0":
            print("\n¡Hasta luego! 👋")
            break

        if opcion.isdigit() and 1 <= int(opcion) <= 10:
            ejercicio = int(opcion)
            tiempos = []
            print(f"\n🔍 Ejecutando Ejercicio {ejercicio}...")
            for cantidad_elementos in range(10, 101, 10):
                print(f"Iteracion: {cantidad_elementos//10}")
                tiempo = ejecutar_ejercicio(ejercicio, cantidad_elementos)
                tiempos.append(tiempo)
                print()


            if tiempos:
                generar_reporte(ejercicio, tiempos)
        else:
            print("\n⚠️ Error: Ingrese un número del 1 al 10.")
