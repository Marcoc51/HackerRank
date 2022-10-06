import re

for i in range(int(input())):
    name, mail = input().split()
    exp = r'\b[a-zA-Z]([\w\.-])+@([a-z])+\.+([a-z]{1,3})'
    m = re.fullmatch(exp, mail[1:-1])
    if m:
        print(name, mail)
