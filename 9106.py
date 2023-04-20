def file_n_lines(file_name: str, n: int) -> None:
    rows = open(file_name, encoding='UTF-8')
    for row in rows.readlines():
        print(row[:-1])
        n -= 1
        if n <= 0:
            rows.close()
            break


file_n_lines('test.txt', 3)
