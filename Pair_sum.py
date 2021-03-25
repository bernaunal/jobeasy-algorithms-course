def pair_sum(arr, k):
    result = []
    index_1 = 0
    while index_1 < len(arr) - 1:
        index_2 = index_1 + 1
        while index_2 < len(arr):
            if arr[index_1] + arr[index_2] == k:
                result.append((arr[index_1], arr[index_2]))
                break
            index_2 += 1
        index_1 += 1
    result = list(set(result))
    return result


print(pair_sum([1, 3, 4, 6, 0, 2, 3, 9, -1, 2, -1], 4))

