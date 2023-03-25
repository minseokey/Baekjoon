# import math
import sys
#
# a, b, c = map(int, sys.stdin.readline().split())
# lis = [False for i in range(math.floor(math.log2(a)) + 1)]
# lis[1] = a % c
# lis[0] = 1
#
# # 2->4->8->16->....
# k = math.floor(math.log2(a))
# temp = k
# for i in range(1, k - 1):
#     if i * 2 <= k:
#         lis[2 * i] = (lis[i] * lis[i]) % c
# ans = 1
# while True:
#     if b == 0:
#         break
#     for i in range(len(lis)-1,-1, -1):
#         if b - i >= 0 and lis[i]:
#             b -= i
#             ans *= lis[i]
#             ans %= c
#             break
#
# print(ans % c)
a, b, c = map(int, sys.stdin.readline().split())
print(pow(a,b,c))