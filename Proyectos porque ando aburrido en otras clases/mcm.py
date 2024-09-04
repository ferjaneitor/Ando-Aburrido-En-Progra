from functools import reduce
from math import lcm


i = [1,3,4,7]

def mcm (value):
    return reduce(lcm, value)

print(mcm(i))