from Get_divisors import get_divisors

def is_amicable(num_1, num_2):
    div_num_1 = get_divisors(num_1, False)
    div_num_2 = get_divisors(num_2, False)

    return num_1 == sum(div_num_2) and num_2 == sum(div_num_1)

print(is_amicable(220, 284))
