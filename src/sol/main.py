from ConfigSol import config_population, config_create
from EvolStats import config_stats
from EvolCycle import evolve, get_pop
from Out import output_solution, get_pareto_front, plot_dif_scales
from HashData import init_data
from scoop import futures

from time import time

def log(msg):
    print(f"----> {msg}")

def main():

    config, rides, adapted, file_name = init_data()

    # Start timing.
    start = time()

    # Config create, toolbox and stats.
    config_create()
    toolbox = config_population(config)
    stats = config_stats()

    # Get initial population.
    pop = get_pop(toolbox)

    # Pareto front from first population.
    log("Printing pareto front dor first population.")
    get_pareto_front(pop, config, rides, adapted)

    # Evolve algorithm.
    log("Evolving algorithm.")
    logbook, best_sol, pop, _ = evolve(
        toolbox, pop, stats, config, rides, adapted)

    # Register map for multiproccesing.
    toolbox.register("map", futures.map)

    # Stop timing.
    end = time()

    # Plot fitness and penalty.
    log("Printing fitness and penalty over generations.")
    plot_dif_scales(logbook)

    # Pareto front from last population.
    log("Printing pareto front dor last population.")
    get_pareto_front(pop, config, rides, adapted)

    # Output file out.
    output_solution(best_sol, file_name)

    ##############

    print(f"--- {round(end-start, 2)} segundos ---")


if __name__ == "__main__":
    main()
