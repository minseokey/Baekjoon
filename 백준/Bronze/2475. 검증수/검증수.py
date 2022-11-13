
a = input().split()
k = 0
for i in range(len(a)):
    k += int(a[i])**2

print(k%10)