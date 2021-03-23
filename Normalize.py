def normalize(string):
    # return ' '.join((string.split(' ')))
    while string[0] == ' ':
        string = string[1:]
    while string[-1] == ' ':
        string = string[:-1]
    index = 0
    while index < len(string):
        if string[index] == ' ' and string[index + 1] == ' ':
            string = string[:index] + string[index + 1:]
        else:
            index += 1
    return string

print(normalize('asasa     jjkl s kkkkkkkkkkk     kkkkiii'))