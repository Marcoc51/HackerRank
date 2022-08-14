from collections import deque

d = deque()
for i in range(int(input())):
    command = input()
    if command[:3] == 'pop':
        if command == 'pop':
            d.pop()
        elif command == 'popleft':
            d.popleft()
    else:
        comm, num = command.split()
        if comm == 'append':
            d.append(num)
        elif comm == 'appendleft':
            d.appendleft(num)

for i in d:
    print(i, end=' ')
