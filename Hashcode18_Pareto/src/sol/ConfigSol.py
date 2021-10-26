import random
from deap import base, creator, tools


def config_create():
    if not hasattr(creator, "FitnessMax"):
        creator.create("FitnessMax", base.Fitness, weights=(1.0, -1.0))

    if not hasattr(creator, "Individual"):
        creator.create("Individual", list, fitness=creator.FitnessMax)


def config_population(config):
    F, N, _, _ = config

    toolbox = base.Toolbox()

    toolbox.register("attribute", random.randint, 0, F - 1)
    toolbox.register("individual", tools.initRepeat,
                     creator.Individual, toolbox.attribute, n=N)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    return toolbox
