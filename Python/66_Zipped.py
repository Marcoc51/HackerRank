n, x = map(int, input().split())
degrees = []
for i in range(x):
    degrees.append(list(map(float, input().split())))
for i in list(zip(*degrees)):
    print(round(sum(i) / len(i), 1))
