import random


def dec(func):
    def wrapper(a):

        n = random.randint(1, 5)
        n *= func(a)
        with open("result.txt", "w") as file:
            file.write(f"{n}")
        file.close()
        return file

    return wrapper


@dec
def fact(num):

    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res


fact(5)
