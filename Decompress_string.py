def decompress_string(string):
    result = ''
    count = ''
    for ch in string[::-1]:
        if ch.isalpha():
            if len(count) > 0:
                result += ch * int(count[::-1])
                count = ''
            else:
                result += ch
        if ch.isdigit():
            count += ch
    return result[::-1]


print(decompress_string('a4b5c3d4'))

