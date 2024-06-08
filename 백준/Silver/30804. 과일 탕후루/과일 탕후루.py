import sys
from collections import defaultdict

N = int(sys.stdin.readline())
fruit = list(map(int, sys.stdin.readline().split()))

maxx = 0
left = 0
fruit_count = defaultdict(int)

for right in range(N):
    fruit_count[fruit[right]] += 1

    while len(fruit_count) > 2:
        fruit_count[fruit[left]] -= 1
        if fruit_count[fruit[left]] == 0:
            del fruit_count[fruit[left]]
        left += 1

    maxx = max(maxx, right - left + 1)

print(maxx)
