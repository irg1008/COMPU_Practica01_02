import random
from deap import base, creator, tools
from HashData import get_data


def configPopulation(): 
		toolbox = base.Toolbox()

		config, _ = get_data()
		F, N, _, _ = config

		creator.create("FitnessMax", base.Fitness, weights=(1.0,))
		creator.create("Individual", list, fitness=creator.FitnessMax)

		toolbox.register("attribute", random.randint, 0, F - 1)
		toolbox.register("individual", tools.initRepeat,
										creator.Individual, toolbox.attribute, n=N)
		toolbox.register("population", tools.initRepeat, list, toolbox.individual)
  
		return toolbox
  	