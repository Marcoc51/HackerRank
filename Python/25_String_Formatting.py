def print_formatted(number):
    rb = len(bin(number).replace("0b", ''))
    for i in range(1, number + 1):
        print(str(i).rjust(rb), end=' ')
        print(oct(i).replace("0o", '').rjust(rb), end=' ')
        print(hex(i).replace("0x", '').rjust(rb).upper(), end=' ')
        print(bin(i).replace("0b", '').rjust(rb))
