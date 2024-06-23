import sys

fois = int(sys.stdin.readline())
for _ in range(fois):
    n = int(sys.stdin.readline())
    preord = list(map(int,sys.stdin.readline().split()))
    inord = list(map(int,sys.stdin.readline().split()))
    ans = []

    # 범위 지정이 중요
    def recur(p_index, i_s, i_e):

        if i_s < i_e:
            # p의 시작점이 루트다.
            root = preord[p_index]
            in_index = inord.index(root)
            if i_s <= in_index < i_e:
                recur(p_index + 1, i_s, in_index)
            if i_s <= in_index < i_e:
                recur(p_index + 1 + in_index - i_s, in_index + 1, i_e)
            #더하기
            ans.append(root)

    recur(0,0,n)

    print(*ans)