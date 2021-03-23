def delete_fragment(string, char):
    # first = 0
    # last = 0
    # index = 0
    # while index < len(string):
    #     if string[index] == char:
    #         first = index
    #         break
    #     index += 1
    # index = len(string) - 1
    # while index >= 0:
    #     if string[index] == char:
    #         last = index
    #         break
    #     index -= 1
    # return string[:first] + string[last + 1:]

    first = string.find(char)
    last = string.rfind(char)

    return string[:first] + string[last + 1:]

print(delete_fragment('aaaarffffddddddsssssrssss','r'))

