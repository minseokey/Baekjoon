n = int(input())
lis = []
for i in range(n):
    lis.append(list(map(int,input().split()))) # 인풋받은 숫자들을 리스트로 저장

lisseq = [[] for i in range(len(lis))]      # 일단 공 리스트 만들어 놓고 값들을 어펜드
for i in range(1,n+1):
    for j in range(i):
        lisseq[i-1].append([])


def onelinepin(col):
    for i in range(col):  #나머지는 받은거 각각 비교 해주어야해요.
        left = lisseq[col-1][i][0] + lis[col][i]  # 합의 각각 오른쪽 왼쪽
        right = lisseq[col-1][i][0] + lis[col][i + 1]
        lisseq[col][i].append(left)
        lisseq[col][i+1].append(right)
        if len(lisseq[col][i]) == 2:
            lisseq[col][i].remove(min(lisseq[col][i]))



lisseq[0][0].append(lis[0][0])
for j in range(1,n):
    onelinepin(j)

print((max(lisseq[n-1]))[0])
