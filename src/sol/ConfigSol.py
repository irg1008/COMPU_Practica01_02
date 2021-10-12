import random
from deap import base, creator, tools

def config_population(config): 
		F, N, _, _ = config

		toolbox = base.Toolbox()

		creator.create("FitnessMax", base.Fitness, weights=(1.0,))
		creator.create("Individual", list, fitness=creator.FitnessMax)

		toolbox.register("attribute", random.randint, 0, F - 1)
		toolbox.register("individual", tools.initRepeat,
										creator.Individual, toolbox.attribute, n=N)
		toolbox.register("population", tools.initRepeat, list, toolbox.individual)
  
		return toolbox
  	