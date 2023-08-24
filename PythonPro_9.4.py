
import time


def dec(func):
    st = time.time()

    def wrapper(a):
        if not isinstance(a, int | float):
            raise TypeError("Wrong Type of a variable")
        if a <= 0:
            raise ValueError("Wrong Value of a variable")

        et = time.time()
        return print(f'Result is {func(a)}\nTime to execute: {et - st}')

    return wrapper


@dec
def fact(num):
    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res


fact(999)
