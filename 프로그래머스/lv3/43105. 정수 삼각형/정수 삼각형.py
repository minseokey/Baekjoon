def solution(triangle):
    t = list(reversed(triangle))
    for i in range(len(t)):
        for j in range(len(t) - i - 1):
            t[i+1][j] += max(t[i][j],t[i][j+1])
    return t[len(t) - 1][0]