a = int(input())
a_set = set(map(int, input().split()))

for i in range(int(input())):
    command, n = input().split()
    if command == "intersection_update":
        a_set.intersection_update(set(map(int, input().split())))
    elif command == "update":
        a_set.update(set(map(int, input().split())))
    elif command == "symmetric_difference_update":
        a_set.symmetric_difference_update(set(map(int, input().split())))
    else:
        a_set.difference_update(set(map(int, input().split())))

print(sum(a_set))
