import re

I = re.findall("([0-9]+)-([0-9]+) ([a-zA-Z]): ([a-z]+)", open("input").read())

# Part 1
s = sum([1 for l in I if int(l[0]) <= l[3].count(l[2]) <= int(l[1])])

print(s)

# Part 2
s = sum([(l[3][int(l[0]) - 1] == l[2]) ^ (l[3][int(l[1]) - 1] == l[2]) for l in I])

print(s)