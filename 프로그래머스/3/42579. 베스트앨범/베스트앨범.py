from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(list)
    
    for ind in range(len(genres)):
        dic[genres[ind]].append((ind, plays[ind]))
    
    
    cntdic = defaultdict(int)
    for i in dic.keys():
        for j in dic[i]:
            cntdic[i] += j[1]

    g_sort = sorted(cntdic.keys(), key = lambda x:cntdic[x], reverse = True)
    
    for i in dic.keys():
        dic[i].sort(key = lambda x:(-x[1],x[0]))
    
    ans = []
    for gen in g_sort:
        if len(dic[gen]) >= 2:
            ans.append(dic[gen][0][0])
            ans.append(dic[gen][1][0])
        else:
            ans.append(dic[gen][0][0])
            
    return ans
    