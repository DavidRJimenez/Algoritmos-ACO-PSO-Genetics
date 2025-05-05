import random

class Particle:
    def __init__(self, dim, bounds):
        self.position = [random.uniform(*bounds) for _ in range(dim)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dim)]
        self.best_pos = list(self.position)
        self.best_score = float('inf')

    def update_velocity(self, global_best, w=0.5, c1=1, c2=2):
        for i in range(len(self.velocity)):
            r1 = random.random()
            r2 = random.random()
            cognitive = c1 * r1 * (self.best_pos[i] - self.position[i])
            social = c2 * r2 * (global_best[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + cognitive + social

    def update_position(self, bounds):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]
            self.position[i] = max(bounds[0], min(bounds[1], self.position[i]))

def sphere_function(x):
    return sum(i**2 for i in x)

def run_pso():
    dim = 2
    bounds = (-10, 10)
    num_particles = 30
    iterations = 100
    particles = [Particle(dim, bounds) for _ in range(num_particles)]
    global_best = [0] * dim
    global_score = float('inf')

    for _ in range(iterations):
        for p in particles:
            score = sphere_function(p.position)
            if score < p.best_score:
                p.best_score = score
                p.best_pos = list(p.position)
            if score < global_score:
                global_score = score
                global_best = list(p.position)

        for p in particles:
            p.update_velocity(global_best)
            p.update_position(bounds)

    print("Mejor posición encontrada:", global_best)
    print("Valor mínimo:", global_score)
