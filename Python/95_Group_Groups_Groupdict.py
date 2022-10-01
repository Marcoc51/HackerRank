import re

m = re.search(r'([a-zA-Z0-9])\1+', input())

if m:
    print(m.group(1))
else:
    print(-1)
