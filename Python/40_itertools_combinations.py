from itertools import combinations

s, r = input().split()
r = int(r)
s_list = sorted(s)
s = ''.join(s_list)
res = []
for i in range(r + 1):
    res += list(combinations(s, i))
res.pop(0)
for i in res:
    print(''.join(i))
