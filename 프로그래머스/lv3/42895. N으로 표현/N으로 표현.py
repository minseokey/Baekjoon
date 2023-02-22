def calc(lisa, lisb, setk):
    for i in lisa:
        for j in lisb:
            setk.add(i + j)
            setk.add(i - j)
            setk.add(i * j)
            if j:
                setk.add(i // j)

def serial(num,N):
    a = 0
    for i in range(num):
        a += (10**i) * N
    return a

def solution(N, number):
    a = [set() for i in range(10)]
    temp = set()
    temp.add(N)
    a[1] = temp
    
    if N == number:
        return 1

    for i in range(2, 9):
        tempset = set()
        tempset.add(serial(i, N))
        for j in range(1,i):
            calc(a[j], a[i-j], tempset)
        if number in tempset:
            return i
        else:
            a[i] = tempset

    return -1