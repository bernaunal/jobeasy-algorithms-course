from Get_divisors import get_divisors

def is_perfect(num):
    return num == sum(get_divisors(num, False))

print(is_perfect(28))