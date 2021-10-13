import matplotlib.pyplot as plt


def show_multiple_graphs(file_logbooks, file_experiments,
                         file_fitness, title):

    colors = ["b", "r", "g", "y", "orange", "purple"]
    def c(i): return colors[i if i < len(colors) else i % len(colors)]

    l = len(file_logbooks)

    nrows = 1 if l == 1 else l//2
    if l % 2 == 1 and l > 1:
        nrows += 1
    ncols = 1 if l == 1 else 2

    fig, axs = plt.subplots(nrows=nrows, ncols=ncols,
                            squeeze=False, constrained_layout=True)
    fig.suptitle(title)

    for i, (l, e, f) in enumerate(zip(file_logbooks, file_experiments, file_fitness)):
        NGEN, CXPB, MUTPB, NIND, TOURNSIZE, INDPB = e
        title = f"Average Fitness for [NGEN: {NGEN}. CXPB: {CXPB}. MUTPB: {MUTPB}. NIND: {NIND}. TOURNSIZE: {TOURNSIZE}. INDPB: {INDPB}] Fitness: {f}"

        gen = l.select("gen")
        avgs = l.select("avg")

        row = i//2
        col = 0 if i % 2 == 0 else 1

        color = c(i)
        axs[row, col].plot(gen, avgs, color)

        axs[row, col].set_title(title, fontsize=6)
        axs[row, col].set_xlabel("Generation")
        axs[row, col].set_ylabel("Fitness", color=color)

        plt.draw()


    plt.show()
