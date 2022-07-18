from collections import Counter

num_of_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_of_customers = int(input())

shoe_num = Counter(shoe_sizes)
total = 0

for i in range(num_of_customers):
    order = list(map(int, input().split()))
    if order[0] in shoe_num.keys() and shoe_num[order[0]] > 0:
        shoe_num[order[0]] -= 1
        total += order[1]

print(total)
