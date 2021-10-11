from ConfigSol import configPopulation
from EvolStats import configStats, showGraph
from EvolCycle import evolve
from Out import output_solution
from HashData import get_data

def main():     
    toolbox = configPopulation()
    stats = configStats()    
    loogbook, best_sol = evolve(toolbox, stats)
    
    showGraph(loogbook)
    
    _, _, file_name = get_data()
    output_solution(best_sol, file_name)


if __name__ == "__main__":
    main()
