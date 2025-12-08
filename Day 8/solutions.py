from pathlib import Path
from itertools import combinations
from math import prod

INPUT = Path(__file__).resolve().parent / "input.txt"
with INPUT.open() as f:
    ln = f.read().splitlines()

ns = [tuple(map(int, l.split(","))) for l in ln]
edges = sorted(
    (sum((x1 - x2) ** 2 for x1, x2 in zip(n1, n2)), n1, n2)
    for n1, n2 in combinations(ns, 2)
)

parent = {n: n for n in ns}
size = {n: 1 for n in ns}
components = len(ns)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

for i, (_, n1, n2) in enumerate(edges):
    if i == 1000:
        comp_sizes = {}
        for n in ns:
            r = find(n)
            comp_sizes[r] = comp_sizes.get(r, 0) + 1
        print(prod(sorted(comp_sizes.values())[-3:]))
    if union(n1, n2):
        components -= 1
    if components == 1:
        print(n1[0] * n2[0])
        break