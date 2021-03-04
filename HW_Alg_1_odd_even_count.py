"""
Count odd and even numbers.  Count odd and even digits of the whole number.
E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).
"""
number = input('Enter a number: ')

even = 0
odd = 0

i = 0

while i < len(number):
    if int(number[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1
print(f'Even: {even} Odd: {odd}')


