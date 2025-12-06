from pathlib import Path

INPUT = Path(__file__).resolve().parent / "input.txt"
with INPUT.open() as f:
    ls = f.read().strip().splitlines()

dial = 50
s = 0
for l in ls:
    d, move = l[0], int(l[1:])
    dial = (dial + move) % 100 if d == "R" else (dial - move) % 100
    s += dial == 0
print(s)

dial = 50
s = 0
for l in ls:
    d, move = l[0], int(l[1:])
    step = 1 if d == "R" else -1
    for _ in range(move):
        dial = (dial + step) % 100
        s += dial == 0
print(s)
