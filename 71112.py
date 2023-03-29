classmate_list = {}

for _ in range(int(input())):
    name, _, month = list(input().split())
    classmate_list.setdefault(month, []).append(name)

for _ in range(int(input())):
    print(*classmate_list.get(input(), ['Нет данных']))