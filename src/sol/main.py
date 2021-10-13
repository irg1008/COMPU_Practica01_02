from ConfigSol import config_population, config_create
from EvolStats import config_stats, show_graph
from EvolCycle import evolve
from Out import output_solution
from HashData import init_data
from scoop import futures


from time import time


def main():
    start = time()

    config, rides, file_name = init_data()

    config_create()

    toolbox = config_population(config)
    stats = config_stats()
    logbook, best_sol, _ = evolve(toolbox, stats, config, rides)

    toolbox.register("map", futures.map)

    end = time()

    show_graph(logbook)
    output_solution(best_sol, file_name)

    print(f"--- {round(end-start, 2)} segundos ---")


if __name__ == "__main__":
    main()
