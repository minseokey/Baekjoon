from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

visited_even = [False] * 500001
visited_odd = [False] * 500001
visited_even[n] = True
queue = deque([(n, k, 0)])
key = False

while queue:
    subin, sis, count = queue.popleft()
    if sis <= 500000:
        # 짝수
        if count % 2 == 0:
            if visited_even[sis]:
                print(count)
                key = True
                break
            else:
                count += 1
                if subin + 1 <= 500000 and not visited_odd[subin + 1]:
                    visited_odd[subin + 1] = True
                    queue.append((subin + 1, sis + count, count))
                if 0 <= subin - 1 and not visited_odd[subin - 1]:
                    visited_odd[subin - 1] = True
                    queue.append((subin - 1, sis + count, count))
                if 0 <= subin * 2 <= 500000 and not visited_odd[subin * 2]:
                    visited_odd[subin * 2] = True
                    queue.append((subin * 2, sis + count, count))

        # 홀수
        else:
            if visited_odd[sis]:
                print(count)
                key = True
                break
            else:
                count += 1
                if subin + 1 <= 500000 and not visited_even[subin + 1]:
                    visited_even[subin + 1] = True
                    queue.append((subin + 1, sis + count, count))
                if 0 <= subin - 1 and not visited_even[subin - 1]:
                    visited_even[subin - 1] = True
                    queue.append((subin - 1, sis + count, count))
                if 0 <= subin * 2 <= 500000 and not visited_even[subin * 2]:
                    visited_even[subin * 2] = True
                    queue.append((subin * 2, sis + count, count))

if not key:
    print(-1)