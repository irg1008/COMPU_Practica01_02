import sys
sys.path.append("..")
sys.path.append("../sol")

from sol.EvalSol import eval_ind
from sol.HashData import init_data
from sol.ConfigSol import config_population, config_create
from sol.EvolStats import config_stats, show_graph
from sol.EvolCycle import evolve

import numpy as np

def config_experiments():
    NGEN = 20
    NPROBLEM = 5

    CXPB = 0.5
    MUTPB = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    NIND = 10

    TOURNSIZE = 3
    INDPB = 0.2

    experiments = np.full(NPROBLEM, None)
    
    for i in range(NPROBLEM):
        experiments[i] = []
        for m in MUTPB:
            exp = [NGEN, m, CXPB, NIND, INDPB, TOURNSIZE]
            experiments[i].append(exp)

    return experiments


def execute(experiments):
    logbooks = []
    fitness = []
    file_names = []
    
    config_create()

    for nproblem, problem in enumerate(experiments):
        config, rides, file_name = init_data(nproblem + 1)
        toolbox = config_population(config)
        
        for exp in problem:
            NGEN, m, CXPB, NIND, INDPB, TOURNSIZE = exp

            print(
                f"Executing {file_name} with ngen: {NGEN}, mutpb: {m}, cxpb: {CXPB}, nind: {NIND}, tournsize: {TOURNSIZE}")

            stats = config_stats()
            logbook, best_sol, _ = evolve(toolbox, stats, config, rides,
                                          CXPB, m, NGEN, NIND, TOURNSIZE, INDPB)

            best_fitness, = eval_ind(best_sol, config, rides)

            logbooks.append(logbook)
            fitness.append(best_fitness)
            file_names.append(file_name)

    return logbooks, fitness, file_names


def show_graphs(logbooks, fitness, file_names):
    for logbook, fit, file_name in zip(logbooks, fitness, file_names):
        print(file_name)
        print(fit)
        show_graph(logbook)


def main():
    experiments = config_experiments()
    logbooks, fitness, file_names = execute(experiments)
    show_graphs(logbooks, fitness, file_names)


if __name__ == "__main__":
    main()
