from ConfigSol import config_population, config_create
from EvolStats import config_stats
from EvolCycle import evolve, get_pop, eval_ind
from Out import output_solution, plot_pareto_front, plot_dif_scales, log
from HashData import init_data

from time import time


def execute(config, toolbox, stats, rides, adapted, file_name,
            MU=50, LAMBDA=50*2, CXPB=0.85, MUTPB=0.15, NGEN=10, INDPB=0.2, NIND=300, plot=True):

    title = f"* Executing {file_name} with ngen: {NGEN}, mutpb: {MUTPB}, cxpb: {CXPB}, indpb: {INDPB}, nind: {NIND}, lambda: {LAMBDA}, mu: {MU}"
    print(title)
    file_title = f"{file_name}_CXPB-{CXPB}_MUTPB-{MUTPB}_LAMBDA-{LAMBDA}_MU-{MU}"

    # Start timing.
    start = time()

    # Get initial population.
    init_pop = get_pop(toolbox, NIND)

    # Evolve algorithm.
    log("Evolving algorithm.")
    pop = list(init_pop)
    logbook, best_sol, pop, _ = evolve(
        toolbox, pop, stats, config, rides, adapted,
        MU, LAMBDA, CXPB, MUTPB, NGEN, INDPB)
    log(f"Best sol fitness and penalty: {eval_ind(best_sol, config, rides, adapted)}")

    # Stop timing.
    end = time()

    # Plot fitness and penalty.
    log("Printing fitness and penalty over generations.")
    plot_dif_scales(plot, logbook, title, file_name=file_title)

    # Pareto front from last population.
    log(
        f"Printing pareto front for first and last population. N: {len(pop)}")
    plot_pareto_front(plot, init_pop, pop, config, rides,
                      adapted, title, file_name=file_title)

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
