def replace(string, old_substring, new_substring):
    len_old_substring = len(old_substring)
    index = string.find(old_substring)

    while index > -1:
        string = string[:index] + new_substring + string[index + len_old_substring:]
        index = string.find(old_substring, index + len(new_substring))
    return string


print('aaaabbbcccdddaa'.replace('aa','z'))
print(replace('aaaabbbcccdddaa','aa','z'))