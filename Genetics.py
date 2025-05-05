import random
import numpy as np
import string
from matplotlib import pyplot as plt

class DNA(object):
    def __init__(self, size, genSet):
        self.genes = np.array(random.choices(genSet, k=size))
        self.fitness = 0

    def mutate(self, parentA, parentB, genSet, mutation_rate):
        newGenes = np.zeros(parentA.genes.shape[0], dtype=int)
        midPoint = random.randint(0, parentA.genes.shape[0])
        for ix in range(len(self.genes)):
            if random.random() < mutation_rate:
                newGenes[ix] = random.choice(genSet)
            else:
                newGenes[ix] = parentA.genes[ix] if ix < midPoint else parentB.genes[ix]
        self.genes = newGenes

class Population(object):
    def __init__(self, target, maxPop, genSet, mutation):
        self.genSet = np.array(list(map(ord, genSet)))
        self.target = np.array(list(map(ord, target)))
        self.maxPop = maxPop
        self.biggest = 0
        self.second = 0
        self.avg_fitness = 0
        self.mutation_rate = mutation
        self.pop = np.array([DNA(self.target.shape[0], self.genSet) for _ in range(maxPop)])

    def calculateFitness(self):
        self.biggest = 0
        self.second = 0
        self.avg_fitness = 0
        for ix in range(self.pop.shape[0]):
            self.pop[ix].fitness = (self.pop[ix].genes == self.target).sum()
            self.avg_fitness += float(self.pop[ix].fitness) / self.target.shape[0]
            if self.pop[ix].fitness > self.pop[self.biggest].fitness:
                self.second = self.biggest
                self.biggest = ix
            elif self.pop[ix].fitness > self.pop[self.second].fitness:
                self.second = ix
        self.avg_fitness = (self.avg_fitness / self.pop.shape[0]) * 100.0

    def nextGeneration(self):
        parentA = self.pop[self.biggest]
        parentB = self.pop[self.second]
        for ix in range(self.pop.shape[0]):
            child = DNA(parentA.genes.shape[0], self.genSet)
            child.mutate(parentA, parentB, self.genSet, self.mutation_rate)
            self.pop[ix] = child

    def evaluate(self):
        return not (self.pop[self.biggest].genes == self.target).all()

def run_genetic_algorithm():
    target = "To be or not to be."
    genSet = string.ascii_letters + string.punctuation + " " + string.digits
    maxPop = 500
    mutation = 0.01

    population = Population(target, maxPop, genSet, mutation)

    generations = []
    generation = 1
    while population.evaluate():
        population.calculateFitness()
        population.nextGeneration()
        generations.append(population.avg_fitness)
        print(f"Generacion: {generation} - Promedio fitness: {population.avg_fitness:.2f}%")
        print("Genes:", ''.join(map(lambda x: chr(int(x)), population.pop[population.biggest].genes)))
        generation += 1

    plt.plot(generations)
    plt.xlabel("Generacion")
    plt.ylabel("Promedio fitness")
    plt.title("Evolución Genética")
    plt.grid()
    plt.show()
