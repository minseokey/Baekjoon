wor = str(input())
liswor = []
ilist = ["c=","c-","d-","lj","nj","s=","z="]

for i in range(0,len(wor)):
    liswor.append(wor[i])
for i in range(-1, len(wor)-2):
    if ("".join(liswor[i:i+3])) == "dz=":
        liswor[i:i+3] = ["0","%","%"]
    if ("".join(liswor[i+1:i+3])) in ilist:
        liswor[i+1:i+3] = ["0", "%"]

k = len(liswor)
for i in range(0,len(liswor)):
    if liswor[i] == "%":
        k = k - 1
print(k)