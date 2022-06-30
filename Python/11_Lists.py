    N = int(input())
    res = []
    for i in range(N):
        cmd = input()
        if cmd[:6] == "insert":
                res.insert(int(cmd[7]), int(cmd[9:]))
        elif cmd[:5] == "print":
            print(res)
        elif cmd[:6] == "remove":
            res.remove(int(cmd[7:]))
        elif cmd[:6] == "append":
            res.append(int(cmd[7:]))
        elif cmd[:4] == "sort":
            res.sort()
        elif cmd[:3] == "pop":
            res.pop()
        elif cmd[:7] == "reverse":
            res.reverse()
