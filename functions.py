import numpy as np

def Vector(vector):
    return np.array(vector)


def Var(vector):
    mean = np.mean(vector)
    diff = vector - mean
    square = diff**2
    var = square/(len(vector)-1)
    return var
print(Var([1,2,3,4,5]))
