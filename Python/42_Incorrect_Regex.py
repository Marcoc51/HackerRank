import re

for i in range(int(input())):
    try:
        re.findall(input(), 'aaaa')
        print(True)
    except:
        print(False)
