from Get_divisors import get_divisors


def in_list(num, list_of_numbers):
    return num in list_of_numbers


def gcd(num1, num2):
    divisor_num1 = get_divisors(num1)
    divisor_num2 = get_divisors(num2)

    result = []
    for num in divisor_num1:
        if in_list(num, divisor_num2):
            result.append(num)
    return max(result)
    # return result[-1]
    # print(divisor_num1)
    # print(divisor_num2)


print(gcd(24, 16))