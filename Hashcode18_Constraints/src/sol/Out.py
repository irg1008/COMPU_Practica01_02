from EvalSol import get_rides_from_ind, sort_rides
from os import path

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


def plot_pen_fitness(lb, title="Penalty over generatons"):
    gen = lb.select("gen")
    avgs = lb.select("avg")
    maxs = lb.select("max")
    mins = lb.select("min")

    _, ax = plt.subplots()

    ax.plot(gen, avgs, "r-", label="Average Fitness")
    ax.plot(gen, maxs, "r-", label="Average Fitness")
    ax.plot(gen, mins, "r-", label="Average Fitness")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness", color="b")
    ax.set_title(title)

    plt.plot()
