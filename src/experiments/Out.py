import matplotlib.pyplot as plt
import numpy as np


def show_multiple_graphs(file_logbooks, file_experiments,
                         file_fitness, title):

    fig, ax = plt.subplots(len(file_logbooks), constrained_layout=True)
    fig.suptitle(title)

    for i, (l, e, f) in enumerate(zip(file_logbooks, file_experiments, file_fitness)):
        NGEN, CXPB, MUTPB, NIND, TOURNSIZE, INDPB = e
        title = f"Average Fitness for [NGEN: {NGEN}. CXPB: {CXPB}. MUTPB: {MUTPB}. NIND: {NIND}. TOURNSIZE: {TOURNSIZE}. INDPB: {INDPB}] Fitness: {f}"

        gen = l.select("gen")
        avgs = l.select("avg")

        ax[i].plot(gen, avgs, "r-")

        ax[i].set_title(title, fontsize=6)
        ax[i].set_xlabel("Generation")
        ax[i].set_ylabel("Fitness", color="b")

        plt.draw()

    plt.show()
