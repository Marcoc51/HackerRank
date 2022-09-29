for _ in range(int(input())):
    try:
        num = input()
        if float(num) and num.find('.'):
            print(True)
        else:
            print(False)
    except:
        print(False)
