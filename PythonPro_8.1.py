def dec(func):
    liba = []

    def wrapper(*args, **kwargs):
        for j in func(*args, **kwargs):
            liba.append(j**3)

        return liba
    return wrapper


@dec
def rng(start, stop, step=1):
    while start < stop:
        yield start
        start += step


d = rng(1, 10)
for i in d:
    print(i)
