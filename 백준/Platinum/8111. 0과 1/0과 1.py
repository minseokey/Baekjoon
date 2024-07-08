from collections import deque

def find_kusa_number(N):
    if N == 0:
        return "BRAK"
    
    queue = deque(["1"])
    visited = set()
    
    while queue:
        num = queue.popleft()
        remainder = int(num) % N
        
        if remainder == 0:
            return num
        
        if (remainder, '0') not in visited:
            queue.append(num + "0")
            visited.add((remainder, '0'))
        
        if (remainder, '1') not in visited:
            queue.append(num + "1")
            visited.add((remainder, '1'))
    
    return "BRAK"

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    result = find_kusa_number(N)
    results.append(result)

for result in results:
    print(result)
