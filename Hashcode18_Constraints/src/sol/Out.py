from EvalSol import get_rides_from_ind, sort_rides
from os import path
import numpy as np

import matplotlib.pyplot as plt
plt_styles = plt.style.available
plt.style.use(plt_styles[7])

dir = path.dirname(__file__)


def log(msg):
    print(f"----> {msg}")


def output_solution(sol, file_name):
    outDirPath = path.join(dir, "../../Output/")
    outFilePath = outDirPath + file_name.strip(".in") + ".out"

    vehicles_rides = get_rides_from_ind(sol)

    with open(outFilePath, "w") as f:
        for v_r in vehicles_rides:
            if v_r is None:
                f.write(str(0))
            else:
                v_r = sort_rides(v_r)
                f.write(str(len(v_r)))
                f.write(" ")
                f.write(" ".join(str(pos) for pos, _ in v_r))

            f.write("\n")

    log(f"Output file for {file_name} has been created in output folder with same name.")

def show_or_save(file_name):
    if file_name is None:
        plt.show()
    else:
        plt.savefig(f"../../Plots/{file_name}.png")

def plot_pen_fitness(lb, title="Penalty over generations", file_name=None):
    gen = lb.select("gen")
    avgs = lb.select("avg")
    maxs = lb.select("max")
    mins = lb.select("min")
    
    avgs = np.abs(avgs)
    maxs = np.abs(maxs)
    mins = np.abs(mins)

    _, ax = plt.subplots()

    ax.plot(gen, avgs, "r-", label="Average Fitness")
    ax.plot(gen, maxs, "b-", label="Max. Fitness")
    ax.plot(gen, mins, "g-", label="Min. Fitness")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness and Penalty", color="b")
    ax.set_title(title)
    
    legend = plt.legend(loc="best", shadow=True, edgecolor="black",
                    borderpad=1, labelspacing=0.8, facecolor="whitesmoke")
    
    plt.setp(legend.get_texts(), color="black")
    show_or_save(file_name)
