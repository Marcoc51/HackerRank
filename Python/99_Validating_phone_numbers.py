import re

for i in range(int(input())):
    s = input()
    m = re.findall(r'^([789])(\d){9}', s)
    if m:
        if len(s) == 10:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
