def string_compress(string):
    counter = 1
    result = string[0]
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            counter += 1
        else:
            if counter > 1:
                result += str(counter)
                counter = 1
            result += string[index + 1]
    else:
        if counter > 1:
            result += str(counter)
    return result


print(string_compress('aaaabbbbbcccdddd'))