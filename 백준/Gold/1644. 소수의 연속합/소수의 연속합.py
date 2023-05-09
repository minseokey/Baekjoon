n = int(input())

# 1. 에라토스테네스로 n 이하의 모든 소수 구하기
def primenum(n):
    lis = [False for i in range(n + 1)]
    prime = []

    for i in range(2,n + 1):
        if not lis[i]:
            prime.append(i)
            for j in range(2*i, n + 1, i):
                lis[j] = True
    return prime

# 투포인터 이용하자.
primelis = primenum(n)
start = 0
end = 0
temp = 0

# 일단 처음값부터 다 더했을때 처음으로 n 넘는값 찾기.
while end <= len(primelis):
    end += 1
    if sum(primelis[start:end]) >= n:
        temp = sum(primelis[start:end])
        break

# 그 후에 앞에서 하나씩 + 그러다가 합이 n 보다 작아지면 뒤에서 하나 + 시킨다. 이거 끝까지 반복.
ans = 0

while start <= len(primelis) and end <= len(primelis):
    if temp < n:
        if end < len(primelis):
            temp += primelis[end]
        end += 1
    elif temp > n:
        temp -= primelis[start]
        start += 1
    elif temp == n:
        if end < len(primelis):
            temp += primelis[end]
        temp -= primelis[start]
        ans += 1
        end += 1
        start += 1

print(ans)



