from collections import Counter

if __name__ == '__main__':
    s = input()
    count = Counter(sorted(s))
    for key, value in count.most_common(3):
        print(key, value)
