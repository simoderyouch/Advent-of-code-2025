from pathlib import Path

INPUT = Path(__file__).resolve().parent / "input.txt"
with INPUT.open() as f:
    data = f.read().strip()

res1 = res2 = 0
for token in data.split(","):
    a, b = token.split("-")
    for i in range(int(a), int(b) + 1):
        s = str(i)
        mid = len(s) // 2
        if len(s) % 2 == 0 and s[:mid] == s[mid:]:
            res1 += i
        if any(s == s[:k] * (len(s) // k) for k in range(1, mid + 1)):
            res2 += i

print(res1)
print(res2)