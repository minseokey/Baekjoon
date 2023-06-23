count = 0
while True:
    try:
        inp = input()
        count+=1
    except EOFError:
        break



print(count)