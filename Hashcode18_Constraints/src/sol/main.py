from ConfigSol import config_population, config_create
from EvolStats import config_stats
from EvolCycle import evolve, get_pop, eval_ind
from Out import output_solution, plot_pen_fitness, log
from HashData import init_data
# from scoop import futures
from time import time


def execute(config, toolbox, stats, rides, adapted, file_name,
            CXPB=0.85, MUTPB=0.15, NGEN=30, INDPB=0.2, TOURNSIZE=3, NIND=100, plot=True):

    title = f"* Executing {file_name} with ngen: {NGEN}, mutpb: {MUTPB}, cxpb: {CXPB}, indpb: {INDPB}, nind: {NIND}, tournsize: {TOURNSIZE}"
    print(title)

    # Start timing.
    start = time()

    # Get initial population.
    pop = get_pop(toolbox, NIND)

    # Evolve algorithm.
    log("Evolving algorithm.")
    logbook, best_sol, pop = evolve(
        toolbox, pop, stats, config, rides, adapted, CXPB, MUTPB, NGEN, INDPB, TOURNSIZE)
    log(f"Best sol fitness and penalty: {eval_ind(best_sol, config, rides, adapted)}")

    # Register map for multiproccesing.
    # toolbox.register("map", futures.map)

    # Stop timing.
    end = time()

    # Plot penalty and fitness.
    if plot:
        log("Printing penalty or fitness over generations.")
        plot_pen_fitness(logbook, title)

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
