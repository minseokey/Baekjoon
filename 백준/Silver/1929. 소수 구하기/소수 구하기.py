y, z = map(int,input().split())
a = [False,False] + [True]*(z-1)
# 0,1, 제외하고 나머지는 리스트로 저장
# 2 ~ n 까지 TRUE로 저장
primes=[]

for i in range(2, z+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, z+1, i):
        a[j] = False
for i in primes:
    if i >= y:
        print(i)