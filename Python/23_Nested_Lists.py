if __name__ == '__main__':
    std = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        std.append([name, score])
    
    min_num = std[0][1]
    index = [0]
    for i in range(1, len(std)):
        if std[i][1] < min_num:
            min_num = std[i][1]
            index[0] = i
    
    for i in range(len(std)):
        if std[i][1] == min_num and i not in index:
            index.append(i)
    index.reverse()    
    for i in index:
        std.pop(i)
    sol = [std[0][0]]
    min_num = std[0][1]
    for i in range(1, len(std)):
        if std[i][1] < min_num:
            min_num = std[i][1]
            sol[0] = std[i][0]
        elif std[i][1] == min_num:
            sol.append(std[i][0])
    
    sol.sort()
    for i in sol:
        print(i)
