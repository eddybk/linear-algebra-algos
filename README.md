# Linear algebra algorithms
There are a couple of things to be mentioned before talking about the implementations themselves:
- Numpy was used for all the operations including vectors and matrices
- I wrote a lot of wrappers for ease of use reasons

Let's begin by talking about the wrappers first:

(if you find that boring just skip ahead to the next chapter)

## 1) Semantic wrappers for np.ndarray operations

### Ok... why?
Working with raw function calls for np.ndarray methods can be a bit tedious,
so there is no real reason, it just takes little time to implement and it helps with productivity in the long run.
:)

There are wrappers for making
- Matrices
- N dim vectors
- 2d vectors
- 3d vectors

### Matrix wrapper
---
Matrix wrapper returns an ndarray, just like all other wrappers, but:
first it type-checks the params, then it checks the kwarg random_vals(by default False),
to see if the matrix should be made with random elemtns. There is also init_value kwarg(set to 0 by default).
If random_vals is False, then the matrix is initiated filled with init_values.. value..

### N dim vector wrapper
---
The only parameter this functions takes is the *args, which gets type-checked against int and float types. If one element is not 
an instance of int or float, then the wrapper returns None. Otherwise it returns np.array(args).
In essence, np.array() is itself an n-dimensional vector, but it's nicer to call it that as well.

### 2 and 3 dimensional vectors
---
A simple wrapper that makes a list out of given parameters (which can not be passed by keyword) and makes an 
np.array out of it, which it then returns. 