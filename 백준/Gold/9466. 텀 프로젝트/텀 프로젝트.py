import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())

for i in range(n):
    leng = int(sys.stdin.readline())
    lis = [0] + list(map(int,sys.stdin.readline().split()))

    # 탐색종료 되었는지 1 ~ n
    finished = [False for _ in range(leng+1)]
    # 방문한 노드인지 1 ~ n
    checked = [False for _ in range(leng+1)]
    ans = leng

    def dfs(curr):
        global ans
        checked[curr] = True
        next = lis[curr]
        # 다음이 연결 가능하다면 계속 연결
        if not checked[next]:
            dfs(next)
        # 만약 더이상의 연결이 힘들다면 리턴돌리면서 탐색종료여부 탐색.
        # check는 방문시에 바뀌고, finished 는 돌아오면서 바뀐다.
        # 따라서 돌아오면서 찾는데 finished 가 True이다? => 사이클 발견.
        else:
            # 다음거가 방문되어있는데, 탐색이 끝나있다면
            if not finished[next]:
                # 사이클 발견
                # 혼자일때
                ans -= 1
                # 여러명일때
                while curr != next:
                    next = lis[next]
                    ans -= 1

        finished[curr] = True

    for j in range(1,leng + 1):
        if not finished[j]:
            dfs(j)

    print(ans)


