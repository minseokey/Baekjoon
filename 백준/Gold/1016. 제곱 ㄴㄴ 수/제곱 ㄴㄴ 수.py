mi, ma = map(int, input().split())
validate = [1 for i in range(ma - mi + 1)]
cnt = 0
i = 2
while i ** 2 <= ma:
    mul = mi // i ** 2
    while mul * (i ** 2) <= ma:
        if 0 <= mul * (i ** 2) - mi <= ma - mi:
            validate[mul * (i ** 2) - mi] = 0
        mul += 1
    i += 1

print(sum(validate))