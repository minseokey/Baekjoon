a = int(input())
count2 = 0
count5 = 0
count10 = 0
for i in range(1,a+1):
    boo = True
    while boo:
        if i%100 == 0:
            count10+= 2
            i/=100
        elif i%10 == 0:
            count10 += 1
            i/=10
        elif i%5 == 0:
            count5 += 1
            i/=5
        elif i%2 == 0:
            count2 += 1
            i/=2
        else:
            boo = False

print(count10 + min(count5,count2))