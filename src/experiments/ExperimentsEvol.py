import sys
sys.path.append("..")
sys.path.append("../sol")

from sol.EvolCycle import evolve
from sol.EvolStats import config_stats, show_graph
from sol.ConfigSol import config_population
from sol.HashData import init_data
from sol.EvalSol import eval_ind

def config_experiments():
    experiments = []

    NGEN = [20, 30, 40, 50]
    NPROBLEM = list(range(1, 6))
    CXPB = 0.5

    MUTPB = 0.0
    NIND = 10

    TOURNSIZE = 3
    INDPB = 0.2

    for i in NPROBLEM:
        for n in NGEN:
            exp = [i, n, MUTPB, CXPB, NIND, INDPB, TOURNSIZE]
            experiments.append(exp)

    return experiments


def execute(experiments):
    logbooks = []
    fitness = []
    file_names = []

    for exp in experiments:

        nproblem, ngen, MUTPB, CXPB, NIND, INDPB, TOURNSIZE = exp

        config, rides, file_name = init_data(nproblem)

        print(
            f"Executing {file_name} with ngen: {ngen}, mutpb: {MUTPB}, cxpb: {CXPB}, nind: {NIND}, tournsize: {TOURNSIZE}")

        toolbox = config_population(config)
        stats = config_stats()
        logbook, best_sol, _ = evolve(toolbox, stats, config, rides,
                                      CXPB, MUTPB, ngen, NIND, TOURNSIZE, INDPB)

        best_fitness, = eval_ind(best_sol, config, rides)

        logbooks.append(logbook)
        fitness.append(best_fitness)
        file_names.append(file_name)

    return logbooks, fitness, file_names


def show_graphs(logbooks, fitness, file_names):
    for logbook, fit, file_name in zip(logbooks, fitness, file_names):
        print(file_name)
        print(fitness)
        show_graph(logbook)


def main():
    experiments = config_experiments()
    logbooks, fitness, file_names = execute(experiments)
    show_graphs(logbooks, fitness, file_names)


if __name__ == "__main__":
    main()
