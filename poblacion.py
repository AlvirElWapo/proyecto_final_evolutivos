import random

# Constants for the problem
NUM_TASKS = 37
NUM_INDIVIDUALS = 50

# Function to initialize a random individual with values and weights
def initialize_individual():
    return [
        {
            'tarea': i,
            'servidor': random.choice(['ServidorExterno', 'ServidorEmpleados']),
            'valor': random.uniform(1, 10),  # Example value for the task
            'peso': random.uniform(0.1, 1.0),  # Example weight for the task
        }
        for i in range(NUM_TASKS)
    ]

# Function to initialize a population
def initialize_population():
    return [initialize_individual() for _ in range(NUM_INDIVIDUALS)]

# Example of how to use the initialized population
population = initialize_population()
print(population)
