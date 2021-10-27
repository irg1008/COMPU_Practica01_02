from EvalSol import get_rides_from_ind, sort_rides
import os

import matplotlib.pyplot as plt
plt_styles = plt.style.available
plt.rcParams["axes.titlesize"] = "medium"

dir = os.path.dirname(__file__)


def log(msg):
    print(f"----> {msg}")


def output_solution(sol, file_name):
    outDirPath = os.path.join(dir, "../../Output/")
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


def get_nice_legend(ax):
    legend = ax.legend(loc="best", shadow=True, edgecolor="black",
                       borderpad=1, labelspacing=0.8, facecolor="whitesmoke")
    plt.setp(legend.get_texts(), color="black")


def show_or_save(plot, file_name, title):
    if not plot and file_name is not None:
        folder = f"../../Plots/{file_name}"

        exists = os.path.exists(folder)
        if not exists:
            os.mkdir(folder)

        plt.savefig(f"{folder}/{title}.png")
    else:
        plt.show()


def plot_pen_fitness(plot, lb, title="Penalty over generations", file_name=None):
    gen = lb.select("gen")
    avgs = lb.select("avg")
    maxs = lb.select("max")
    mins = lb.select("min")

    min_value = min(mins)

    fig, (ax1, ax2) = plt.subplots(2, figsize=(10, 6))

    ax1.plot(gen, avgs, "g-", label="Average Fitness")
    ax1.plot(gen, maxs, "r-", label="Maxs Fitness")
    ax1.plot(gen, mins, "b-", label="Mins Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness - Penalty", color="b")
    get_nice_legend(ax1)

    ax2.plot(gen, avgs, "g-", label="Average Fitness")
    ax2.plot(gen, maxs, "r-", label="Maxs Fitness")
    ax2.plot(gen, mins, "b-", label="Mins Fitness")
    ax2.set_xlabel("Generation")
    ax2.set_ylim([min_value, 0])
    ax2.set_ylabel("Penalty", color="r")
    get_nice_legend(ax2)
    
    fig.suptitle(title)

    show_or_save(plot, file_name, title="pen_fitness")
