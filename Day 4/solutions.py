from pathlib import Path

INPUT = Path(__file__).resolve().parent / "input.txt"
with INPUT.open() as f:
    ls = [line for line in f.read().strip().splitlines()]

paper = {i + 1j * j for i, l in enumerate(ls) for j, c in enumerate(l) if c == "@"}
octdir = {1, 1j, -1, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j}
removed = []
while to_remove := {z for z in paper if len({z + dz for dz in octdir} & paper) < 4}:
    removed.append(len(to_remove))
    paper -= to_remove

print(removed[0])
print(sum(removed))