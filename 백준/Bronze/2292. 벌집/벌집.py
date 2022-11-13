n = int(input())
k = 0
t = 0
ques = float((n - 2) / 6)
while True:
    t = t + 1
    k = k + t

    if n == 1:
        print(1)
        break
    elif ques < float(k):
        print(t+1)
        break