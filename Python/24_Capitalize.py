def solve(s):
    result = ''
    for i in range(len(s)):
        if i == 0 or s[i - 1] == ' ':
            result += s[i].upper()
        else:
            result += s[i]
    return result
