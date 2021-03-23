length = int(input(f"Enter the length of a list: "))
array_1 = []

for item in range(length):
    number = int(input(f"Enter a value of element: "))
    array_1.append(number)


def sum_and_mult(array):
    sum_of_list = 0
    mult_of_list = 1
    for item in array:
        sum_of_list += item
        mult_of_list *= item
    return {
        'array': array,
        'sum': sum_of_list,
        'mult': mult_of_list
    }


print(sum_and_mult(array_1))