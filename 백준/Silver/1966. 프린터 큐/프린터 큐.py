n = int(input())

for i in range(n):
    al,tar = map(int,input().split())
    lis = input().split()
    arr = []
    for j in range(al):
        arr.append({lis[j]:"normal"})
    arr[tar] = {lis[tar]:"target"}

    count = 1
    while(True):
        if list(arr[0].values())[0] == "target" and list(arr[0].keys())[0] == max(lis):
            print(count)
            break
        elif list(arr[0].keys())[0] == max(lis):
            count += 1
            del arr[0]
            lis.remove(max(lis))

        else:
            temp = arr[0]
            del arr[0]
            arr.append(temp)