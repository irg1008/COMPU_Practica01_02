from os import listdir
from os.path import join, isfile, dirname
from typing import List

def get_data_from_file(path: str):
    with open(path, "r") as f:
        data: List[List[int]] = []
        lines = f.readlines()
        for line in lines:
            data.append([int(c) for c in line.split()])
        return data


def get_paths_of_dir(path: str, extension: str):
    return [join(path, f) for f in listdir(path)
            if isfile(join(path, f)) and f.endswith(extension)]


def init_data(n_problem=None):    
    dir = dirname(__file__)

    inDirPath = join(dir, "../../Input/")
    inPaths = get_paths_of_dir(inDirPath, extension=".in")

    if n_problem is None or not 1 <= n_problem <= 5:
        n_problem = int(input("Elige el problema (1-5): "))

    inDirFiles = listdir(inDirPath)
    file_name = inDirFiles[n_problem - 1]

    path = inPaths[n_problem - 1]
    prob = get_data_from_file(path)

    # Problem data.
    _, _, F, N, B, T = prob[0]
    config = [F, N, B, T]

    # Rides.
    rides = prob[1:]
    
    return config, rides, file_name
