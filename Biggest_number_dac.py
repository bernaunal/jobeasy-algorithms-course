from Max_item_and_index_in_a_list import find_maxitem_and_index_inlist


def biggest_number_dac(list_1):
    list_len = len(list_1)
    max_number1 = 0
    max_number2 = 0

    if list_len == 0:
        return 'Exception. Empty list'
    if list_len == 1:
        return list_1[0]
    if list_len % 2 == 0:
        max_number1 = find_maxitem_and_index_inlist(list_1[0:int(list_len/2)])
        max_number2 = find_maxitem_and_index_inlist(list_1[int(list_len/2 - 1) + 1:list_len])
    else:
        max_number1 = find_maxitem_and_index_inlist(list_1[0:int(list_len / 2)])
        max_number2 = find_maxitem_and_index_inlist(list_1[int(list_len / 2 ):list_len])
    if int(max_number1) > int(max_number2):
        return int(max_number1)
    else:
        return int(max_number2)

# print(biggest_number_dac([ ]))
# print(biggest_number_dac([3]))
print(biggest_number_dac([1,2,3,44,33,11,234,555,22,1,78,869,121]))