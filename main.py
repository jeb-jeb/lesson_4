def sum_of_numbers(*args):
    result = 0
    for arg in args:
        if type(arg) != int:
            return 'Arg not a int'
        result += arg

    return result


def str_is_palindrome(initial_string):
    index = 0
    for reverse_index in range(len(initial_string), 0, -1):
        reverse_index -= 1
        if initial_string[reverse_index] != initial_string[index]:
            return False
        index += 1
    return True


def split_str_space(initial_str):
    result = ""
    split_str = initial_str.split()
    for i in split_str:
        result += i

    return result
