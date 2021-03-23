def palindrome_check(string_to_be_tested):
    return string_to_be_tested == string_to_be_tested[::-1]


print(palindrome_check('rasdar'))