import numpy as np
import random

class Ant:
    def __init__(self, num_cities):
        self.tour = []
        self.distance = 0
        self.num_cities = num_cities

    def visit(self, city, distance_matrix):
        if self.tour:
            self.distance += distance_matrix[self.tour[-1]][city]
        self.tour.append(city)

    def reset(self):
        self.tour = []
        self.distance = 0

def run_aco():
    cities = 5
    distance_matrix = np.random.randint(10, 100, size=(cities, cities))
    np.fill_diagonal(distance_matrix, 0)
    num_ants = 10
    iterations = 50
    decay = 0.5
    alpha = 1
    beta = 2
    pheromone = np.ones((cities, cities))
    best_tour = None
    best_distance = float('inf')

    for _ in range(iterations):
        all_ants = []
        for _ in range(num_ants):
            ant = Ant(cities)
            unvisited = list(range(cities))
            current = random.choice(unvisited)
            ant.visit(current, distance_matrix)
            unvisited.remove(current)

            while unvisited:
                probs = []
                for city in unvisited:
                    tau = pheromone[current][city] ** alpha
                    eta = (1 / distance_matrix[current][city]) ** beta
                    probs.append(tau * eta)
                probs = probs / np.sum(probs)
                next_city = random.choices(unvisited, weights=probs)[0]
                ant.visit(next_city, distance_matrix)
                unvisited.remove(next_city)
                current = next_city

            ant.distance += distance_matrix[ant.tour[-1]][ant.tour[0]]
            if ant.distance < best_distance:
                best_distance = ant.distance
                best_tour = ant.tour
            all_ants.append(ant)

        pheromone *= decay
        for ant in all_ants:
            for i in range(len(ant.tour)):
                a, b = ant.tour[i], ant.tour[(i+1)%cities]
                pheromone[a][b] += 1.0 / ant.distance

    print("Mejor ruta encontrada:", best_tour + [best_tour[0]])
    print("Distancia total:", best_distance)
