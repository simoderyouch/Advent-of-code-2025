from pathlib import Path
from collections import deque

INPUT = Path(__file__).resolve().parent / "input.txt"
with INPUT.open() as f:
    lines = f.read().splitlines()

grid = {r + 1j * c: ch for r, row in enumerate(lines) for c, ch in enumerate(row)}
start = next(z for z, ch in grid.items() if ch == "S")

q = deque([start])
seen = {start}
count_splits = 0
hist = {start: 1}

while q:
    z = q.popleft()
    nz = z + 1
    if nz in seen or nz not in grid:
        continue
    
    seen.add(nz)
    if grid[nz] == "^":
        left = nz - 1j
        right = nz + 1j
        q.append(left)
        q.append(right)
        hist[left] = hist.get(left, 0) + hist.get(z, 0)
        hist[right] = hist.get(right, 0) + hist.get(z, 0)
        count_splits += 1
    else:
        q.append(nz)
        hist[nz] = hist.get(nz, 0) + hist.get(z, 0)

print(count_splits)

bottom_r = max(z.real for z in grid)
bottom = [z for z in grid if z.real == bottom_r]
print(sum(hist.get(b, 0) for b in bottom))
