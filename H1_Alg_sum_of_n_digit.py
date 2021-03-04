"""
Rewrite a program with any number of digits.
Instead of  3 digits, you should sum digits up from n digits number,
Where User enter n manually. n > 0
"""

number = input('Enter a number: ')
sum_of_digits = 0
i = 0

while i < len(number):
    sum_of_digits += int(number[i])
    i += 1

print(sum_of_digits)
