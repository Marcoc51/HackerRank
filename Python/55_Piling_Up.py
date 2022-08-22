for _ in range(int(input())):
    res = "Yes"
    l = []
    s = int(input())
    b = list(map(int, input().split()))
    for i in range(s):
        if b[0] >= b[-1]:
            l.append(b.pop(0))
        else:
            l.append(b.pop(-1))
        if len(l) > 1 and l[-1] > l[-2]:
            res = "No"
            break
    print(res)
