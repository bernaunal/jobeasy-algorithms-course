from Digital_root import sum_of_digits


def digital_root_rec(num):
    if num < 10:
        return num
    return digital_root_rec(sum_of_digits(num))

# print(digital_root_rec(165))