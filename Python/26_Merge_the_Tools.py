def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        res = string[i : i + k]
        sub = ''
        for j in range(len(res)):
            if res[j] not in sub:
                sub += res[j]
        print(sub)
