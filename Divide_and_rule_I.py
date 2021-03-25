def power_dac(number, power):
    if power < 0:
        return 'exception'
    if power == 0:
        return 1
    if power == 1:
        return number
    if power % 2 == 0:
        temp = power_dac(number, power / 2)
        return temp * temp
    return number * power_dac(number, power - 1)


print(power_dac(8, 100))

