def multiply(a: int):
    def inner(b: int):
        nonlocal a
        b *= a
        return b

    return inner


f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5)) #10
print("Умножение 2 на 15 =", f_2(15)) #30
f_3 = multiply(3)
print('_________________________')
print("Умножение 3 на 5 =", f_3(5)) #15
print("Умножение 3 на 15 =", f_3(15)) #45