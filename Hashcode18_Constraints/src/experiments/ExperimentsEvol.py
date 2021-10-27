from sol.HashData import init_data
from sol.ConfigSol import config_population, config_create
from sol.EvolStats import config_stats
from sol.main import execute
import numpy as np
import sys
sys.path.append("..")
sys.path.append("../sol")


def config_experiments():

    NPROBLEM = [2, 3, 4]

    NGEN = [10]  # Número de generaciones.
    CXPB = [0.85]  # Probabilidad de cruce.
    MUTPB = [0.15]  # Probabilidad de mutación.
    NIND = [300]  # Número de individuos en población.
    INDPB = [0.2]  # Probabilidad independiente de mutar cada atributo.
    TOURNSIZE = [3]

    values_to_combine = [CXPB, MUTPB, NGEN, INDPB, TOURNSIZE, NIND]
    combinations = np.array(np.meshgrid(*values_to_combine)
                            ).T.reshape(-1, len(values_to_combine))

    experiments = {}
    for i in NPROBLEM:
        experiments[i] = combinations

    return experiments


def execute_experiments(experiments):
    config_create()

    for nproblem in experiments:
        problem = experiments[nproblem]

        config, rides, adapted, file_name = init_data(nproblem)
        toolbox = config_population(config)
        stats = config_stats()

        for exp in problem:
            execute(config, toolbox, stats, rides, adapted,
                    file_name, *exp, plot=True)


def main():
    experiments = config_experiments()
    execute_experiments(experiments)


if __name__ == "__main__":
    main()
