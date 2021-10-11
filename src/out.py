from os import path
from EvalSol import get_rides_from_ind

dir = path.dirname(__file__)


def output_solution(sol):
    outDirPath = path.join(dir, "../Output/")
    outFilePath = outDirPath + "out.txt"
    
    vehicles_rides = get_rides_from_ind(sol)
    
    with open(outFilePath, "w") as f:
        for vehicle_rides in vehicles_rides:
          
          if vehicle_rides is None:
            f.write(str(0))
          else:
            f.write(str(len(vehicle_rides)))
            f.write(" ")
            f.write(" ".join(str(ride) for ride in vehicle_rides))
          
          f.write("\n")
