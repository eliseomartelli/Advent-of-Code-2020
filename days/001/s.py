from itertools import combinations as c
from math import prod as p
from sys import argv as a

I = open("input").readlines()

# Solution
s = [p(i) for i in c([int(i) for i in I], int(a[1])) if sum(i) == int(a[2])][0]

print(s)