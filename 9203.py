def find_lines_len_more_6(file_name: str) -> int:
    count = 0
    with open(file_name, encoding='UTF-8') as file:
        for row in file.readlines():
            count += 1 if len(row) - 1 > 6 else 0
    return count


print(find_lines_len_more_6('test.txt'))
