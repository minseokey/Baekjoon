ga = ['A','B','C']
gb = ["D","E","F"]
gc = ['G','H','I']
gd = ['J','K','L']
ge = ['M','N','O']
gf = ['P','Q','R','S']
gg = ['T','U','V']
gh = ['W','X','Y','Z']
a = str(input())
t = 0
for i in range(0,len(a)):
    if a[i] in ga:
        t = t + 3
    elif a[i] in gb:
        t = t + 4
    elif a[i] in gc:
        t = t + 5
    elif a[i] in gd:
        t = t + 6
    elif a[i] in ge:
        t = t + 7
    elif a[i] in gf:
        t = t + 8
    elif a[i] in gg:
        t = t + 9
    elif a[i] in gh:
        t = t + 10
print(t)