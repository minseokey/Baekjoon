import sys
import itertools
from collections import deque

n, m = map(int, sys.stdin.readline().split())

grid = []
virus = []
empty = set()

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j, val in enumerate(row):
        if val == 2:
            virus.append((i, j))
        elif val == 0:
            empty.add((i, j))
    grid.append(row)

combinations = list(itertools.combinations(virus, m))

if not empty:
    print(0)
else:
    DIR = ((1, 0), (0, 1), (-1, 0), (0, -1))
    mincount = float("inf")
    
    for comb in combinations:
        queue = deque(comb)
        visited = set(comb)
        temp_empty = empty.copy()
        
        count = 0
        while queue and temp_empty:
            next_queue = deque()
            for y, x in queue:
                for dy, dx in DIR:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n and (ny, nx) not in visited:
                        visited.add((ny, nx))
                        if grid[ny][nx] == 0:
                            temp_empty.remove((ny, nx))
                        if grid[ny][nx] in {0, 2}:
                            next_queue.append((ny, nx))
            queue = next_queue
            count += 1
            if count >= mincount:  # Early break to save time
                break
        
        if not temp_empty:  # If every position is infected
            mincount = min(mincount, count)
    
    print(-1 if mincount == float('inf') else mincount)
