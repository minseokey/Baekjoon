def solution(begin, target, words):
    # using dfs

    ans = []

    def dfs(now, wordlis, checklist1, count):
        if now == target:
            ans.append(count)
        templis = []
        for i in wordlis:
            # checking words
            temp = 0
            for j in range(len(now)):
                if now[j] != i[j]:
                    temp += 1
            if temp == 1 and not checklist1[wordlis.index(i)]:
                templis.append(i)

        for k in templis:
            newchecklist = checklist1
            newchecklist[wordlis.index(k)] = True
            dfs(k, wordlis, newchecklist, count+1)

    checklist = [False for i in range(len(words))]
    dfs(begin, words,checklist,0)
    print(ans)
    return min(ans) if ans else 0