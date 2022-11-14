import collections
def solution(nums):
    a = dict(collections.Counter(nums))
    vala = list(a.values())
    pickNum = len(nums)//2

    if len(vala) >= pickNum:
        return pickNum
    else:
        count = set()
        countNum = 0
        while True:
            for i in a.keys():
                a[i] -= 1
                countNum += 1
                count.add(i)
                if countNum == pickNum:
                    return len(count)