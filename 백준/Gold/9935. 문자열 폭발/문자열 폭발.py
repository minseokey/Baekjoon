import sys

word = sys.stdin.readline().strip()
explo = [*sys.stdin.readline().strip()]
sexplo = len(explo)
ans = []
for i in word:
    ans.append(i)
    while len(ans) >= sexplo and ans[- sexplo:] == explo:
        del ans[-sexplo:]
print("".join(ans)) if ans else print("FRULA")