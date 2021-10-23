import numpy as np
import sys
sys.path.append("..")
sys.path.append("../sol")
from sol.EvalSol import eval_ind
from sol.HashData import init_data
from sol.ConfigSol import config_population, config_create
from sol.EvolStats import config_stats
from sol.EvolCycle import evolve, get_pop
from sol.Out import plot_dif_scales, get_pareto_front


def config_experiments():

    NPROBLEM = [2, 3, 4]

    NGEN = [10]  # Número de generaciones.
    CXPB = [0.85]  # Probabilidad de cruce.
    MUTPB = [0.15]  # Probabilidad de mutación.
    NIND = [300]  # Número de individuos en población.
    INDPB = [0.2]  # Probabilidad independiente de mutar cada atributo.

    values_to_combine = [NGEN, CXPB, MUTPB, NIND, INDPB]
    combinations = np.array(np.meshgrid(*values_to_combine)
                            ).T.reshape(-1, len(values_to_combine))

    experiments = {}
    for i in NPROBLEM:
        experiments[i] = combinations

    return experiments


def execute(experiments, plot=False):
    config_create()

    PER_MU = 0.2

    for nproblem in experiments:
        problem = experiments[nproblem]

        config, rides, adapted, file_name = init_data(nproblem)
        toolbox = config_population(config)

        for exp in problem:
            NGEN, CXPB, MUTPB, NIND, INDPB = exp

            # Número de individuos que se seleccionan en cada generación.
            MU = NIND * PER_MU
            LAMBDA = MU * 2  # Number of children produced in each generation.

            print(
                f"Executing {file_name} with ngen: {NGEN}, mutpb: {MUTPB}, cxpb: {CXPB}, indpb: {INDPB}, nind: {NIND}, lambda: {LAMBDA}, mu: {MU}")

            stats = config_stats()

            pop = get_pop(toolbox)

            if plot:
                get_pareto_front(pop, config, rides, adapted)

            logbook, _, pop, _ = evolve(
                toolbox, pop, stats, config, rides, adapted,
                MU, LAMBDA, CXPB, MUTPB, NGEN, INDPB)

            if plot:
                plot_dif_scales(logbook)
                get_pareto_front(pop, config, rides, adapted)


def main():
    experiments = config_experiments()
    execute(experiments, plot=True)


if __name__ == "__main__":
    main()
