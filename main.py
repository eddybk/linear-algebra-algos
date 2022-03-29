import numpy as np
import random

def matrix(rows: int, cols: int, *, random_val:bool=False, init_value:float=0) -> np.array:
    if random_val:
        return np.array([[random.uniform(-1, 1) for _ in range(cols)] for _ in range(rows)])
    return np.array([[init_value for _ in range(cols)] for _ in range(rows)])

def vec2(x: float, y: float, /):
    return np.array([x, y])


def vec(*args: float):
    for value in args:
        if not isinstance(value, float):
            if not isinstance(value, int):
                print(f"Could not instanciate a vector with value {value=} of type {type(value)}. Returned None instead")
                return None
    return np.array(args)


if __name__ == "__main__":
    m = matrix(2, 2, random_val=True)
    print(m)