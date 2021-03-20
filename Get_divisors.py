def get_divisors(num, include_last_num:bool):
    result = []
    if include_last_num:
        needed_range = range(1, num + 1)
    else:
        needed_range = range(1, num)

    for item in needed_range:
        if num % item == 0:
            result.append(item)

    return result

# print(get_divisors(20))