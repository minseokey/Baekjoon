Num = []
dick = {}
i = 1
while True:
    try:
        a = int(input())
        Num.append(a)
        dick.update({a: i})
        i = i + 1
    except:
        break

print(max(Num))
print(dick[max(Num)])
