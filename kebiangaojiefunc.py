from math import sqrt
def same(x, *fs):
    s=[f(x) for f in fs]
    return s
print(same(2, sqrt, abs))