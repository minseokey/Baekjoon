Word = input()
Lis = []
numlis = []
a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(0,len(Word)):
    Lis.append(Word[i])
    numlis.append(i)

for k in range(0, len(a)):
    for j in range(0, len(Lis)):
        if a[k] == Lis[j]:
            a[k] = (numlis[j])

for o in range(0,len(a)):
    if type(a[o]) != int:
        a[o] = -1


print(' '.join(map(str, a)))