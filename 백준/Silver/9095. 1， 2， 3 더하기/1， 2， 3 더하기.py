import sys
n = int(sys.stdin.readline())
dptable = dict()
dptable[1] = 1
dptable[2] = 2
dptable[3] = 4
for i in range(n):
   k = int(input())
   if k >= 4:
      for i in range(4,k+1):
         dptable[i] = dptable[i-1]+dptable[i-2]+dptable[i-3]

   print(dptable[k])