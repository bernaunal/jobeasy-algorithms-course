from random import randint

length = int(input('Enter a number of items: '))
list_numbers = []


for _ in range(length):
    list_numbers.append(randint(1, 10))
print(list_numbers)

# def two_mins(array):
#     result =[]
#     min_element = min(array)
#     result.append(min_element)
#     array.remove(min_element)
#     min_element = min(array)
#     result.append(min_element)
#     return result

def n_mins(array, n):
    result = []
    if len(array) < n:
        n = len(array)
    for _ in range(n):
        min_element = min(array)
        result.append(min_element)
        array.remove(min_element)
    return result


print(n_mins(list_numbers, 3))

    # min_value = array[0]
    # min_index = 0
    # index = 0
    # while index < len(array):
    #     if min_value > array[index]:
    #         min_value = array[index]
    #         min_index = index
    #     index += 1
    # return {
    #     'array': array,
    #     'min_value': min_value,
    #     'min_index': min_index
    # }
