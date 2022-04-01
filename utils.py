import numpy as np
def plot_vec(v: np.ndarray, *, scale=(0, 100)):
    import matplotlib.pyplot as plt

    x = v[0]
    y = v[1]

    _, ax = plt.subplots()
    ax.scatter(x, y)

    ax.set(xlim=(0, scale[0] + 1), xticks=np.arange(scale[0], scale[1] + 1),
       ylim=(0, scale[1] + 1), yticks=np.arange(scale[0], scale[1] + 1))

    plt.show()