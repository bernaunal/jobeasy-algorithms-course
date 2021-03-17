def to_bin(number):
    result = ''

    # while number > 0:
    #     result += str(number % 2)
    #     number //= 2
    # return result[::-1]


    while number > 0:
        number, remainder = divmod(number, 2)
        result += str(remainder)
    return result[::-1]

# print(f'0b'+to_bin(256))
# 10001001
# print(str(bin(256))[2:])
# print(to_bin(256))

def bin_gap(bin_number):
    max_gap = 0
    counter = 0
    for item in str(bin_number):
        if item == '0':
            counter += 1
        elif item == '1':
            if counter > 0 and counter > max_gap:
                max_gap = counter
            counter = 0
    return max_gap

print(to_bin(21113345))
print(bin_gap(to_bin(21113345)))

