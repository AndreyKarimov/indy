def searsh_eya(file_name: str) -> None:
    with open(file_name, encoding='UTF-8') as file:
        set_ = set(x for x in file.read().upper().split() if x.endswith('ЕЯ'))
        print(*sorted(set_, key=lambda x: (len(x), x)), sep='\n')
searsh_eya('words.txt')