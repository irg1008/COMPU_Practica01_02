from ConfigSol import config_population, config_create
from EvolStats import config_stats
from EvolCycle import evolve, get_pop, eval_ind
from Out import output_solution, get_pareto_front, plot_dif_scales, log
from HashData import init_data
from scoop import futures

from time import time


def execute(config, toolbox, stats, rides, adapted, file_name,
            MU=50, LAMBDA=50*2, CXPB=0.85, MUTPB=0.15, NGEN=10, INDPB=0.2, NIND=300, plot=True):

    title = f"* Executing {file_name} with ngen: {NGEN}, mutpb: {MUTPB}, cxpb: {CXPB}, indpb: {INDPB}, nind: {NIND}, lambda: {LAMBDA}, mu: {MU}"
    print(title)

    # Start timing.
    start = time()

    # Get initial population.
    pop = get_pop(toolbox, NIND)

    # Pareto front from first population.
    if plot:
        log("Printing pareto front for first population.")
        get_pareto_front(pop, config, rides, adapted, title)

    # Evolve algorithm.
    log("Evolving algorithm.")
    logbook, best_sol, pop, _ = evolve(
        toolbox, pop, stats, config, rides, adapted,
        MU, LAMBDA, CXPB, MUTPB, NGEN, INDPB)
    log(f"Best sol fitness and penalty: {eval_ind(best_sol, config, rides, adapted)}")

    # Register map for multiproccesing.
    toolbox.register("map", futures.map)

    # Stop timing.
    end = time()

    # Plot fitness and penalty.
    if plot:
        log("Printing fitness and penalty over generations.")
        plot_dif_scales(logbook, title)

    # Pareto front from last population.
    if plot:
        log("Printing pareto front for last population.")
        get_pareto_front(pop, config, rides, adapted, title)

    # Output file out.
    output_solution(best_sol, file_name)

    ##############

    log(f"Executing time: {round(end-start, 2)} seconds.")


def main():
    config, rides, adapted, file_name = init_data()

    # Config create, toolbox and stats.
    config_create()
    toolbox = config_population(config)
    stats = config_stats()

    execute(config, toolbox, stats, rides, adapted, file_name)


if __name__ == "__main__":
    main()
