from deap import tools
from deap import algorithms
from EvalSol import eval_ind

def configAlg(toolbox):
    TOURNSIZE, INDPB = 3, 0.2
    
    toolbox.register("select", tools.selTournament, tournsize=TOURNSIZE)
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=INDPB)
    toolbox.register("evaluate", eval_ind)

def evolve(toolbox, stats):
    CXPB, MUTPB, NGEN = 0.5, 0.0, 20
    NIND = 10

    configAlg(toolbox)

    pop = toolbox.population(n=NIND)

    pop, logbook = algorithms.eaSimple(
        pop, toolbox, CXPB, MUTPB, NGEN, stats, verbose=False)

    bestSol = tools.selBest(pop, 1)[0]

    print("El resultado de la evolución es: ")
    print(logbook)
    print("La mejor solucion encontrada es: ")
    print(bestSol)
    
    return logbook, bestSol