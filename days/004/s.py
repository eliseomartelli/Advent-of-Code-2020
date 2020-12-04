import re
from math import prod

I = [i.strip().replace(" ", "\n") for i in open("input").read().split("\n\n")]

s = sum([prod([a in i for a in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]) for i in I])

print(s)
