a = input()
b = input()
c = input()

lis = ["Fizz", "Buzz", "FizzBuzz"]
temp = 0
if a not in lis:
    temp = int(a) + 3
elif b not in lis:
    temp = int(b) + 2
elif c not in lis:
    temp = int(c) + 1

if temp%5 == 0 and temp%3 == 0:
    print("FizzBuzz")
elif temp%3 == 0:
    print("Fizz")
elif temp%5 == 0:
    print("Buzz")
else:
    print(temp)
