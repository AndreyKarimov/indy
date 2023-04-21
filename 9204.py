def count_unic_word(file_name: str) -> int:
    with open(file_name, encoding='UTF-8') as file:
        return len(set(file.read().lower().split()))


print(count_unic_word('lorem.txt'))