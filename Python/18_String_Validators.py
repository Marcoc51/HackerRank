if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
        if s[i].isalnum():
            print(s[i].isalnum())
            break
        elif i == len(s) - 1:
            print(False)
    for i in range(len(s)):
        if s[i].isalpha():
            print(s[i].isalnum())
            break
        elif i == len(s) - 1:
            print(False)
    for i in range(len(s)):
        if s[i].isdigit():
            print(s[i].isalnum())
            break  
        elif i == len(s) - 1:
            print(False)   
    for i in range(len(s)):
        if s[i].islower():
            print(s[i].isalnum())
            break
        elif i == len(s) - 1:
            print(False)
    for i in range(len(s)):
        if s[i].isupper():
            print(s[i].isalnum())
            break
        elif i == len(s) - 1:
            print(False)
