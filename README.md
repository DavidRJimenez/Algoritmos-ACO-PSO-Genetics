
# Algoritmos de Optimización: Genético, Enjambre de Partículas y Colonia de Hormigas

Este proyecto implementa tres algoritmos de optimización clásicos en Python, accesibles desde un menú interactivo:

1.  **Algoritmo Genético** — Converge hacia un string objetivo.
2.  **Optimización de Rutas con Colonia de Hormigas (ACO)** — Encuentra la ruta óptima entre ciudades.
3.  **Optimización con Enjambre de Partículas (PSO)** — Minimiza una función matemática (función esfera).

---

##  Estructura del proyecto
├── main.py # Menú principal para ejecutar los algoritmos
├── genetics.py # Implementación del algoritmo genético
├── aco.py # Implementación del algoritmo de colonia de hormigas
├── pso.py # Implementación del algoritmo de partículas
└── README.md # Este archivo


---

##  Cómo Ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Instala los requerimientos si no los tienes:

```bash
pip install numpy matplotlib

Resultados Esperados
 Algoritmo Genético

Evoluciona una población de cadenas de texto hasta igualar una frase objetivo.

    Objetivo: "To be or not to be."

    Salida: Progreso generacional con visualización de fitness promedio.

Ejemplo:
Generacion: 42 - Promedio fitness: 91.14%
Genes: To be,or not to be.

 Colonia de Hormigas (ACO)

Optimiza la ruta entre 5 ciudades generadas aleatoriamente usando feromonas y visibilidad.

Ejemplo:
Mejor ruta encontrada: [3, 1, 4, 2, 0, 3]
Distancia total: 213
Minimiza la función esfera f(x)=∑xi2f(x)=∑xi2​, buscando el punto más cercano al origen.

Ejemplo:
Mejor posición encontrada: [3.64e-12, 1.31e-12]
Valor mínimo: 1.50e-23


Requisitos

    Python 3.7 o superior

    numpy

    matplotlib

Instalación rápida:
pip install numpy matplotlib

Estudiantes:
David Ricardo Jimenez Nuñez
Cesar Martinez
Mateo Pissarello

