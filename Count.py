def count_chars(string, substring, start, end):
    counter = 0
    if len(string) < len(substring):
        return counter
    # option #1
    # while string.find(substring) > -1:
    #     counter += 1
    # option #2
    index = string.find(substring, start, end)
    while index > -1:
        index = string.find(substring, index + 1, end)
        counter += 1
    return counter

print(count_chars('hello hero heman', 'he', 2, 20))