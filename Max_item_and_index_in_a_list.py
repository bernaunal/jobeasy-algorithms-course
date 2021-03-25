from random import randint
# lowest = int(input('From number: '))
# highest = int(input('To number: '))
#
# length = int(input(f"Enter the lentgh of the list: "))
# array_1 =[]
#
# for i in range(length):
#     item = randint(lowest, highest)
#     array_1.append(item)


def find_maxitem_and_index_inlist(array):
    max_value = array[0]
    max_index = 0
    index = 0
    while index < len(array):
        if max_value < array[index]:
            max_value = array[index]
            max_index = index
        index += 1
    return max_value
    # {
    #     'array': array,
    #     'max_value': max_value,
    #     'max_index': max_index
    # }

# print(find_maxitem_and_index_inlist(array_1))