import re

for _ in range(int(input())):
    s = input()
    if len(set(s)) == 10 and s.isalnum() and re.match(r'(.*[A-Z].*){2,}', s) and re.match(r'(.*[0-9].*){3,}', s):
        print('Valid')
    else:
        print('Invalid')
