a = int(input())
b = input().split(" ")
newb = []
for i in range(0,a):
     newb.append(int(b[i]))
print(min(newb),max(newb))

