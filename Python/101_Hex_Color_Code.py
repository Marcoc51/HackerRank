import re

regex = r'[\s:](#[0-9A-Fa-f]{3}\b|#[A-Fa-f0-9]{6}\b)'
for _ in range(int(input())):
    s = input()
    m = re.findall(regex, s)
    if m:
        print(*m, sep='\n')
