n = int(input())
s = set(map(int, input().split()))
num = int(input())
for i in range(num):
    command = input()
    try:
        if len(command) > 3:
            cmd, item = command.split()
            if cmd == 'remove':
                s.remove(int(item))
            else:
                s.discard(int(item))
        else:
            s.pop()
    except KeyError:
        pass
print(sum(s))
