import sys 
input = sys.stdin.readline
r = int(input())

for i in range(0,r):
    a,b = map(int,input().split())
    print(a + b)