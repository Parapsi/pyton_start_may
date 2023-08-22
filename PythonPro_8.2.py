import time


def dec(func):
    numbers = {}

    def dic(n):
        key = str(n)
        if key not in numbers:
            numbers[key] = func(n)
        return numbers[key]
    return dic


@dec
def fibonacci(n):

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


st = time.time()
f = fibonacci(40)
et = time.time()
print(f"{f}, time to exec: {(et - st):.6f}")


def fibonacci_2(n):

    if n < 2:
        return n

    return fibonacci_2(n - 1) + fibonacci_2(n - 2)


st_1 = time.time()
f_1 = fibonacci_2(30)
et_1 = time.time()
print(f"{f_1}, time to exec: {(et_1 - st_1):.6f}")
