from deap import tools
from deap import algorithms
from EvalSol import eval_ind


def get_penalty(ind, rides, adapted):
    pen = 0

    for i_ride, i_car in enumerate(ind):
        adapted_ride = rides[i_ride][-1]
        adapted_car = adapted[i_car]

        if adapted_car == 0 and adapted_ride == 1:
            pen += 1

    return pen


def distance(ind, rides, adapted):
    def constant(pen): return pen
    def lineal(pen): return pen*2
    def quadratic(pen): return pen**2

    pen = get_penalty(ind, rides, adapted)
    dis = lineal(pen)
    return dis


def feasible(ind, rides, adapted, B):
    pen = get_penalty(ind, rides, adapted)
    threshold = B  # Bonus value of problem.
    return pen <= threshold


def config_alg(toolbox, config, rides, adapted, INDPB, TOURNSIZE):
    F, _, B, _ = config

    def eval(ind): return eval_ind(ind, config, rides, adapted)
    def feas(ind): return feasible(ind, rides, adapted, B)
    def dis(ind): return distance(ind, rides, adapted)

    toolbox.register("select", tools.selTournament, tournsize=TOURNSIZE)
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutUniformInt, indpb=INDPB, low=0, up=F-1)
    toolbox.register("evaluate", eval)

    DISTANCE_OFFSET = 0

    toolbox.decorate("evaluate", tools.DeltaPenality(
        feas, DISTANCE_OFFSET, dis))


def get_pop(toolbox, NIND):
    return toolbox.population(n=int(NIND))


def evolve(toolbox, pop, stats, config, rides, adapted, CXPB=0.85, MUTPB=0.15, NGEN=10, INDPB=0.2, TOURNSIZE=3):
    NGEN = int(NGEN)
    TOURNSIZE = int(TOURNSIZE)

    config_alg(toolbox, config, rides, adapted, INDPB, TOURNSIZE)

    pop, logbook = algorithms.eaSimple(
        pop, toolbox, CXPB, MUTPB, NGEN, stats, verbose=False)

    best_sol = tools.selBest(pop, 1)[0]

    return logbook, best_sol, pop
