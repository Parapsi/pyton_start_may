import random


def dec(func):
    def wrapper(a):

        n = random.randint(1, 5)
        n *= func(a)
        return f"result is {n}"

    return wrapper


@dec
def fact(num):

    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res


print(fact(5))
