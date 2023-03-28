contactList = {}

for _ in range(int(input())):
    number, name = input().split()
    if name not in contactList:
        contactList[name] = [number]
    else:
        contactList.get(name).append(number)

for _ in range(int(input())):
    name = input()
    if name in contactList:
        print(*contactList[name])
    else:
        print('Неизвестный номер')