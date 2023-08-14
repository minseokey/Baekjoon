n = int(input())
dic = {}
anslis = []
for i in range(n):
    temp = int(input())
    dic[i + 1] = temp


def dfs(temp, now, start, visited):
    temp.append(now)
    if dic[now] == start:
        return True
    elif not visited[now]:
        visited[now] = True
        return dfs(temp, dic[now], start, visited)
    else:
        return False


# 일단 자리수와 같은거.
# 그 후에 dfs 를 통해 간다.
for i in range(1, n + 1):
    temp = []
    visited = [False for _ in range(n + 1)]
    key = dfs(temp, i, i, visited)
    if key:
        anslis += temp

ans = []
anslis = list(set(anslis))

print(len(anslis))
for i in anslis:
    ans.append(dic[i])
ans.sort()
for i in ans:
    print(i)
