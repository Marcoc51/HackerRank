from collections import OrderedDict

items = OrderedDict()
nums = int(input())
for i in range(nums):
    item_list = input().split()
    price = int(item_list.pop())
    item = ' '.join(item_list)
    if item in items.keys():
        items[item] += price
    else:
        items[item] = price
for key, value in items.items():
    print(f'{key} {value}')
