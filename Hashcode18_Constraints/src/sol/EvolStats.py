import matplotlib.pyplot as plt
import numpy as np
from deap import tools


def config_stats():
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("max", np.max)
    stats.register("std", np.std)
    stats.register("avg", np.average)

    return stats
