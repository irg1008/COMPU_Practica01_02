from ConfigSol import configPopulation
from EvolStats import configStats, showGraph
from EvolCycle import evolve
from out import output_solution

def main():   
    toolbox = configPopulation()
    stats = configStats()    
    loogbook, bestSol = evolve(toolbox, stats)
    
    showGraph(loogbook)
    output_solution(bestSol)


if __name__ == "__main__":
    main()
