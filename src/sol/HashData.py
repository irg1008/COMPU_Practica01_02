import numpy as np
from os import listdir
from os.path import join, isfile, dirname
from typing import List

config, rides = None, None
file_name = None


def get_data():
    global config, rides, file_name
    if config is None or rides is None or file_name is None:
        init_data()
    return config, rides, file_name


dir = dirname(__file__)


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


def init_data():
    global config, rides, file_name

    inDirPath = join(dir, "../../Input/")
    inPaths = get_paths_of_dir(inDirPath, extension=".in")

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
