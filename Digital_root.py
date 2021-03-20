# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
from random import randint


def sum_of_digits(number):
    # down = 10 ** (digits - 1)
    # up = (10 ** digits) - 1
    # random_value = randint(down, up)

    sum_of_digits = 0
    for char in str(number):
        sum_of_digits += int(char)
    return sum_of_digits

# print(sum_of_digits(3))

def digital_root(num):
    while num > 9:
        num = sum_of_digits(num)
    return num


# print(digital_root(2244))