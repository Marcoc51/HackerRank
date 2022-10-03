import re

s = input()
k = input()
res = []
for i in range(len(s)):
    m = re.search(k, s[i: i+len(k)])
    if m:
        res.append((m.start() + i, m.end() - 1 + i))
if res:
    print(*res, sep='\n')
else:
    print((-1, -1))
