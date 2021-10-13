
import numpy as np
from Out import show_multiple_graphs

import sys
sys.path.append("..")
sys.path.append("../sol")

from sol.EvalSol import eval_ind
from sol.HashData import init_data
from sol.ConfigSol import config_population, config_create
from sol.EvolStats import config_stats
from sol.EvolCycle import evolve


def config_experiments():
    NPROBLEM = [2, 3, 5]

    NGEN = [100] # Número de generaciones.

    CXPB = [0.5, 1.0]  # Probabilidad de cruce.
    MUTPB = [0.075] # Probabilidad de mutación.
    NIND = [150] # Número de individuos en población.

    TOURNSIZE = [3] # Número de invividuos participando en cada torneo.
    INDPB = [0.05] # Probabilidad independiente de mutar cada atributo.

    combinations = np.array(np.meshgrid(
        NGEN, CXPB, MUTPB, NIND, TOURNSIZE, INDPB)).T.reshape(-1, 6)

    experiments = {}

    for i in NPROBLEM:
        experiments[i] = combinations

    return experiments


def execute(experiments):
    logbooks = {}
    fitness = {}
    files = {}

    config_create()

    for nproblem in experiments:
        problem = experiments[nproblem]

        config, rides, file_name = init_data(nproblem)
        toolbox = config_population(config)
    
        logbooks[nproblem] = []
        fitness[nproblem] = []
        files[nproblem] = file_name

        for exp in problem:
            NGEN, CXPB, MUTPB, NIND, TOURNSIZE, INDPB = exp

            print(
                f"Executing {file_name} with ngen: {NGEN}, mutpb: {MUTPB}, cxpb: {CXPB}, nind: {NIND}, tournsize: {TOURNSIZE}")

            stats = config_stats()
            logbook, best_sol, _ = evolve(toolbox, stats, config, rides,
                                          CXPB, MUTPB, NGEN, NIND, TOURNSIZE, INDPB)

            best_fitness, = eval_ind(best_sol, config, rides)

            logbooks[nproblem].append(logbook)
            fitness[nproblem].append(best_fitness)

    return logbooks, fitness, files


def show_graphs(logbooks, fitness, experiments, files):
    for n in logbooks:
        file_logbooks = logbooks[n]
        file_fitness = fitness[n]
        file_name = files[n]
        file_experiments = experiments[n]

        show_multiple_graphs(file_logbooks, file_experiments,
                            file_fitness, title=file_name)


def main():
    experiments = config_experiments()
    logbooks, fitness, files = execute(experiments)
    show_graphs(logbooks, fitness, experiments, files)


if __name__ == "__main__":
    main()
