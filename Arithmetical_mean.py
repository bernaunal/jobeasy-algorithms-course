from random import randint

length = int(input('Enter a number of items: '))
list_numbers = []


for _ in range(length):
    list_numbers.append(randint(1, 10))
print(list_numbers)


def ar_mean(arr):
    result = []
    arith_mean = sum(arr) / len(arr)
    for item in arr:
        if item < arith_mean:
            result.append(item)
    return result


print(ar_mean(list_numbers))