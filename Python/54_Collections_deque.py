from collections import deque

d = deque()
for i in range(int(input())):
    command = input()
    if command[:3] == 'pop' or command[:3] == 'rev' or command[:3] == 'cle':
        if command == 'pop':
            d.pop()
        elif command == 'popleft':
            d.popleft()
        elif command == 'reverse':
            d.reverse()
        elif command == 'clear':
            d.clear
    else:
        comm, num = command.split()
        if comm == 'append':
            d.append(num)
        elif comm == 'appendleft':
            d.appendleft(num)
        elif comm == 'extend':
            d.extend(num)
        elif comm == 'extendleft':
            d.extendleft(num)
        elif comm == 'count':
            d.count(num)
        elif comm == 'remove':
            d.remove(num)
        elif comm == 'rotate':
            d.rotate(num)

for i in d:
    print(i, end=' ')
