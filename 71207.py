def calculate(x: float, y: float, operation: str = 'a') -> None:
    def addition(a: float, b: float):
        print(float(a + b))

    def subtraction(a: float, b: float):
        print(float(a - b))

    def division(a: float, b: float):
        print(a / b if b != 0 else 'На ноль делить нельзя!')

    def multiplication(a: float, b: float):
        print(float(a * b))

    match operation:
        case 'a':            addition(x, y)
        case 's':            subtraction(x, y)
        case 'd':            division(x, y)
        case 'm':            multiplication(x, y)
        case _:              print('Ошибка. Данной операции не существует')


calculate(int(input()), int(input()), input())
