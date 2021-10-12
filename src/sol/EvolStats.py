import matplotlib.pyplot as plt
import numpy as np
from deap import tools


def config_stats():
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    return stats


def show_graph(logbook):
    gen = logbook.select("gen")
    avgs = logbook.select("avg")

    fig = plt.figure()

    ax = plt.gca()
    line = ax.plot(gen, avgs, "r-", label="Average Fitness")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness", color="b")

    plt.show()
