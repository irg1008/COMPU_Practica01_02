from os import listdir, path
from os.path import join, isfile
from typing import List

dir = path.dirname(__file__)


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


config = []
rides = []


def init_data():
    global config, rides

    inDirPath = path.join(dir, "../Input/")

    inPaths = get_paths_of_dir(inDirPath, extension=".in")
    inData = [get_data_from_file(path) for path in inPaths]

    n_problem = int(input("Elige el problema (1-5): "))

    prob = inData[n_problem - 1]

    # Problem data.
    _, _, F, N, B, T = prob[0]
    config = [F, N, B, T]

    # Rides.
    rides = prob[1:]


def get_data():
    if config == [] or config == []:
        init_data()
    return config, rides
