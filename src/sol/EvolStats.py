import matplotlib.pyplot as plt
import numpy as np
from deap import tools


def config_stats():
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min, axis=0)
    stats.register("max", np.max, axis=0)
    stats.register("std", np.std, axis=0)
    stats.register("avg", np.average, axis=0)

    return stats
