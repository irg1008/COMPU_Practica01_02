from deap import tools
from deap import algorithms
from EvalSol import eval_ind


def config_alg(toolbox, config, rides, adapted, INDPB):
    def eval(ind): return eval_ind(ind, config, rides, adapted)

    F = config[0]

    toolbox.register("select", tools.selNSGA2)
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutUniformInt, indpb=INDPB, low=0, up=F-1)
    toolbox.register("evaluate", eval)


def get_pop(toolbox, NIND):
    return toolbox.population(n=int(NIND))


def evolve(toolbox, pop, stats, config, rides, adapted, MU=50, LAMBDA=50*2, CXPB=0.85, MUTPB=0.15, NGEN=10, INDPB=0.2):
    MU = int(MU)
    LAMBDA = int(LAMBDA)
    NGEN = int(NGEN)

    config_alg(toolbox, config, rides, adapted, INDPB)

    hof = tools.ParetoFront()

    pop, logbook = algorithms.eaMuPlusLambda(
        pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats, halloffame=hof, verbose=False)

    best_sol = tools.selBest(pop, 1)[0]

    return logbook, best_sol, pop, hof
