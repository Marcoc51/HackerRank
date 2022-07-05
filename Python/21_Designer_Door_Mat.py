n, m = input().split()
n = int(n)
m = int(m)
mul = 3

for i in range(1, n, 2):
    num = (m-mul) // 2
    print('-' * num, end='')
    print('.|.'*i, end='')
    print('-' * num)
    mul += 6

num = (m-len("WELCOME")) // 2
print('-' * num, end='')
print("WELCOME", end='')
print('-' * num)

for i in range(n-2, 0, -2):
    mul -= 6
    num = (m-mul) // 2
    print('-' * num, end='')
    print('.|.'*i, end='')
    print('-' * num)
