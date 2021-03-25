from random import randint

length = int(input('Enter a number of items: '))
list_numbers = []

for _ in range(length):
    list_numbers.append(randint(-20, 20))

def largest_sum_continuos_sublist(arr):
    best_sublist = [arr[0]]
    best_sublist_sum = arr[0]
    index_1 = 0
    while index_1 < len(arr):
        index_2 = index_1 + 1
        current_sublist = [arr[index_1]]
        current_sublist_sum = arr[index_1]
        while index_2 < len(arr):
            current_sublist_sum += arr[index_2]
            current_sublist.append(arr[index_2])
            if current_sublist_sum > best_sublist_sum:
                best_sublist_sum = current_sublist_sum
                best_sublist = current_sublist
            index_2 += 1
        index_1 += 1
    return {
        'sum': best_sublist_sum,
        'sublist': best_sublist,
    }

print(largest_sum_continuos_sublist(list_numbers))
