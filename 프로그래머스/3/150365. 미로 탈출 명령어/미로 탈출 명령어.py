def solution(n, m, x, y, r, c, k):
    # 출발 -> x,y
    # 도착 -> r,c
    # 총 거리 -> k
    # x 길이 n, y 길이 m
    # dfs로 찾아 -> 순서는 d,l,r,u

    stack = [(x - 1, y - 1, "")]
    mini = [[["" for _ in range(k + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
    ENU = ["u", "r", "l", "d"]
    DIR = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    while stack:
        tx, ty, route = stack.pop()
        ll = len(route)

        if tx == r - 1 and ty == c - 1 and ll == k:
            return route
        elif tx == r - 1 and ty == c - 1 and (k - ll) % 2 == 1:
            return "impossible"

        elif ll < k:
            for ind, dir in enumerate(DIR):
                if 0 <= tx + dir[0] < n and 0 <= ty + dir[1] < m and (
                        mini[tx + dir[0]][ty + dir[1]][ll + 1] == "" or mini[tx + dir[0]][ty + dir[1]][ll + 1] > route +
                        ENU[ind]):
                    mini[tx + dir[0]][ty + dir[1]][ll + 1] = route + ENU[ind]
                    stack.append((tx + dir[0], ty + dir[1], route + ENU[ind]))

    return "impossible"