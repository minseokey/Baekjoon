m,d=input().split()
m=int(m)
d=int(d)

c=0
a=[0,31,28,31,30,31,30,31,31,30,31,30]
for i in range(0,m):
    c=c+a[i]
    
if (c+d)%7==1 :
    print('MON')
elif (c+d)%7==2 :
    print('TUE')
elif (c+d)%7==3 :
    print('WED')
elif (c+d)%7==4 :
    print('THU')
elif (c+d)%7==5 :
    print('FRI')
elif (c+d)%7==6 :
    print('SAT')
else :
    print('SUN')