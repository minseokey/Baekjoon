n=int(input())
t=str(input())
a=list(t)
q=0
for i in range(0,n):
    sum= int((a[i]))+q
    q=sum
print(sum)
    