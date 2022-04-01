import numpy as np
from typing import Optional

def add_vecs(vecs: np.ndarray, /):
    ret = np.array([0 for _ in range(len(vecs))])
    for i in range(len(vecs)):
        ret += vecs[i]
    return ret

def plot_vec(v: np.ndarray, *, scale=(0, 100)):
    import matplotlib.pyplot as plt

    x = v[0]
    y = v[1]

    _, ax = plt.subplots()
    ax.scatter(x, y)

    ax.set(xlim=(0, scale[0] + 1), xticks=np.arange(scale[0], scale[1] + 1),
       ylim=(0, scale[1] + 1), yticks=np.arange(scale[0], scale[1] + 1))

    plt.show()

def hats(*, dimensions: int, root: list=[0.0], scalars: list=[0.0]) -> Optional[np.ndarray]:
    scalars = np.array(scalars)
    root = np.array(root)
    dimr = range(dimensions)
    if len(scalars) == 1 and scalars[0] == 0:
        ret = np.array([np.array([0 for _ in dimr]) for _ in dimr])
        for i in dimr:
            ret[i][i] = 1
        return ret
    elif len(scalars) == dimensions:
        ret = hats(dimensions=dimensions)
        for i in dimr:
            ret[i] = ret[i] * scalars[i]
        return ret
    else:
        return None