def longest_word(string):
    arr = string.split(' ')
    how_many_strings = len(arr)
    max_string = ''
    for index in range(len(arr)):
        if len(arr[index]) > len(max_string):
            max_string = arr[index]
    return max_string

# better way
#     arr = string.split(' ')
#     arr.sort(key=len)
#     return arr[-1]

print(longest_word('bu bir kusun hikayesi'))
