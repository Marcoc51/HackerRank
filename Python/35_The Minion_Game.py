def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = {'Kevin': 0, 'Stuart': 0}
    for i in range(len(string)): 
        if string[i] in vowels:
            result['Kevin'] += len(string) - i
        else:
            result['Stuart'] += len(string) - i
    if result['Stuart'] > result['Kevin']:
        print(f"Stuart {result['Stuart']}")
    elif result['Stuart'] < result['Kevin']:
        print(f"Kevin {result['Kevin']}")
    else:
        print("Draw")
