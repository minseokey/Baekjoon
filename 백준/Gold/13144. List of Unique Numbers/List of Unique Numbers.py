import sys
from collections import defaultdict

num_dict = defaultdict(list)
input = sys.stdin.readline
n = int(input().rstrip())

num_list = list(map(int, input().split()))

result = 0
start, end = 0, 0
seq = [False for _ in range(1000001)]

while start < n and end < n:
    if not seq[num_list[end]]:
        seq[num_list[end]] = True
        end += 1
        result += (end - start)
    else:
        seq[num_list[start]] = False
        start += 1

print(result)