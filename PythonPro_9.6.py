def dec(func):
    def wrapper(n):
        if wrapper.count <= 3:
            wrapper.count += 1
            return print(func(n))

    wrapper.count = 1
    return wrapper


@dec
def fact(num):
    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res


fact(5)
fact(10)
fact(20)
fact(30)

