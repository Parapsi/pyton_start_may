def dec(func):
    numbers = {}

    def wrapper(n):
        key = str(n)
        if key not in numbers:
            numbers[key] = func(n)
        return numbers[key]
    return wrapper


@dec
def fact(num):

    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res


print(fact(200))
print(fact(200))
print(fact(200))
print(fact(200))
print(fact(200))
print(fact(200))
print(fact(200))
print(fact(200))