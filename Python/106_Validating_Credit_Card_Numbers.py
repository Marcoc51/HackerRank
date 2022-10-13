import re

regex = r'\b[456][0-9]{3}(-?[0-9]{4}){3}$'
for _ in range(int(input())):
    s = input()
    if re.match(regex, s) and (len(s) == 16 or len(s) == 19):
        s = ''.join(s.split('-'))
        if re.search(r'([0-9])\1{3}', s):
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')
