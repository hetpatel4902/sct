import random

def fitness(individual):
    x = int(individual, 2)
    return x**2

def binary(number):
    return "{0:b}".format(number).zfill(5)

def initial_population(population_size):
    return [binary(random.randint(0, 20)) for i in range(population_size)]

def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=fitness)

def single_point_crossover(individual1, individual2):
    crossover_point = random.randint(1, len(individual1)-1)
    offspring1 = individual1[:crossover_point] + individual2[crossover_point:]
    offspring2 = individual2[:crossover_point] + individual1[crossover_point:]
    return offspring1, offspring2

def bit_flip_mutation(individual, mutation_rate):
    mutated_individual = ""
    for bit in individual:
        mutated_bit = bit
        if random.uniform(0, 1) < mutation_rate:
            mutated_bit = "0" if bit == "1" else "1"
        mutated_individual += mutated_bit
    return mutated_individual

def genetic_algorithm(population_size, tournament_size, crossover_rate, mutation_rate, generations):
    population = initial_population(population_size)
    for i in range(generations):
        new_population = []
        while len(new_population) < population_size:
            # Selection
            parent1 = tournament_selection(population, tournament_size)
            parent2 = tournament_selection(population, tournament_size)
            # Crossover
            if random.uniform(0, 1) < crossover_rate:
                offspring1, offspring2 = single_point_crossover(parent1, parent2)
                # Mutation
                offspring1 = bit_flip_mutation(offspring1, mutation_rate)
                offspring2 = bit_flip_mutation(offspring2, mutation_rate)
                # Add offspring to new population
                new_population.append(offspring1)
                if len(new_population) < population_size:
                    new_population.append(offspring2)
        # Replace population with new population
        population = new_population
        best_individual = max(population, key=fitness)
        best_fitness = fitness(best_individual)
        print(f"Generation {i+1}: Best individual: {best_individual} Fitness: {best_fitness}")

genetic_algorithm(population_size=10, tournament_size=3, crossover_rate=0.8, mutation_rate=0.1, generations=5)
