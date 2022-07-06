def print_rangoli(size):
    # your code goes here
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    code = (size - 1) * 2
    asc = alpha[:size]
    desc = alpha[:size]
    desc.reverse()
    
    for i in range(size):
        print('-' * code, end='')
        print(('-').join(desc[: i + 1]), end='')
        if i > 0:
            print('-', end='')
            print(('-').join(asc[- i:]), end='')
        print('-' * code)
        code -= 2
    
    code += 2
    
    for i in range(size - 2, -1, -1):
        code += 2
        print('-' * code, end='')
        print(('-').join(desc[: i + 1]), end='')
        if i > 0:
            print('-', end='')
            print(('-').join(asc[- i:]), end='')
        print('-' * code)
    
