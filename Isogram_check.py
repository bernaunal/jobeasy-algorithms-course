from Anagram_check import anagram_check


def isogram_check(string):
    unique_str = ''.join(list(set(string)))
    return anagram_check(unique_str, string)


print(isogram_check('abscs'))