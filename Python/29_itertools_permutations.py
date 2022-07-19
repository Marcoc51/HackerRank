from itertools import permutations

string, k = input().split()
k = int(k)
per = list(permutations(string, k))
ans = []
for i in per:
    res = ''
    for j in i:
        res += j
    ans.append(res)

ans.sort()
for i in ans:
    print(i)
