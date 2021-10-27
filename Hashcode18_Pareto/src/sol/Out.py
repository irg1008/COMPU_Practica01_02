from EvalSol import get_rides_from_ind, sort_rides, eval_ind
from os import path
import numpy as np
import os

import matplotlib.pyplot as plt
import matplotlib.animation as ani

plt_styles = plt.style.available
plt.style.use(plt_styles[7])
plt.rcParams["axes.titlesize"] = "medium"

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


def col(a, *n_cols):
    cols = []
    for n in n_cols:
        col = np.array(a)[:, n]
        cols.append(col)
    return cols


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

# def anim_plot(a, b):
#     fig, ax = plt.subplots()
#     ax.axis([0, max(a), 0, max(b)])
#     l, = ax.plot([], [])

#     def animate(i):
#         l.set_data(a[:i], b[:i])

#     anim = ani.FuncAnimation(fig, animate, frames=len(a))

#     plt.close()
#     return anim


def get_pareto_front(pop, config, rides, adapted):
    fitness = []
    penalty = []
    pairs = []

    # Get fitness and penalty.
    for ind in pop:
        f, p = eval_ind(ind, config, rides, adapted)
        fitness.append(f)
        penalty.append(p)
        pairs.append([f, p])

    # Get frontier.
    sorted_pairs = sorted(pairs, reverse=True)
    front = [sorted_pairs[0]]

    for pair in sorted_pairs[1:]:
        if pair[1] < front[-1][1]:
            front.append(pair)

    f_front = [f for f, _ in front]
    p_front = [p for _, p in front]

    return fitness, penalty, f_front, p_front


def plot_pareto_front(plot, init_pop, pop, config, rides, adapted, title="Pareto Front", file_name=None):
    fitness, penalty, f_front, p_front = get_pareto_front(
        pop, config, rides, adapted)
    init_fitness, init_penalty, init_f_front, init_p_front = get_pareto_front(
        init_pop, config, rides, adapted)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    label_first = f"Population: {len(init_pop)}"
    label_last = f"Population: {len(pop)}"

    label_line = "Pareto Front"
    line_style = "-o"

    x_rotation = 30

    y_label = "Penalty"
    x_label = "Fitness"

    dots_alpha = 0.6

    c = "b"

    ax1.scatter(init_fitness, init_penalty,
                alpha=dots_alpha, label=label_first)
    ax1.plot(init_f_front, init_p_front, line_style, color=c,
             alpha=dots_alpha, label=label_line)
    ax1.tick_params(axis="x", rotation=x_rotation)
    ax1.set_ylabel(y_label)
    ax1.set_xlabel(x_label)
    get_nice_legend(ax1)

    ax2.scatter(fitness, penalty, alpha=dots_alpha, label=label_last)
    ax2.plot(f_front, p_front, line_style, color=c,
             alpha=dots_alpha, label=label_line)
    ax2.tick_params(axis="x", rotation=x_rotation)
    ax2.set_ylabel(y_label)
    ax2.set_xlabel(x_label)
    get_nice_legend(ax2)

    fig.suptitle(title)

    show_or_save(plot, file_name, "pareto")


def plot_dif_scales(plot, lb, title="Fitness and Penalty", separated=True, file_name=None):
    gen = lb.select("gen")
    avgs = lb.select("avg")
    mins = lb.select("min")
    maxs = lb.select("max")

    fit_avgs, pen_avgs = col(avgs, 0, 1)
    fit_maxs, pen_maxs = col(maxs, 0, 1)
    fit_mins, pen_mins = col(mins, 0, 1)

    linewidth = 2
    line_alpha = 0.6
    grid_alpha = 0.1

    fit_label = "Fitness"
    pen_label = "Penalty"
    x_label = "Generations"

    avg_label = "Average"
    max_label = "Maxs"
    min_label = "Mins"

    size = (12, 6)

    c_max, c_avg, c_min = ["r", "g", "b"]

    if separated:
        fig, ax = plt.subplots(2, figsize=size)
        ax1, ax2 = ax[0], ax[1]
    else:
        fig, ax = plt.subplots(figsize=size)
        ax1, ax2 = ax, ax.twinx()

    fig.suptitle(title)

    ax1.set_xlabel(x_label)
    ax1.set_ylabel(fit_label)
    ax1.tick_params(axis="y")
    ax1.grid(alpha=grid_alpha)

    ax2.set_xlabel(x_label)
    ax2.set_ylabel(pen_label)
    ax2.tick_params(axis="y")
    ax2.grid(alpha=grid_alpha)

    ax1.plot(gen, fit_avgs, color=c_avg,
             linewidth=linewidth, alpha=line_alpha, label=avg_label)
    ax1.plot(gen, fit_maxs, color=c_max,
             linewidth=linewidth, alpha=line_alpha, label=max_label)
    ax1.plot(gen, fit_mins, color=c_min,
             linewidth=linewidth, alpha=line_alpha, label=min_label)
    get_nice_legend(ax1)

    ax2.plot(gen, pen_avgs, color=c_avg,
             linewidth=linewidth, alpha=line_alpha, label=avg_label)
    ax2.plot(gen, pen_maxs, color=c_max,
             linewidth=linewidth, alpha=line_alpha, label=max_label)
    ax2.plot(gen, pen_mins, color=c_min,
             linewidth=linewidth, alpha=line_alpha, label=min_label)
    get_nice_legend(ax2)

    show_or_save(plot, file_name, "fitness-penalty")
