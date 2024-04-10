def is_palindrome(string: str):
    # return string == string[::-1]
    # return string == ''.join(reversed(string))
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            return False

        return True

""""
def foo(value):
    if len(value) == 0:
        return True
    if value[0] != value[-1]:
        return False
    return foo(value[1:-1])

print(foo('aboba'))
print(foo('ffqqd'))

"""