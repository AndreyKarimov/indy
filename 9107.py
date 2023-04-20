def create_file_with_numbers(n: int):
    file = open(f'range_{n}.txt', mode='a', encoding='UTF-8')
    [file.write(str(i)+'\n') for i in range(1, n+1)]
    file.close()


create_file_with_numbers(10)

    # file = open(f'range_{n}.txt', mode='r', encoding='UTF-8')
