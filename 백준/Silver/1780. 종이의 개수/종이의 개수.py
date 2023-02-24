import sys

N = int(sys.stdin.readline())
lis = []
for i in range(N):
    lis.append(list(map(int,sys.stdin.readline().split())))

dic = dict()
dic[-1] = 0
dic[0] = 0
dic[1] = 0

def counter(N, lis):
    # 단위구간이 모두 같은지 탐색
    if len(lis) == 1:
        dic[lis[0][0]] += 1
        return
    key = True

    for j in range(N):
        if lis[0] != lis[j]:
            key = False
            break

    for i in range(N):
        if len(list(set(lis[i]))) != 1:
            key = False
        if not key:
            break


    # 만약 단위구간이 모두 같다면
    if key:
        temp = lis[0][0]
        dic[temp] += 1
    # 하나라도 다르다면
    else:
        for k in range(3):
            for i in range(3):
                templis = [j[k*(N//3):(k+1)*(N//3)] for j in lis[i*(N//3):(i+1)*(N//3)]]
                counter(N//3,templis)

counter(N,lis)
print(dic[-1])
print(dic[0])
print(dic[1])
