def revert_int_option_1(x: int) -> int:
    """ Напишите программу, которая развернет число (тип int) """
    #return int(str(x)[::-1])
    return int(''.join(list(reversed(str(x)))))




print(revert_int_option_1(123))