import random
import string

# TARGET = "methinks it is like a weasel"
CHARS = string.ascii_lowercase + " "
POP_SIZE = 100
MUTATION_RATE = 0.05
MAX_GENERATIONS = 10000

def random_string(length):
    return ''.join(random.choice(CHARS) for _ in range(length))

def score(candidate):
    return sum(c == t for c, t in zip(candidate, TARGET))

def mutate(parent):
    # Randomly mutate each character with probability MUTATION_RATE
    return ''.join(
        c if random.random() > MUTATION_RATE else random.choice(CHARS)
        for c in parent
    )

def crossover(parent1, parent2):
    # Single-point crossover
    point = random.randint(0, len(TARGET) - 1)
    return parent1[:point] + parent2[point:]

def select(population):
    # Tournament selection: pick two random, return the better
    a, b = random.sample(population, 2)
    return a if score(a) > score(b) else b

def genetic_algorithm():
    population = [random_string(len(TARGET)) for _ in range(POP_SIZE)]
    best = max(population, key=score)
    best_score = score(best)

    for generation in range(1, MAX_GENERATIONS + 1):
        new_population = []
        for _ in range(POP_SIZE):
            parent1 = select(population)
            parent2 = select(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
        current_best = max(population, key=score)
        current_score = score(current_best)
        if current_score > best_score:
            best = current_best
            best_score = current_score
        if generation % 100 == 0 or best_score == len(TARGET):
            print(f"Generation {generation}: Best='{best}' Score={best_score}/{len(TARGET)}")
        if best_score == len(TARGET):
            print(f"Target reached in {generation} generations!")
            break

if __name__ == "__main__":
    genetic_algorithm()