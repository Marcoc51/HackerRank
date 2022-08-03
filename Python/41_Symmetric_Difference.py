m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
res = []
res += list(a.difference(b)) + list(b.difference(a))
res.sort()
for i in res:
    print(i)
