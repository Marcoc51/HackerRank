if n%2 == 1:
        print("Weird")
    else:
        if n in [i for i in range(2, 6)]:
            print("Not Weird")
        elif n in [i for i in range(6, 21)]:
            print("Weird")
        else:
            print("Not Weird")
