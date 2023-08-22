a = [1, 2, 4, 5, 6, 7]


def num(n):
    b = [i**3 for i in n]
    return sum(b)

print(num(a))