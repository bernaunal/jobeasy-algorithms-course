def get_divisors(num):
    result = []
    for item in range(1, num):
        if num % item == 0:
            result.append(item)
    return result

print(get_divisors(20))