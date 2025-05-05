import string
from Genetics import run_genetic_algorithm
from aco import run_aco
from pso import run_pso

def main():
    while True:
        print("\n--- ALGORITMOS DE OPTIMIZACIÓN ---")
        print("1. Algoritmo Genético (evolución de string)")
        print("2. Colonia de Hormigas (optimización de rutas)")
        print("3. Enjambre de Partículas (minimizar función)")
        print("4. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            run_genetic_algorithm()
        elif choice == '2':
            run_aco()
        elif choice == '3':
            run_pso()
        elif choice == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == '__main__':
    main()
