def count_unic_word(file_name: str) -> dict:
    words = {}
    with open(file_name, encoding='UTF-8') as file:
        for word in file.read().upper().split():
            words[word] = words.setdefault(word, 0) + 1
    return words


words = count_unic_word('lorem.txt')
