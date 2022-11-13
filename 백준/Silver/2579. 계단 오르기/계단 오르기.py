n = int(input())
lis = [int(input()) for i in range(n)]
adding = [[-1,-1] for j in range(n + 1)]

# adding[n][0] = 1칸 올라온 녀석. 따라서 그 다음값은 adding[n-1][최댓값] + lis[n] 값이 되어야 하며 2칸을 뛰게된다.
adding[0][0] = 0
adding[0][1] = 0
adding[1][0] = lis[0]
adding[1][1] = lis[0]
for i in range(2,n + 1):
    adding[i][0] = lis[i-1] + adding[i-1][1]
    adding[i][1] = max(adding[i-2][0],adding[i-2][1]) + lis[i-1]

print(max(adding[n]))