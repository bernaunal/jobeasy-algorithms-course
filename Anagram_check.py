# str1 = input(f"First String :")
# str2 = input(f"Second String :")

def anagram_check(string1, string2):
    if not len(string1) == len(string2) and not string1 == string2:
        return False
    for char in string1:
        if not string1.count(char) == string2.count(char):
            return False
    return True


# print(anagram_check(str1, str2))

