def sum_of_numbers(*args):
    result = 0
    for arg in args:
        if type(arg) != int:
            return 'Arg not a int'
        result += arg

    return result
