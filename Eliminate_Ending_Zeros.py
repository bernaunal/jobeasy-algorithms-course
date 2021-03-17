# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

def eliminate_ending_zeros(num):
    index = 0
    while index <= len(str(num)):
        if num % 10 == 0:
                num //= 10
        index += 1
    return num

print(eliminate_ending_zeros(-1050000))