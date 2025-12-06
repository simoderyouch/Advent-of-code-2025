from pathlib import Path
import math

INPUT_PATH = Path(__file__).resolve().parent / "input.txt"
with open(INPUT_PATH) as f:
    lines = f.read().splitlines()

nums_lines = lines[:-1]
ops_line = lines[-1]

starts = []
ops = []
for i, ch in enumerate(ops_line):
    if ch == "+":
        starts.append(i)
        ops.append(sum)
    elif ch == "*":
        starts.append(i)
        ops.append(math.prod)

ends = [s_next - 1 for s_next in starts[1:]] + [None]

nums1 = [[line[start:end] for line in nums_lines] for start, end in zip(starts, ends)]
nums2 = [["".join(chars) for chars in zip(*group)] for group in nums1]

for dataset in (nums1, nums2):
    total = 0
    for op, col in zip(ops, dataset):
        total += op(map(int, col))
    print(total)

