import functools

# Напишите определение декоратора validate_args
def validate_args(func):
    @functools.wraps(func)
    def inner(*args):
        match len(args):
            case 0 | 1:     return 'Not enough arguments'
            case 2:         return 'Wrong types' if type(args[0]) is not int or type(args[1]) is not int else func(*args)
            case _:         return 'Too many arguments'
    return inner


# Код ниже не удаляйте, он нужен для проверки
@validate_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


assert add_numbers(4, 5) == 9
assert add_numbers(4) == 'Not enough arguments'
assert add_numbers() == 'Not enough arguments'
assert add_numbers('hello') == 'Not enough arguments'
assert add_numbers(3, 5, 6) == 'Too many arguments'
assert add_numbers('a', 'b', 'c') == 'Too many arguments'
assert add_numbers(4.5, 5.1) == 'Wrong types'
assert add_numbers('hello', 4) == 'Wrong types'
assert add_numbers(9, 'hello') == 'Wrong types'
assert add_numbers([1, 3], {}) == 'Wrong types'
assert add_numbers.__name__ == 'add_numbers'
assert add_numbers.__doc__.strip() == 'Return sum of x and y'
print('Good')
