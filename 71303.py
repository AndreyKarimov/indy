def create_accumulator():
    sum_ = 0

    def inner(num: int):
        nonlocal sum_
        sum_ += num
        return sum_

    return inner


summator_1 = create_accumulator()
print(summator_1(1)) # печатает 1
print(summator_1(5)) # печатает 6
print(summator_1(2)) # печатает 8
print('---------------------------')
summator_2 = create_accumulator()
print(summator_2(3)) # печатает 3
print(summator_2(4)) # печатает 7