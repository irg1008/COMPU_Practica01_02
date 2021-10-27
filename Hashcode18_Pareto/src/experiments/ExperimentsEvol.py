import numpy as np
import sys
sys.path.append("..")
sys.path.append("../sol")
from sol.main import execute
from sol.EvolStats import config_stats
from sol.ConfigSol import config_population, config_create
from sol.HashData import init_data


def config_experiments():

    NPROBLEM = [2, 3]
    NGEN = [15]  # Número de generaciones.
    NIND = [300]  # Número de individuos en población.
    INDPB = [0.2]  # Probabilidad independiente de mutar cada atributo.

    CXPB = [0.5, 0.7, 0.9]  # Probabilidad de cruce.
    MUTPB = [0.1, 0.3, 0.5]  # Probabilidad de mutación.

    # Límite de invididuos en población.
    POR_MU = [0.6, 1, 1.4]
    MU = np.array(NIND) * np.array(POR_MU)

    # Creación de hijos en cada generación. Aumenta población hasta MU.
    POR_LAMBDA = [1.0, 2.0, 3.0]
    LAMBDA = np.array(NIND) * np.array(POR_LAMBDA)

    values_to_combine = [MU, LAMBDA, CXPB, MUTPB, NGEN, INDPB, NIND]
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
            _, _, CXPB, MUTPB, _, _, _ = exp

            if CXPB + MUTPB > 1:
                continue

            execute(config, toolbox, stats, rides, adapted,
                    file_name, *exp, plot=True)


def main():
    experiments = config_experiments()
    execute_experiments(experiments)


if __name__ == "__main__":
    main()
