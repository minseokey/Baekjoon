from collections import deque


def solution(queue1, queue2):
    # 위에서 뽑고, 아래로 더해준다.
    count = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    a = sum(queue1)
    b = sum(queue2)
    t = len(queue1) * 3
    while a != b and count < t:
        count += 1
        if a > b:
            ta = queue1.popleft()
            queue2.append(ta)
            a -= ta
            b += ta
        else:
            tb = queue2.popleft()
            queue1.append(tb)
            b -= tb
            a += tb

    if count == t:
        count = -1

    return count