def factorial_rec(num):
    if num < 0:
        return 'Only positive numbers'
    if num == 0 or num == 1:
        return 1
    return num * factorial_rec(num - 1)

print(factorial_rec(5))