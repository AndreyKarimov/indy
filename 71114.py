unicComment = {
    'Дили' : set(),
    'Били' : set(),
    'Вили' : set(),
}
while True:
    line = input()
    if line == 'конец':
        break
    else:
        name, name_comm = line.split(': ')
        unicComment.get(name).add(name_comm)

for key, value in sorted(unicComment.items(), key=lambda x: len(x[1]), reverse=True):
    print(f'Количество уникальных комментаторов у {key} - {len(value)}')


