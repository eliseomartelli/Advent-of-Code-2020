I = [l.strip() for l in open("input").readlines()]

# Part 1
s = sum([l[i * 3 % len(l)] == "#" for i, l in enumerate(I)])

print(s)
