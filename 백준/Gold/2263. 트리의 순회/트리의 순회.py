import sys

sys.setrecursionlimit(100000)
node = int(sys.stdin.readline())
inorder = sys.stdin.readline().split()
postorder = sys.stdin.readline().split()

# 여기서 n => 해당크기의 root,
# left => root 기준 왼쪽 노드들
# right => root 기준 오른쪽 노드들

dic = []


def recur(ins, ine, pos, poe):

    # leafnode
    if inorder[ins] == postorder[pos] and ine == ins and poe == pos:
        dic.append(inorder[ine])
    else:
        # root 구하기
        root = postorder[poe]
        dic.append(root)

        # 만약 오른쪽만 남았다면
        if inorder[ins] == root:
            recur(ins + 1, ine, pos, poe - 1)

        # 만약 왼쪽만 남았다면
        elif inorder[ine] == root:
            recur(ins, ine - 1, pos, poe - 1)

        # 아니라면
        else:
            inlis = [0, 0, 0, 0]

            for i in range(1, len(inorder)):
                if inorder[i] == root:
                    # l_st
                    inlis[0] = ins
                    # l_en
                    inlis[1] = i-1
                    # r_st
                    inlis[2] = i+1
                    # r_en
                    inlis[3] = ine

            polis = [pos, pos + inlis[1] - inlis[0], pos + inlis[1] - inlis[0] + 1, poe - 1]


            recur(inlis[0], inlis[1], polis[0], polis[1])

            recur(inlis[2], inlis[3], polis[2], polis[3])


recur(0, len(inorder) - 1, 0, len(postorder) - 1)

print(" ".join(dic))
