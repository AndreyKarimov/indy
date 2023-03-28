a = input().split(': ')
result = {}
while a != 'конец' and len(a)>1:
    result[a[0]] = int(a[1])
    a = input().split(': ')
[print(item) for item, value in sorted(result.items(), key=lambda pair: -pair[1])]



