# string1 = input('Enter a string')


def unique_char_string(string):
    # # option #1
    # result = ''
    # for char in string:
    #     if result.count(char) == 0:
    #         result += char
    # # option #2
    # result = ''
    # for char in string:
    #     if char not in result:
    #         result += char
    #
    # # option #3
    # return ''.join(set(string))
    # # return result
    acc = 0
    num = string
    arr = [int(x) for x in num]
    for char in num:
        acc += int(char)
    return acc

print(unique_char_string('1371623'))