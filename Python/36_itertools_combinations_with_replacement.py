from itertools import combinations_with_replacement

s, r = input().split()
r = int(r)
s_list = sorted(s)
s = ''.join(s_list)
res = list(combinations_with_replacement(s, r))
for i in res:
    print(''.join(i))
