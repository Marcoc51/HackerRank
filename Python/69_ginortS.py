low, upper, odd, even = [], [], [], []
for i in input():
    if i.islower():
        low.append(i)
    elif i.isupper():
        upper.append(i)
    elif type(eval(i)) is int:
        if int(i) % 2 == 1:
            odd.append(i)
        else:
            even.append(i)
low.sort()
upper.sort()
odd.sort()
even.sort()
res = low + upper + odd + even
print(''.join(res))
