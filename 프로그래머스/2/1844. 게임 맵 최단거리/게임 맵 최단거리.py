from collections import deque

def solution(maps):
    queue = deque([(1,0,0)])
    ans = float("INF")
    DIR = [(0,1), (1,0), (-1,0), (0,-1)]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    while queue:
        t_cnt,ty,tx = queue.popleft()
        if ty == len(maps)-1 and tx == len(maps[0])-1:
            ans = min(t_cnt, ans)
        else:
            for dy,dx in DIR:
                if 0 <= ty+dy < len(maps) and 0 <= tx + dx < len(maps[0]) and maps[ty+dy][tx+dx] == 1 and not visited[ty+dy][tx+dx]:
                    queue.append((t_cnt + 1, ty+dy, tx+dx))
                    visited[ty + dy][tx + dx] = True
    if ans == float("INF"):
        return -1
    else:
        return ans