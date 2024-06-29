import sys

n, k = map(int, sys.stdin.readline().split())
sche = list(map(int, sys.stdin.readline().split()))

multi = []

def pop_next(ind):
    now = sche[ind]
    reset = [float('inf')] * n
    # 하나라도 앞으로 안쓰거나 or 모두 한번씩 더 사용한다면, 맨 뒤에 있는거 삭제
    t_sched = sche[ind+1:]
    for i in range(len(t_sched)):
        if t_sched[i] in multi and reset[multi.index(t_sched[i])] == float('inf'):
            reset[multi.index(t_sched[i])] = i

    maxind = reset.index(max(reset))
    multi.pop(maxind)
    multi.append(now)

count = 0
for i in range(len(sche)):
    if sche[i] not in multi:
        if len(multi) < n:
            multi.append(sche[i])
        else:
            pop_next(i)
            count += 1

print(count)