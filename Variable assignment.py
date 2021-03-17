# a = int(input('Input value a '))
# b = int(input('Input value b '))
#
# print(f'a = {a}, b = {b}')

# option 1
# temp = a
# a = b
# b = temp

# option 2
# a = a + b
# b = a - b
# a = a - b

# option 3
a, b = 10, 5
print(f'a = {a}, b = {b}')

a, b = b, a
a, b = b, a + 100

print(f'a = {a}, b = {b}')