a_set = set(map(int, input().split()))
for i in range(int(input())):
    if a_set.issuperset(set(map(int, input().split()))):
        out = True
    else:
        out = False
        break
print(out)
