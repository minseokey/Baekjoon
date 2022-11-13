num = int(input())
foi = 1
Fira = num // 10
Firb = num % 10
Summ = 10 * Firb + (Fira + Firb) % 10
while not num == Summ:
    a = 0
    b = 0
    a = Summ // 10
    b = Summ % 10
    Summ = 10*b + ((a + b) % 10)
    foi = foi + 1
print(foi)
