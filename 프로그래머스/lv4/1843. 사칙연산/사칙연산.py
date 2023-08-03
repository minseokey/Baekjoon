def solution(arr):
    num = []
    al = []
    for i in range(len(arr)):
        if i % 2 == 0:
            num.append(int(arr[i]))
        else:
            al.append(arr[i])
    
        
    dp_min = [[float('inf') for _ in range(len(num))] for _ in range(len(num))]
    dp_max = [[float('-inf') for _ in range(len(num))] for _ in range(len(num))]
    
    
    N = len(num)

    # diff
    for i in range(N):
        # start
        for j in range(N-i):
            start = j
            end = j+i
            if i == 0:
                dp_max[start][start] = dp_min[start][start] = num[start]
            # mid
            else:
                for mid in range(start,end):
                    if al[mid] == "+":
                        dp_max[start][end] = max(dp_max[start][mid] + dp_max[mid+1][end],dp_max[start][end])
                        dp_min[start][end] = min(dp_min[start][mid] + dp_min[mid+1][end],dp_min[start][end])
                    elif al[mid] == "-":
                        dp_max[start][end] = max(dp_max[start][mid] - dp_min[mid+1][end],dp_max[start][end])
                        dp_min[start][end] = min(dp_min[start][mid] - dp_max[mid+1][end],dp_min[start][end])
            
    return dp_max[0][-1]