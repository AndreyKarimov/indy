def gen_squares(n: int) -> int:
    for i in range(1, n + 1):
        yield i ** 2


for i in gen_squares(5):
    print(i)
