import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


def solution(operations):
    answer = []
    num_dict = defaultdict(int)
    min_heap = []
    max_heap = []
    for o in range(operations):
        oper, num = input().split()
        num = int(num)
        if oper == 'I':
            num_dict[num] += 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if num == 1:
                while (max_heap):
                    max_num = -heapq.heappop(max_heap)
                    if num_dict[max_num] != 0:
                        num_dict[max_num] -= 1
                        break
            else:
                while (min_heap):
                    min_num = heapq.heappop(min_heap)
                    if num_dict[min_num] != 0:
                        num_dict[min_num] -= 1
                        break

    while (max_heap and num_dict[-max_heap[0]] == 0): heapq.heappop(max_heap)
    while (min_heap and num_dict[min_heap[0]] == 0): heapq.heappop(min_heap)

    if not max_heap:
        print('EMPTY')
    else:
        print(-max_heap[0], min_heap[0])


T = int(input())
for _ in range(T):
    k = int(input())
    solution(k)