def fibonacci_rec(n):
    if n < 0:
        return 'Not a valid value'
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


print(fibonacci_rec(10))

