from collections import defaultdict

d = defaultdict(list)
A, B = map(int, input().split())
for i in range(A):
    d['A'].append(input())

for i in range(B):
    d['B'].append(input())

for i in range(len(d['B'])):
    if d['B'][i] in d['A']:
        for j in range(len(d['A'])):
            if d['B'][i] == d['A'][j]:
                print(j + 1, end=' ')
        print()
    else:
        print(-1)
