import sys
n = int(sys.stdin.readline())
for i in range(n):
   nn = int(input())
   counter = 0
   dic = dict()
   for j in range(nn):
      name,part = sys.stdin.readline().split()
      if part not in dic.keys():
         dic[part] = [name]
      else:
         dic[part].append(name)

   count = 1
   for i in dic.keys():
      count *= len(dic[i])+1
   print(count - 1)