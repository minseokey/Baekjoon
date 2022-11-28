import itertools
def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def solution(word):
    t = prime_list(10 ** len(word))
    ans = 0
    temp = []
    page = []
    for k in range(len(word)):
        temp.append(word[k])
    for l in range(len(word)):
        page += list(itertools.permutations(temp,l+1))
    page = list(set(page))
    for q in page:
        if int("".join(q)) in t and int("".join(q)) != 0:
            ans += 1
            t.remove(int("".join(q)))


    return ans