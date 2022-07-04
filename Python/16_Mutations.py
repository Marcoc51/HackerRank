def mutate_string(string, position, character):
    s = ""
    for i in range(len(string)):
        if i == position:
            s += character
        else:
            s += string[i]
    return s
