from math import prod

I = [l.strip() for l in open("input").readlines()]

# Part 1
s = sum([l[i * 3 % len(l)] == "#" for i, l in enumerate(I)])

print(s)

s = prod([sum([l[i * a[0] % len(l)] == "#" for i, l in enumerate(I[0 :: a[1]])]) for a in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])

print(s)
