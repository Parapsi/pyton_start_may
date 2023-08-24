def dec(func):
    def wrapper(a):
        if not isinstance(a, int | float):
            raise TypeError("Wrong Type of a variable")
        if a <= 0:
            raise ValueError("Wrong Value of a variable")

        return print(func(a))

    return wrapper


@dec
def fact(num):

    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res


fact(0)
