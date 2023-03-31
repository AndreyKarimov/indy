def create_accumulator(start: int = 0):
    def inner(num: int):
        nonlocal start
        start += num
        return start

    return inner


summator_1 = create_accumulator(100)
print(summator_1(1)) # печатает 101
print(summator_1(5)) # печатает 106
print(summator_1(2)) # печатает 108
print('_________________________')
summator_2 = create_accumulator()
print(summator_2(3)) # печатает 3
print(summator_2(4)) # печатает 7