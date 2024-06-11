def gen_yield(n: int):
    for i in range(n):
        yield i


numbers = gen_yield(5)
for number in numbers:
    print(number)
