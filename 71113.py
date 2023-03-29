marks = {}
while True:
    record = input()
    match record:
        case 'конец':
            break
        case _:
            name, mark = record.split(', ')
            marks.setdefault(name, []).append(int(mark))

for key, value in sorted(marks.items(), key=lambda pair: (-sum(pair[1]) / len(pair[1]), pair[0])):
    print(key, sum(value) / len(value))