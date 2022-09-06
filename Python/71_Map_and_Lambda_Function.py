cube = lambda x:x ** 3 

def fibonacci(n):
    if n == 0:
        fib = []
    elif n == 1:
        fib = [0]
    elif n == 2:
        fib = [0, 1]
    else:
        fib = [0, 1]
        for i in range(1, n - 1):
            fib.append(fib[i] + fib[i - 1]) 
    return fib
