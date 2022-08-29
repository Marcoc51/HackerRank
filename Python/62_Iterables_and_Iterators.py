from itertools import combinations

n = int(input())
items = input().split()
k = int(input())
count = 0
res = list(combinations(range(1, n + 1), k))
index = [i + 1 for i in range(n) if 'a' == items[i]]
for i in range(len(res)):
    for j in range(len(index)):
        if index[j] in res[i]:
            count += 1
            break
print(round(count / len(res), 3))
