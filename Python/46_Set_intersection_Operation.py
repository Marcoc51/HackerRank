n = int(input())
n_set = set(input().split())

b = int(input())
b_set = set(input().split())

total = n_set.intersection(b_set)
print(len(total))
