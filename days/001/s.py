from itertools import combinations
from math import prod
import sys

EXP = 2020
EXPL = [int(i) for i in open("input").readlines()]
N = int(sys.argv[1])

# Solution
print(prod([i for i in combinations(EXPL, N) if sum(i) == EXP][0]))
