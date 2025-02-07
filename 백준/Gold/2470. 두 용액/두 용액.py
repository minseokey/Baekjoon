import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

maxx = (float('INF'), 0, 0)

start = 0
end = len(nums)-1

while end - start > 0:
    if maxx[0] > abs(nums[end] + nums[start]):
        maxx = (abs(nums[end] + nums[start]), start, end)

    if nums[end] + nums[start] > 0:
        end -= 1
    else:
        start += 1


print(nums[maxx[1]], nums[maxx[2]])