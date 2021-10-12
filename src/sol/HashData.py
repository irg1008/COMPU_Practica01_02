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

    in_dirpath = join(dir, "../../Input/")
    in_dirfiles = listdir(in_dirpath)
    in_paths = get_paths_of_dir(in_dirpath, extension=".in")

    if n_problem is None or not 1 <= n_problem <= 5:
        for i, file in enumerate(in_dirfiles):
            print(f"{i + 1}.- {file}")
        n_problem = int(input("Elige el problema (1-5): "))

    file_name = in_dirfiles[n_problem - 1]

    path = in_paths[n_problem - 1]
    prob = get_data_from_file(path)

    # Problem data.
    _, _, F, N, B, T = prob[0]
    config = [F, N, B, T]

    # Rides.
    rides = prob[1:]
    
    return config, rides, file_name
