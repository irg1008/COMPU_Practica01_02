from deap import tools
from deap import algorithms
from EvalSol import evalRide 

def configAlg(toolbox):
    TOURNSIZE, INDPB = 3, 0.2
    
    toolbox.register("select", tools.selTournament, tournsize=TOURNSIZE)
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=INDPB)
    toolbox.register("evaluate", evalRide)

def evolve(toolbox, stats):
    CXPB, MUTPB, NGEN = 0.5, 0.2, 30

    configAlg(toolbox)

    pop = toolbox.population(n=100)

    pop, logbook = algorithms.eaSimple(
        pop, toolbox, CXPB, MUTPB, NGEN, stats, verbose=False)

    bestSol = tools.selBest(pop, 1)[0]

    print("El resultado de la evolución es: ")
    print(logbook)
    print("La mejor solucion encontrada es: ")
    print(bestSol)
    
    return logbook, bestSol