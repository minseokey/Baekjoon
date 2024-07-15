a=' '+input()
b=' '+input()
n,m=len(a),len(b)
d=[[0]*m for _ in range(n)]
for i in range(1,n):
    for j in range(1,m):
        if a[i]==b[j]:
            d[i][j] = d[i-1][j-1]+1
print(max(map(max, d)))