def count_num(file_name: str) -> int:
    count = 0
    sum_ = 0
    with open(file_name, encoding='UTF-8') as file:
        for number in file.read().split():
            count += 1 if 99 < int(number) < 1000 else 0
            sum_ += int(number) if 9 < int(number) < 100 else 0
    print(f'количество трехзначных чисел: {count}')
    print(f'сумму двухзначных чисел: {sum_}')


count_num('numbers.txt')
