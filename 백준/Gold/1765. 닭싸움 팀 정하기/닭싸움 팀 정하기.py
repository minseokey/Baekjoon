import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
enemy = dict()
friend = dict()
for i in range(m):
    typ,a,b = sys.stdin.readline().split()
    if typ == "E":
        if int(a) in enemy.keys():
            enemy[int(a)].append(int(b))
        else:
            enemy[int(a)] = [int(b)]
        if int(b) in enemy.keys():
            enemy[int(b)].append(int(a))
        else:
            enemy[int(b)] = [int(a)]
    else:
        if int(a) in friend.keys():
            friend[int(a)].append(int(b))
        else:
            friend[int(a)] = [int(b)]

        if int(b) in friend.keys():
            friend[int(b)].append(int(a))
        else:
            friend[int(b)] = [int(a)]


final_friend = dict()
# 먼저 원수의 원수를 추가해보자.
for i in range(1,n+1):
    final_friend[i] = set()
    # 원수의원수 추가
    if i in enemy.keys():
        for en in enemy[i]:
            if en in enemy.keys():
                for enen in enemy[en]:
                    if enen != i:
                        final_friend[i].add(enen)

    # 친구의친구는 무제한 루프. set-dfs 이용
    stack = [i]
    while stack:
        temp = stack.pop()
        if temp in friend.keys():
            for fr in friend[temp]:
                if fr not in final_friend[i]:
                    if fr != i:
                        final_friend[i].add(fr)
                        stack.append(fr)



# 이제 친구 다 구함, 팀 만들어주기
# 당연히 DFS
visited = [False] * (n+1)
count = 0
for i in range(1,n+1):
    if not visited[i]:
        count += 1
        stack = [i]
        visited[i] = True
        while stack:
            t = stack.pop()
            for j in final_friend[t]:
                if not visited[j]:
                    stack.append(j)
                    visited[j] = True


print(count)