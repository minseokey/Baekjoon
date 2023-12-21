import sys

def kmp_table(pattern):
    length = len(pattern)
    fail = [0] * length
    t = 0
    for i in range(1, length):
        while pattern[i] != pattern[t] and t > 0:
            t = fail[t-1]
        if pattern[i] == pattern[t]:
            t += 1
            fail[i] = t
    return fail

def kmp_search(pattern, string):
    fail = kmp_table(pattern)
    j = 0
    ans = []
    for i in range(len(string)):
        while j > 0 and string[i] != pattern[j]:
            j = fail[j-1]
        if string[i] == pattern[j]:
            if j == len(pattern)-1:
                ans.append(i-j + 1)
                j = fail[j]
            else:
                j += 1
    return ans

string = list(sys.stdin.readline().strip("\n"))
pattern = list(sys.stdin.readline().strip("\n"))

anslis = kmp_search(pattern, string)
print(len(anslis))
print(*anslis)