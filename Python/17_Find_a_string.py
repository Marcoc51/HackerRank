def count_substring(string, sub_string):
    res = 0
    for i in range(len(string)):
        try:
            if sub_string == string[i:i+len(sub_string)]:
                res += 1
        except:
            break
    return res
