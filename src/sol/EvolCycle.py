from deap import tools
from deap import algorithms
from EvalSol import eval_ind


def config_alg(toolbox, config, rides, TOURNSIZE, INDPB):
    def eval(ind): return eval_ind(ind, config, rides)

    toolbox.register("select", tools.selTournament, tournsize=int(TOURNSIZE))
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=INDPB)
    toolbox.register("evaluate", eval)


def evolve(toolbox, stats, config, rides, CXPB=1.0, MUTPB=0.075, NGEN=100, NIND=150, TOURNSIZE=3, INDPB=0.05):
    config_alg(toolbox, config, rides, TOURNSIZE, INDPB)

    pop = toolbox.population(n=int(NIND))

    pop, logbook = algorithms.eaSimple(
        pop, toolbox, CXPB, MUTPB, int(NGEN), stats, verbose=False)

    best_sol = tools.selBest(pop, 1)[0]

    return logbook, best_sol, pop
